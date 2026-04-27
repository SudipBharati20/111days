"""
stability_buffer.py
===================
Prevents flickering by only confirming a detected value once it has
remained the same for `required_frames` consecutive frames.

This is critical for smooth voice output — without stabilisation, the
TTS engine would be triggered dozens of times per second on a noisy signal.
"""

from logger_setup import get_logger

logger = get_logger("finger_counter.stability")


class StabilityBuffer:
    """
    Sliding-window majority filter for finger count values.

    Parameters
    ----------
    required_frames : int
        Number of consecutive identical readings before `is_stable` is True.

    Example
    -------
    buf = StabilityBuffer(required_frames=8)
    for count in stream_of_counts:
        stable = buf.update(count)
        if stable:
            speak(buf.confirmed_value)
    """

    def __init__(self, required_frames: int = 8):
        if required_frames < 1:
            raise ValueError("required_frames must be >= 1")
        self._required = required_frames
        self._streak: int = 0
        self._last_value: int = -1
        self._confirmed: int = -1
        logger.debug("StabilityBuffer created (required=%d).", required_frames)

    # ── Public API ────────────────────────────────────────────────────────

    def update(self, value: int) -> bool:
        """
        Feed a new observed value.

        Returns True when `value` has been stable for `required_frames`
        and is *different* from the previously confirmed value.
        """
        if value == self._last_value:
            self._streak += 1
        else:
            self._streak = 1
            self._last_value = value

        if self._streak >= self._required:
            if value != self._confirmed:
                self._confirmed = value
                logger.debug("Confirmed value=%d after %d stable frames.",
                             value, self._streak)
                return True   # newly confirmed — trigger speech / action
        return False

    def reset(self) -> None:
        """Clear internal state (e.g. on user reset request)."""
        self._streak = 0
        self._last_value = -1
        self._confirmed = -1
        logger.debug("StabilityBuffer reset.")

    # ── Properties ────────────────────────────────────────────────────────

    @property
    def current_value(self) -> int:
        """Most recently seen value (may not yet be stable)."""
        return self._last_value

    @property
    def confirmed_value(self) -> int:
        """Last value that passed the stability threshold."""
        return self._confirmed

    @property
    def streak(self) -> int:
        """Current consecutive-frame count for the current value."""
        return self._streak

    @property
    def is_stable(self) -> bool:
        """True if the current streak meets the threshold."""
        return self._streak >= self._required
