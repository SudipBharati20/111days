"""
window_manager.py
=================
Creates and manages the OpenCV display window.
Abstracts window creation, resizing, frame display, and teardown.
"""

import cv2
import numpy as np

from config import Config
from logger_setup import get_logger

logger = get_logger("finger_counter.window")


class WindowManager:
    """
    Manages the OpenCV named window lifecycle.

    Usage
    -----
    wm = WindowManager(cfg)
    wm.create()
    wm.show(frame)
    wm.destroy()
    """

    def __init__(self, cfg: Config):
        self._cfg   = cfg
        self._title = cfg.WINDOW_TITLE
        self._open  = False

    # ── Lifecycle ─────────────────────────────────────────────────────────

    def create(self, resizable: bool = True) -> None:
        flag = cv2.WINDOW_NORMAL if resizable else cv2.WINDOW_AUTOSIZE
        cv2.namedWindow(self._title, flag)
        self._open = True
        logger.info("Window %r created (resizable=%s).", self._title, resizable)

    def show(self, frame: np.ndarray) -> None:
        """Display a BGR frame."""
        if not self._open:
            self.create()
        cv2.imshow(self._title, frame)

    def destroy(self) -> None:
        if self._open:
            cv2.destroyAllWindows()
            self._open = False
            logger.info("Window destroyed.")

    # ── Convenience ───────────────────────────────────────────────────────

    def set_title(self, title: str) -> None:
        """Update window title (creates a new window if not already open)."""
        if self._open:
            cv2.setWindowTitle(self._title, title)
        self._title = title

    @property
    def is_open(self) -> bool:
        return self._open

    # ── Context manager ───────────────────────────────────────────────────

    def __enter__(self):
        self.create()
        return self

    def __exit__(self, *_):
        self.destroy()
