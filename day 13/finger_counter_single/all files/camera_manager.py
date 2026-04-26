"""
camera_manager.py
=================
Manages webcam lifecycle: open, read frames, release.
Frames are automatically mirrored (flip) for natural selfie-style interaction.
"""

import cv2
import numpy as np
from config import Config
from logger_setup import get_logger

logger = get_logger("finger_counter.camera")


class CameraManager:
    """
    Context-manager–friendly wrapper around cv2.VideoCapture.

    Usage
    -----
    cam = CameraManager(cfg)
    if cam.open():
        ret, frame = cam.read()
        ...
    cam.release()

    Or:
    with CameraManager(cfg) as cam:
        ret, frame = cam.read()
    """

    def __init__(self, cfg: Config):
        self.cfg = cfg
        self._cap: cv2.VideoCapture | None = None

    # ── Lifecycle ─────────────────────────────────────────────────────────

    def open(self) -> bool:
        """Open the camera. Returns True on success."""
        self._cap = cv2.VideoCapture(self.cfg.CAMERA_INDEX)
        if not self._cap.isOpened():
            logger.error("Cannot open camera index %d.", self.cfg.CAMERA_INDEX)
            return False

        self._cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.cfg.FRAME_WIDTH)
        self._cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.cfg.FRAME_HEIGHT)
        self._cap.set(cv2.CAP_PROP_FPS, self.cfg.TARGET_FPS)

        actual_w = int(self._cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        actual_h = int(self._cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        logger.info("Camera %d opened at %dx%d.", self.cfg.CAMERA_INDEX, actual_w, actual_h)
        return True

    def read(self) -> tuple[bool, np.ndarray | None]:
        """Read one frame. Returns (success, mirrored_BGR_frame)."""
        if self._cap is None or not self._cap.isOpened():
            return False, None
        ret, frame = self._cap.read()
        if ret:
            frame = cv2.flip(frame, 1)   # mirror so left↔right feels natural
        return ret, frame

    def release(self) -> None:
        """Release the camera resource."""
        if self._cap:
            self._cap.release()
            self._cap = None
            logger.info("Camera released.")

    # ── Context manager ───────────────────────────────────────────────────

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, *_):
        self.release()

    # ── Properties ────────────────────────────────────────────────────────

    @property
    def is_open(self) -> bool:
        return self._cap is not None and self._cap.isOpened()

    @property
    def resolution(self) -> tuple[int, int]:
        if not self.is_open:
            return (0, 0)
        return (
            int(self._cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(self._cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
        )
