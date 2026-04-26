"""
frame_processor.py
==================
Pipeline step that takes a raw BGR frame, runs finger detection,
updates stability & stats, triggers speech, and returns a rendered frame.
All per-frame logic lives here — keeping main.py minimal.
"""

import numpy as np

from config import Config
from finger_detector import FingerDetector
from stability_buffer import StabilityBuffer
from speech_controller import SpeechController
from hud_renderer import HUDRenderer
from fps_counter import FPSCounter
from session_stats import SessionStats
from logger_setup import get_logger

logger = get_logger("finger_counter.processor")


class FrameProcessor:
    """
    Processes one BGR frame through the full pipeline and returns
    the annotated output frame ready for display.
    """

    def __init__(
        self,
        cfg: Config,
        detector: FingerDetector,
        stability: StabilityBuffer,
        speech: SpeechController,
        hud: HUDRenderer,
        fps: FPSCounter,
        stats: SessionStats,
    ):
        self._cfg       = cfg
        self._detector  = detector
        self._stability = stability
        self._speech    = speech
        self._hud       = hud
        self._fps       = fps
        self._stats     = stats
        logger.info("FrameProcessor ready.")

    def process(self, raw_frame: np.ndarray) -> np.ndarray:
        """
        Full per-frame pipeline.

        1. Detect fingers
        2. Update stability buffer
        3. Maybe trigger speech
        4. Update stats
        5. Render HUD
        6. Return annotated frame
        """
        # 1. Detect
        result = self._detector.process(raw_frame)
        count  = result.total_fingers

        # 2. Stability
        newly_stable = self._stability.update(count)
        is_stable    = self._stability.is_stable

        # 3. Speech
        spoke = self._speech.maybe_speak(count, newly_stable)
        if spoke:
            self._stats.record_speech(count)

        # 4. Stats
        current_fps = self._fps.tick()
        self._stats.record_frame(count)

        # 5. Render
        output = self._hud.draw(
            result.annotated_frame,
            count,
            is_stable,
            self._speech._voice.enabled,
            current_fps,
        )
        return output

    def reset(self) -> None:
        """Reset stability and speech controller (user-requested)."""
        self._stability.reset()
        self._speech.reset()
        logger.info("FrameProcessor state reset.")
