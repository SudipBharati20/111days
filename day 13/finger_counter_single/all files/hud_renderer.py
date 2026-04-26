"""
hud_renderer.py
===============
Draws all on-screen overlays onto a BGR frame:
  • Translucent top bar with title & FPS
  • Large centred digit + word label
  • Glow effect around the digit
  • Stability ring indicator
  • Controls hint bar at the bottom
"""

import cv2
import numpy as np

from config import Config
from number_words import NumberWords
from logger_setup import get_logger

logger = get_logger("finger_counter.hud")


class HUDRenderer:
    """
    Stateless renderer — call ``draw()`` every frame with current state.
    """

    def __init__(self, cfg: Config, words: NumberWords | None = None):
        self.cfg = cfg
        self.words = words or NumberWords()
        logger.info("HUDRenderer initialised.")

    # ── Public API ────────────────────────────────────────────────────────

    def draw(
        self,
        frame: np.ndarray,
        count: int,
        stable: bool,
        voice_on: bool,
        fps: float,
    ) -> np.ndarray:
        """
        Render all HUD elements onto `frame` (in-place copy).

        Parameters
        ----------
        frame    : BGR frame already annotated with hand landmarks.
        count    : Current finger count (0-10).
        stable   : Whether the count has passed the stability threshold.
        voice_on : Voice toggle state.
        fps      : Current FPS for display.
        """
        out = frame.copy()
        h, w = out.shape[:2]

        self._draw_top_bar(out, w, fps)
        self._draw_voice_status(out, w, h, voice_on)

        if count > 0:
            self._draw_count(out, w, h, count, stable)
        else:
            self._draw_idle_msg(out, w, h)

        self._draw_controls_hint(out, h)
        return out

    # ── Private helpers ───────────────────────────────────────────────────

    def _draw_top_bar(self, frame, w, fps):
        overlay = frame.copy()
        cv2.rectangle(overlay, (0, 0), (w, 70), (10, 10, 20), -1)
        cv2.addWeighted(overlay, 0.65, frame, 0.35, 0, frame)
        cv2.putText(frame, "Finger Counter",
                    (14, 46), self.cfg.FONT, 1.1,
                    self.cfg.ACCENT_COLOR, 2, cv2.LINE_AA)
        cv2.putText(frame, f"FPS: {fps:.1f}",
                    (w - 155, 46), self.cfg.FONT, 0.75,
                    self.cfg.TEXT_COLOR, 1, cv2.LINE_AA)

    def _draw_voice_status(self, frame, w, h, voice_on):
        color = self.cfg.ACCENT_COLOR if voice_on else self.cfg.WARN_COLOR
        label = "Voice: ON" if voice_on else "Voice: OFF"
        cv2.putText(frame, label,
                    (w - 155, h - 20), self.cfg.FONT, 0.6,
                    color, 1, cv2.LINE_AA)

    def _draw_count(self, frame, w, h, count, stable):
        digit = str(count)
        word  = self.words.word(count)
        fs    = 5.0
        thick = 12
        (tw, th), _ = cv2.getTextSize(digit, self.cfg.FONT, fs, thick)
        cx = (w - tw) // 2
        cy = h // 2 + th // 2

        # Glow layers
        for blur in (30, 20, 10):
            glow = tuple(int(c * 0.25) for c in self.cfg.ACCENT_COLOR)
            cv2.putText(frame, digit, (cx, cy),
                        self.cfg.FONT, fs, glow,
                        thick + blur, cv2.LINE_AA)
        # Main digit
        cv2.putText(frame, digit, (cx, cy),
                    self.cfg.FONT, fs, self.cfg.ACCENT_COLOR,
                    thick, cv2.LINE_AA)

        # Word below digit
        (ww, wh), _ = cv2.getTextSize(word, self.cfg.FONT, 1.4, 2)
        cv2.putText(frame, word,
                    ((w - ww) // 2, cy + wh + 22),
                    self.cfg.FONT, 1.4, self.cfg.TEXT_COLOR, 2, cv2.LINE_AA)

        # Stability ring
        ring_col = self.cfg.ACCENT_COLOR if stable else (80, 80, 80)
        cv2.circle(frame, (w // 2, h // 2), 125, ring_col, 2)

    def _draw_idle_msg(self, frame, w, h):
        msg = "Show your fingers!"
        (mw, _), _ = cv2.getTextSize(msg, self.cfg.FONT, 1.2, 2)
        cv2.putText(frame, msg,
                    ((w - mw) // 2, h // 2),
                    self.cfg.FONT, 1.2, (110, 110, 110), 2, cv2.LINE_AA)

    def _draw_controls_hint(self, frame, h):
        hints = "[Q] Quit   [S] Toggle Voice   [R] Reset"
        cv2.putText(frame, hints,
                    (14, h - 20), self.cfg.FONT, 0.55,
                    (90, 90, 110), 1, cv2.LINE_AA)
