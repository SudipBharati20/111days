"""
voice_engine.py
===============
Thread-safe text-to-speech wrapper using pyttsx3.
Runs speech synthesis in a background daemon thread to keep the video
loop non-blocking.
"""

import threading
import pyttsx3

from config import Config
from logger_setup import get_logger

logger = get_logger("finger_counter.voice")


class VoiceEngine:
    """
    Thread-safe TTS engine.

    Methods
    -------
    speak(text)   : Say `text` asynchronously (fires and forgets).
    toggle()      : Enable / disable voice output.
    is_busy       : True while speech is in progress.
    enabled       : Current on/off state.
    """

    def __init__(self, cfg: Config):
        self._cfg = cfg
        self._engine: pyttsx3.Engine = pyttsx3.init()
        self._configure_engine()
        self._lock = threading.Lock()
        self._busy = False
        self._enabled = True
        logger.info("VoiceEngine ready (rate=%d, volume=%.1f).",
                    cfg.SPEECH_RATE, cfg.SPEECH_VOLUME)

    # ── Public API ────────────────────────────────────────────────────────

    def speak(self, text: str) -> bool:
        """
        Speak `text` in a daemon thread.
        Returns False if engine is already busy or disabled.
        """
        if not self._enabled or self._busy:
            return False

        def _worker():
            self._busy = True
            with self._lock:
                try:
                    self._engine.say(text)
                    self._engine.runAndWait()
                except Exception as exc:
                    logger.warning("TTS error: %s", exc)
            self._busy = False

        t = threading.Thread(target=_worker, daemon=True, name="tts-worker")
        t.start()
        logger.debug("Queued speech: %r", text)
        return True

    def toggle(self) -> bool:
        """Toggle voice on/off. Returns new state."""
        self._enabled = not self._enabled
        state = "ON" if self._enabled else "OFF"
        logger.info("Voice toggled: %s", state)
        return self._enabled

    # ── Properties ────────────────────────────────────────────────────────

    @property
    def enabled(self) -> bool:
        return self._enabled

    @enabled.setter
    def enabled(self, value: bool) -> None:
        self._enabled = value

    @property
    def is_busy(self) -> bool:
        return self._busy

    # ── Internal ──────────────────────────────────────────────────────────

    def _configure_engine(self) -> None:
        self._engine.setProperty("rate", self._cfg.SPEECH_RATE)
        self._engine.setProperty("volume", self._cfg.SPEECH_VOLUME)
        voices = self._engine.getProperty("voices")
        if voices:
            self._engine.setProperty("voice", voices[0].id)
