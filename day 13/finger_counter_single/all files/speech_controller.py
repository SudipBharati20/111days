"""
speech_controller.py
====================
Decides *when* to trigger a voice announcement.
Applies cooldown and change-detection logic so the TTS engine
isn't called redundantly.
"""

import time

from config import Config
from voice_engine import VoiceEngine
from number_words import NumberWords
from logger_setup import get_logger

logger = get_logger("finger_counter.speech_ctrl")


class SpeechController:
    """
    Wraps VoiceEngine with cooldown and deduplication logic.

    Parameters
    ----------
    cfg   : Config
    voice : VoiceEngine instance
    words : NumberWords instance
    """

    def __init__(self, cfg: Config, voice: VoiceEngine, words: NumberWords):
        self._cfg   = cfg
        self._voice = voice
        self._words = words
        self._last_spoken_count: int   = -1
        self._last_speech_time:  float = 0.0
        self._total_spoken: int = 0
        logger.info("SpeechController initialised.")

    # ── Public API ────────────────────────────────────────────────────────

    def maybe_speak(self, count: int, newly_stable: bool) -> bool:
        """
        Speak `count` if conditions are met.

        Parameters
        ----------
        count        : Confirmed finger count.
        newly_stable : True when StabilityBuffer just confirmed a new value.

        Returns True if speech was triggered.
        """
        if not newly_stable:
            return False
        if count == 0:
            return False
        if not self._voice.enabled:
            return False
        if self._voice.is_busy:
            return False

        now = time.monotonic()
        cooldown_ok = (now - self._last_speech_time) >= self._cfg.SPEECH_COOLDOWN
        new_count   = count != self._last_spoken_count

        if not (cooldown_ok or new_count):
            return False

        word = self._words.word(count)
        triggered = self._voice.speak(word)
        if triggered:
            self._last_spoken_count = count
            self._last_speech_time  = now
            self._total_spoken     += 1
            logger.info("Spoke %r for count=%d (total_spoken=%d).",
                        word, count, self._total_spoken)
        return triggered

    def reset(self) -> None:
        """Reset speech state (e.g. after user presses R)."""
        self._last_spoken_count = -1
        self._last_speech_time  = 0.0
        logger.debug("SpeechController reset.")

    # ── Properties ────────────────────────────────────────────────────────

    @property
    def last_spoken_count(self) -> int:
        return self._last_spoken_count

    @property
    def total_spoken(self) -> int:
        return self._total_spoken
