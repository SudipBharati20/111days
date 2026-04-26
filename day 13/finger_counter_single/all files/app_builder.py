"""
app_builder.py
==============
Factory / dependency-injection module.
Constructs all application components in the correct order
and wires them together, so main.py stays small and clean.
"""

from config import Config
from logger_setup import setup_logger, get_logger
from camera_manager import CameraManager
from finger_detector import FingerDetector
from voice_engine import VoiceEngine
from stability_buffer import StabilityBuffer
from fps_counter import FPSCounter
from number_words import NumberWords
from hud_renderer import HUDRenderer
from speech_controller import SpeechController
from frame_processor import FrameProcessor
from session_stats import SessionStats
from window_manager import WindowManager
from keyboard_handler import KeyboardHandler


def build_app(cfg: Config | None = None):
    """
    Construct and return all application objects as a namespace dict.

    Returns
    -------
    dict with keys:
        cfg, camera, detector, voice, stability, fps, words,
        hud, speech, processor, stats, window, keyboard
    """
    if cfg is None:
        cfg = Config()

    setup_logger(cfg)
    log = get_logger("finger_counter.builder")
    log.info("Building application components…")

    camera    = CameraManager(cfg)
    detector  = FingerDetector(cfg)
    voice     = VoiceEngine(cfg)
    stability = StabilityBuffer(cfg.STABLE_FRAMES)
    fps       = FPSCounter(smoothing=30)
    words     = NumberWords(language="english")
    hud       = HUDRenderer(cfg, words)
    stats     = SessionStats()
    speech    = SpeechController(cfg, voice, words)
    processor = FrameProcessor(cfg, detector, stability, speech, hud, fps, stats)
    window    = WindowManager(cfg)
    keyboard  = KeyboardHandler(wait_ms=1)

    log.info("All components built successfully.")

    return {
        "cfg":       cfg,
        "camera":    camera,
        "detector":  detector,
        "voice":     voice,
        "stability": stability,
        "fps":       fps,
        "words":     words,
        "hud":       hud,
        "stats":     stats,
        "speech":    speech,
        "processor": processor,
        "window":    window,
        "keyboard":  keyboard,
    }
