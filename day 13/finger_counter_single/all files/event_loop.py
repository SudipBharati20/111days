"""
event_loop.py
=============
The core capture → process → display → input loop.
Separated from main.py so it can be unit-tested or replaced
(e.g. swap in a video-file source for offline testing).
"""

import sys

from camera_manager import CameraManager
from frame_processor import FrameProcessor
from window_manager import WindowManager
from keyboard_handler import KeyboardHandler, Action
from session_stats import SessionStats
from voice_engine import VoiceEngine
from logger_setup import get_logger

logger = get_logger("finger_counter.loop")


def run_event_loop(
    camera:    CameraManager,
    processor: FrameProcessor,
    window:    WindowManager,
    keyboard:  KeyboardHandler,
    stats:     SessionStats,
    voice:     VoiceEngine,
) -> None:
    """
    Main event loop.  Blocks until the user quits.

    Parameters match the keys returned by app_builder.build_app().
    """
    logger.info("Entering event loop.")

    if not camera.open():
        logger.critical("Cannot open camera — aborting.")
        sys.exit(1)

    window.create()

    try:
        while True:
            ret, frame = camera.read()
            if not ret or frame is None:
                logger.warning("Empty frame — skipping.")
                continue

            output = processor.process(frame)
            window.show(output)

            action = keyboard.poll()

            if action == Action.QUIT:
                logger.info("Quit action received.")
                break

            elif action == Action.TOGGLE_VOICE:
                new_state = voice.toggle()
                logger.info("Voice is now %s.", "ON" if new_state else "OFF")

            elif action == Action.RESET:
                processor.reset()
                logger.info("Reset triggered by user.")

    except KeyboardInterrupt:
        logger.info("KeyboardInterrupt — exiting loop.")

    finally:
        _teardown(camera, window, stats)


def _teardown(
    camera: CameraManager,
    window: WindowManager,
    stats:  SessionStats,
) -> None:
    camera.release()
    window.destroy()
    logger.info("Teardown complete.")
    print(stats.summary())
