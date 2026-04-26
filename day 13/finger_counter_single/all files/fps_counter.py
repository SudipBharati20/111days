"""
fps_counter.py
==============
Smoothed frames-per-second counter using a rolling time window.
"""

import time
from collections import deque
from logger_setup import get_logger

logger = get_logger("finger_counter.fps")


class FPSCounter:
    """
    Calculates a smoothed FPS value over a rolling window of timestamps.

    Parameters
    ----------
    smoothing : int
        Number of recent frame timestamps to keep for averaging.

    Usage
    -----
    fps = FPSCounter(smoothing=30)
    while capturing:
        fps.tick()
        display(fps.value)
    """

    def __init__(self, smoothing: int = 30):
        if smoothing < 2:
            raise ValueError("smoothing must be >= 2")
        self._smoothing = smoothing
        self._times: deque[float] = deque(maxlen=smoothing)
        self._peak: float = 0.0

    def tick(self) -> float:
        """
        Record the current time as a frame boundary.
        Returns the current smoothed FPS.
        """
        self._times.append(time.perf_counter())
        current = self.value
        if current > self._peak:
            self._peak = current
        return current

    @property
    def value(self) -> float:
        """Current smoothed FPS. Returns 0.0 if not enough data yet."""
        if len(self._times) < 2:
            return 0.0
        elapsed = self._times[-1] - self._times[0]
        return (len(self._times) - 1) / elapsed if elapsed > 0 else 0.0

    @property
    def peak(self) -> float:
        """Highest FPS observed since creation."""
        return self._peak

    def reset(self) -> None:
        """Clear history."""
        self._times.clear()
        self._peak = 0.0
        logger.debug("FPSCounter reset.")
