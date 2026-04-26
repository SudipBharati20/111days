"""
config.py
=========
Central configuration dataclass for the Finger Counter application.
All tunable parameters live here so every other module stays clean.
"""

from dataclasses import dataclass, field
import cv2


@dataclass
class Config:
    # ── Camera ──────────────────────────────────────────────────────────────
    CAMERA_INDEX: int = 0
    FRAME_WIDTH: int = 1280
    FRAME_HEIGHT: int = 720
    TARGET_FPS: int = 30

    # ── MediaPipe ────────────────────────────────────────────────────────────
    DETECTION_CONFIDENCE: float = 0.80
    TRACKING_CONFIDENCE: float = 0.70
    MAX_HANDS: int = 2

    # ── Speech ───────────────────────────────────────────────────────────────
    SPEECH_COOLDOWN: float = 1.5   # seconds between repeated announcements
    SPEECH_RATE: int = 160         # words per minute
    SPEECH_VOLUME: float = 1.0

    # ── Stability ────────────────────────────────────────────────────────────
    STABLE_FRAMES: int = 8         # consecutive identical frames before confirming

    # ── UI / HUD ─────────────────────────────────────────────────────────────
    FONT: int = cv2.FONT_HERSHEY_SIMPLEX
    BG_COLOR: tuple = field(default_factory=lambda: (15, 15, 25))
    ACCENT_COLOR: tuple = field(default_factory=lambda: (0, 220, 180))
    TEXT_COLOR: tuple = field(default_factory=lambda: (240, 240, 240))
    WARN_COLOR: tuple = field(default_factory=lambda: (0, 80, 255))
    WINDOW_TITLE: str = "Finger Counter — Press Q to quit"

    # ── Logging ──────────────────────────────────────────────────────────────
    LOG_FILE: str = "finger_counter.log"
    LOG_LEVEL: str = "INFO"
