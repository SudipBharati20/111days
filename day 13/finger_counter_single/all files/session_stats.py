"""
session_stats.py
================
Tracks runtime statistics for the current session:
  - total frames processed
  - total speech triggers
  - per-count frequency histogram
  - elapsed wall-clock time
Printed as a summary on exit.
"""

import time
from collections import defaultdict
from logger_setup import get_logger

logger = get_logger("finger_counter.stats")


class SessionStats:
    """
    Lightweight statistics tracker.

    Usage
    -----
    stats = SessionStats()
    stats.record_frame(count=3)
    stats.record_speech(count=3)
    print(stats.summary())
    """

    def __init__(self):
        self._start_time = time.monotonic()
        self._frames: int = 0
        self._speech_triggers: int = 0
        self._count_histogram: dict[int, int] = defaultdict(int)

    # ── Recording ─────────────────────────────────────────────────────────

    def record_frame(self, count: int) -> None:
        self._frames += 1
        self._count_histogram[count] += 1

    def record_speech(self, count: int) -> None:
        self._speech_triggers += 1

    # ── Reporting ─────────────────────────────────────────────────────────

    def summary(self) -> str:
        elapsed = time.monotonic() - self._start_time
        avg_fps = self._frames / elapsed if elapsed > 0 else 0.0
        lines = [
            "─" * 40,
            "Session Summary",
            "─" * 40,
            f"  Duration          : {elapsed:.1f}s",
            f"  Frames processed  : {self._frames}",
            f"  Average FPS       : {avg_fps:.1f}",
            f"  Speech triggers   : {self._speech_triggers}",
            "  Count histogram   :",
        ]
        for k in sorted(self._count_histogram):
            bar = "█" * min(self._count_histogram[k] // 10, 30)
            lines.append(f"    {k:>2} fingers : {self._count_histogram[k]:>6}  {bar}")
        lines.append("─" * 40)
        return "\n".join(lines)

    # ── Properties ────────────────────────────────────────────────────────

    @property
    def frames(self) -> int:
        return self._frames

    @property
    def elapsed(self) -> float:
        return time.monotonic() - self._start_time

    @property
    def average_fps(self) -> float:
        e = self.elapsed
        return self._frames / e if e > 0 else 0.0
