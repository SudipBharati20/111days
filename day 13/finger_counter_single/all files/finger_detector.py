"""
finger_detector.py
==================
Wraps MediaPipe Hands to detect and count raised fingers.
Supports both hands (up to 10 fingers total).
Returns the annotated frame along with the finger count.
"""

import cv2
import mediapipe as mp
import numpy as np
from dataclasses import dataclass

from config import Config
from logger_setup import get_logger

logger = get_logger("finger_counter.detector")


@dataclass
class DetectionResult:
    total_fingers: int
    annotated_frame: np.ndarray
    hands_detected: int


class FingerDetector:
    """
    Counts raised fingers using MediaPipe Hands landmarks.

    Finger-up logic
    ---------------
    * Thumb  : compare x-coordinates (tip vs IP joint), flipped per hand side.
    * Others : tip y-coordinate < PIP joint y-coordinate → finger is raised.
    """

    # Landmark indices
    TIPS: list[int] = [4, 8, 12, 16, 20]
    PIPS: list[int] = [3, 6, 10, 14, 18]

    def __init__(self, cfg: Config):
        self.cfg = cfg
        _mp = mp.solutions.hands
        self._hands = _mp.Hands(
            static_image_mode=False,
            max_num_hands=cfg.MAX_HANDS,
            min_detection_confidence=cfg.DETECTION_CONFIDENCE,
            min_tracking_confidence=cfg.TRACKING_CONFIDENCE,
        )
        self._draw = mp.solutions.drawing_utils
        self._styles = mp.solutions.drawing_styles
        self._mp_hands = _mp
        logger.info(
            "FingerDetector ready (max_hands=%d, det=%.2f, track=%.2f).",
            cfg.MAX_HANDS, cfg.DETECTION_CONFIDENCE, cfg.TRACKING_CONFIDENCE,
        )

    # ── Public API ────────────────────────────────────────────────────────

    def process(self, bgr_frame: np.ndarray) -> DetectionResult:
        """
        Process one BGR frame.

        Parameters
        ----------
        bgr_frame : np.ndarray
            Raw BGR frame from the camera.

        Returns
        -------
        DetectionResult
            total_fingers, annotated frame, number of hands detected.
        """
        rgb = cv2.cvtColor(bgr_frame, cv2.COLOR_BGR2RGB)
        results = self._hands.process(rgb)
        annotated = bgr_frame.copy()
        total = 0
        hands_found = 0

        if results.multi_hand_landmarks:
            for hand_lm, hand_info in zip(
                results.multi_hand_landmarks, results.multi_handedness
            ):
                label = hand_info.classification[0].label  # "Left" | "Right"
                total += self._count_fingers(hand_lm, label)
                hands_found += 1
                self._draw.draw_landmarks(
                    annotated,
                    hand_lm,
                    self._mp_hands.HAND_CONNECTIONS,
                    self._styles.get_default_hand_landmarks_style(),
                    self._styles.get_default_hand_connections_style(),
                )

        return DetectionResult(
            total_fingers=total,
            annotated_frame=annotated,
            hands_detected=hands_found,
        )

    def release(self) -> None:
        self._hands.close()
        logger.info("FingerDetector released.")

    # ── Helpers ───────────────────────────────────────────────────────────

    def _count_fingers(self, landmarks, hand_label: str) -> int:
        lm = landmarks.landmark
        count = 0

        # Thumb (horizontal comparison, side-dependent)
        if hand_label == "Right":
            if lm[self.TIPS[0]].x < lm[self.PIPS[0]].x:
                count += 1
        else:
            if lm[self.TIPS[0]].x > lm[self.PIPS[0]].x:
                count += 1

        # Index → Pinky (vertical comparison)
        for tip_idx, pip_idx in zip(self.TIPS[1:], self.PIPS[1:]):
            if lm[tip_idx].y < lm[pip_idx].y:
                count += 1

        return count
