"""
Finger Counter with Voice Output
=================================
Uses webcam + MediaPipe to detect number of raised fingers (1-10)
and speaks the count aloud using pyttsx3.

Requirements:
    pip install opencv-python mediapipe pyttsx3 numpy

Usage:
    python finger_counter.py

Controls:
    Q  - Quit
    S  - Toggle speech on/off
    R  - Reset/recalibrate
"""

import cv2
import mediapipe as mp
import pyttsx3
import numpy as np
import time
import threading
import logging
import sys
import os

# ─────────────────────────────────────────────
# LOGGING SETUP
# ─────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("finger_counter.log"),
    ],
)
logger = logging.getLogger(__name__)


# ─────────────────────────────────────────────
# CONFIGURATION
# ─────────────────────────────────────────────
class Config:
    CAMERA_INDEX: int = 0
    FRAME_WIDTH: int = 1280
    FRAME_HEIGHT: int = 720
    DETECTION_CONFIDENCE: float = 0.8
    TRACKING_CONFIDENCE: float = 0.7
    MAX_HANDS: int = 2
    SPEECH_COOLDOWN: float = 1.5   # seconds between speech outputs
    STABLE_FRAMES: int = 8         # frames count must be stable before speaking
    FONT = cv2.FONT_HERSHEY_SIMPLEX
    BG_COLOR = (15, 15, 25)
    ACCENT_COLOR = (0, 220, 180)
    TEXT_COLOR = (240, 240, 240)
    WARN_COLOR = (0, 80, 255)
    WINDOW_TITLE = "Finger Counter — Press Q to quit"


# ─────────────────────────────────────────────
# TTS ENGINE
# ─────────────────────────────────────────────
class VoiceEngine:
    """Thread-safe wrapper around pyttsx3."""

    def __init__(self):
        self._engine = pyttsx3.init()
        self._engine.setProperty("rate", 160)
        self._engine.setProperty("volume", 1.0)
        voices = self._engine.getProperty("voices")
        if voices:
            self._engine.setProperty("voice", voices[0].id)
        self._lock = threading.Lock()
        self._busy = False
        self.enabled = True
        logger.info("VoiceEngine initialised.")

    def speak(self, text: str):
        if not self.enabled or self._busy:
            return

        def _run():
            self._busy = True
            with self._lock:
                try:
                    self._engine.say(text)
                    self._engine.runAndWait()
                except Exception as exc:
                    logger.warning("TTS error: %s", exc)
            self._busy = False

        threading.Thread(target=_run, daemon=True).start()

    def toggle(self):
        self.enabled = not self.enabled
        state = "ON" if self.enabled else "OFF"
        logger.info("Voice %s", state)
        return state


# ─────────────────────────────────────────────
# FINGER DETECTION
# ─────────────────────────────────────────────
class FingerDetector:
    """
    Counts raised fingers using MediaPipe Hands.
    Supports both hands (max 10 fingers).
    """

    # Landmark indices for finger tips and their PIP joints
    TIPS = [4, 8, 12, 16, 20]
    PIPS = [3, 6, 10, 14, 18]

    def __init__(self, cfg: Config):
        self._mp_hands = mp.solutions.hands
        self._mp_draw = mp.solutions.drawing_utils
        self._mp_styles = mp.solutions.drawing_styles
        self.hands = self._mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=cfg.MAX_HANDS,
            min_detection_confidence=cfg.DETECTION_CONFIDENCE,
            min_tracking_confidence=cfg.TRACKING_CONFIDENCE,
        )
        self.cfg = cfg
        logger.info("FingerDetector initialised (max_hands=%d).", cfg.MAX_HANDS)

    def _count_hand(self, landmarks, hand_label: str) -> int:
        lm = landmarks.landmark
        count = 0

        # Thumb — compare x-axis (mirrored for left/right)
        if hand_label == "Right":
            if lm[self.TIPS[0]].x < lm[self.PIPS[0]].x:
                count += 1
        else:
            if lm[self.TIPS[0]].x > lm[self.PIPS[0]].x:
                count += 1

        # Other four fingers — tip y above pip y means raised
        for tip, pip in zip(self.TIPS[1:], self.PIPS[1:]):
            if lm[tip].y < lm[pip].y:
                count += 1

        return count

    def process(self, frame_rgb: np.ndarray):
        """
        Returns (total_finger_count, annotated_bgr_frame, hand_results).
        """
        results = self.hands.process(frame_rgb)
        annotated = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR)
        total = 0

        if results.multi_hand_landmarks:
            for hand_lm, hand_info in zip(
                results.multi_hand_landmarks, results.multi_handedness
            ):
                label = hand_info.classification[0].label
                total += self._count_hand(hand_lm, label)
                self._mp_draw.draw_landmarks(
                    annotated,
                    hand_lm,
                    self._mp_hands.HAND_CONNECTIONS,
                    self._mp_styles.get_default_hand_landmarks_style(),
                    self._mp_styles.get_default_hand_connections_style(),
                )

        return total, annotated, results

    def release(self):
        self.hands.close()


# ─────────────────────────────────────────────
# STABILITY BUFFER
# ─────────────────────────────────────────────
class StabilityBuffer:
    """
    Only confirms a count once it has been stable for N consecutive frames.
    Prevents flickering speech triggers.
    """

    def __init__(self, required_frames: int = 8):
        self.required = required_frames
        self._last = -1
        self._streak = 0

    def update(self, value: int) -> bool:
        """Returns True when value has been stable for `required` frames."""
        if value == self._last:
            self._streak += 1
        else:
            self._streak = 1
            self._last = value
        return self._streak >= self.required

    @property
    def current(self) -> int:
        return self._last


# ─────────────────────────────────────────────
# HUD / OVERLAY RENDERER
# ─────────────────────────────────────────────
class HUDRenderer:
    """Draws all on-screen overlays."""

    NUMBER_WORDS = [
        "", "One", "Two", "Three", "Four", "Five",
        "Six", "Seven", "Eight", "Nine", "Ten",
    ]

    def __init__(self, cfg: Config):
        self.cfg = cfg

    def draw(
        self,
        frame: np.ndarray,
        count: int,
        stable: bool,
        voice_on: bool,
        fps: float,
    ) -> np.ndarray:
        h, w = frame.shape[:2]
        overlay = frame.copy()

        # Semi-transparent top bar
        cv2.rectangle(overlay, (0, 0), (w, 70), (10, 10, 20), -1)
        cv2.addWeighted(overlay, 0.7, frame, 0.3, 0, frame)

        # Title
        cv2.putText(frame, "Finger Counter", (14, 44),
                    self.cfg.FONT, 1.1, self.cfg.ACCENT_COLOR, 2, cv2.LINE_AA)

        # FPS
        cv2.putText(frame, f"FPS: {fps:.1f}", (w - 150, 44),
                    self.cfg.FONT, 0.75, self.cfg.TEXT_COLOR, 1, cv2.LINE_AA)

        # Voice status
        v_color = self.cfg.ACCENT_COLOR if voice_on else self.cfg.WARN_COLOR
        v_text = "Voice: ON" if voice_on else "Voice: OFF"
        cv2.putText(frame, v_text, (w - 150, h - 20),
                    self.cfg.FONT, 0.6, v_color, 1, cv2.LINE_AA)

        # Big count display
        if count > 0:
            word = self.NUMBER_WORDS[min(count, 10)]
            count_str = str(count)
            font_scale = 5.0
            thickness = 12
            (tw, th), _ = cv2.getTextSize(count_str, self.cfg.FONT, font_scale, thickness)
            cx = (w - tw) // 2
            cy = h // 2 + th // 2

            # Glow effect
            for blur in [30, 20, 10]:
                color_dim = tuple(int(c * 0.3) for c in self.cfg.ACCENT_COLOR)
                cv2.putText(frame, count_str, (cx, cy),
                            self.cfg.FONT, font_scale, color_dim, thickness + blur, cv2.LINE_AA)
            cv2.putText(frame, count_str, (cx, cy),
                        self.cfg.FONT, font_scale, self.cfg.ACCENT_COLOR, thickness, cv2.LINE_AA)

            # Word label below
            (ww, wh), _ = cv2.getTextSize(word, self.cfg.FONT, 1.4, 2)
            wx = (w - ww) // 2
            cv2.putText(frame, word, (wx, cy + wh + 20),
                        self.cfg.FONT, 1.4, self.cfg.TEXT_COLOR, 2, cv2.LINE_AA)

            # Stability indicator ring
            ring_color = self.cfg.ACCENT_COLOR if stable else (100, 100, 100)
            cv2.circle(frame, (w // 2, h // 2), 120, ring_color, 2)

        else:
            msg = "Show your fingers!"
            (mw, _), _ = cv2.getTextSize(msg, self.cfg.FONT, 1.2, 2)
            cv2.putText(frame, msg, ((w - mw) // 2, h // 2),
                        self.cfg.FONT, 1.2, (120, 120, 120), 2, cv2.LINE_AA)

        # Controls hint
        hints = "[Q] Quit   [S] Toggle Voice   [R] Reset"
        cv2.putText(frame, hints, (14, h - 20),
                    self.cfg.FONT, 0.55, (100, 100, 120), 1, cv2.LINE_AA)

        return frame


# ─────────────────────────────────────────────
# CAMERA MANAGER
# ─────────────────────────────────────────────
class CameraManager:
    """Handles webcam lifecycle."""

    def __init__(self, cfg: Config):
        self.cfg = cfg
        self.cap = None

    def open(self) -> bool:
        self.cap = cv2.VideoCapture(self.cfg.CAMERA_INDEX)
        if not self.cap.isOpened():
            logger.error("Cannot open camera index %d", self.cfg.CAMERA_INDEX)
            return False
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.cfg.FRAME_WIDTH)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.cfg.FRAME_HEIGHT)
        self.cap.set(cv2.CAP_PROP_FPS, 30)
        logger.info("Camera opened: %dx%d",
                    int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                    int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        return True

    def read(self):
        if self.cap is None:
            return False, None
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.flip(frame, 1)   # Mirror for natural interaction
        return ret, frame

    def release(self):
        if self.cap:
            self.cap.release()
            logger.info("Camera released.")


# ─────────────────────────────────────────────
# FPS COUNTER
# ─────────────────────────────────────────────
class FPSCounter:
    def __init__(self, smoothing: int = 30):
        self._times = []
        self._smoothing = smoothing

    def tick(self) -> float:
        now = time.perf_counter()
        self._times.append(now)
        if len(self._times) > self._smoothing:
            self._times.pop(0)
        if len(self._times) < 2:
            return 0.0
        elapsed = self._times[-1] - self._times[0]
        return (len(self._times) - 1) / elapsed if elapsed > 0 else 0.0


# ─────────────────────────────────────────────
# MAIN APPLICATION
# ─────────────────────────────────────────────
class FingerCounterApp:
    """Orchestrates all components."""

    def __init__(self):
        self.cfg = Config()
        self.camera = CameraManager(self.cfg)
        self.detector = FingerDetector(self.cfg)
        self.voice = VoiceEngine()
        self.hud = HUDRenderer(self.cfg)
        self.buffer = StabilityBuffer(self.cfg.STABLE_FRAMES)
        self.fps_counter = FPSCounter()
        self._last_spoken = -1
        self._last_speech_time = 0.0

    def _should_speak(self, count: int, stable: bool) -> bool:
        if not stable:
            return False
        if count == 0:
            return False
        now = time.time()
        if count == self._last_spoken and (now - self._last_speech_time) < self.cfg.SPEECH_COOLDOWN:
            return False
        return True

    def run(self):
        logger.info("Starting Finger Counter App…")
        if not self.camera.open():
            logger.critical("Failed to open camera. Exiting.")
            sys.exit(1)

        cv2.namedWindow(self.cfg.WINDOW_TITLE, cv2.WINDOW_NORMAL)

        try:
            while True:
                ret, frame = self.camera.read()
                if not ret:
                    logger.warning("Empty frame received.")
                    continue

                # Convert to RGB for MediaPipe
                rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                count, annotated, _ = self.detector.process(rgb)

                stable = self.buffer.update(count)
                fps = self.fps_counter.tick()

                # Speak if stable new count
                if self._should_speak(count, stable):
                    words = HUDRenderer.NUMBER_WORDS[min(count, 10)]
                    self.voice.speak(words)
                    self._last_spoken = count
                    self._last_speech_time = time.time()
                    logger.info("Spoke: %s (%d finger(s))", words, count)

                # Render HUD
                output = self.hud.draw(annotated, count, stable, self.voice.enabled, fps)
                cv2.imshow(self.cfg.WINDOW_TITLE, output)

                # Key handling
                key = cv2.waitKey(1) & 0xFF
                if key == ord("q"):
                    logger.info("Quit requested.")
                    break
                elif key == ord("s"):
                    state = self.voice.toggle()
                    logger.info("Voice toggled: %s", state)
                elif key == ord("r"):
                    self.buffer = StabilityBuffer(self.cfg.STABLE_FRAMES)
                    self._last_spoken = -1
                    logger.info("Reset.")

        except KeyboardInterrupt:
            logger.info("Interrupted by user.")
        finally:
            self._cleanup()

    def _cleanup(self):
        self.camera.release()
        self.detector.release()
        cv2.destroyAllWindows()
        logger.info("Cleanup complete.")


# ─────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────
if __name__ == "__main__":
    app = FingerCounterApp()
    app.run()
