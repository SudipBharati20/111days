"""
cli.py
======
Command-line interface for the Finger Counter app.
Parses sys.argv and returns an updated Config object.

Usage examples
--------------
python main.py
python main.py --camera 1 --width 640 --height 480
python main.py --no-voice
python main.py --stable-frames 12 --language nepali
"""

import argparse
from config import Config
from number_words import NumberWords
from logger_setup import get_logger

logger = get_logger("finger_counter.cli")


def parse_args(argv: list[str] | None = None) -> Config:
    """
    Parse command-line arguments and return a populated Config.

    Parameters
    ----------
    argv : list[str] | None
        Argument list (defaults to sys.argv[1:]).

    Returns
    -------
    Config
        Config instance with CLI overrides applied.
    """
    parser = argparse.ArgumentParser(
        prog="finger_counter",
        description="Finger Counter with Voice Output — show fingers to camera",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    # Camera
    cam = parser.add_argument_group("Camera")
    cam.add_argument("--camera", type=int, default=0, metavar="INDEX",
                     help="OpenCV camera device index")
    cam.add_argument("--width", type=int, default=1280,
                     help="Capture width in pixels")
    cam.add_argument("--height", type=int, default=720,
                     help="Capture height in pixels")

    # Detection
    det = parser.add_argument_group("Detection")
    det.add_argument("--det-conf", type=float, default=0.80, metavar="FLOAT",
                     help="MediaPipe hand detection confidence threshold")
    det.add_argument("--track-conf", type=float, default=0.70, metavar="FLOAT",
                     help="MediaPipe hand tracking confidence threshold")
    det.add_argument("--max-hands", type=int, default=2,
                     help="Maximum number of hands to detect")
    det.add_argument("--stable-frames", type=int, default=8,
                     help="Consecutive frames needed to confirm a count")

    # Speech
    spe = parser.add_argument_group("Speech")
    spe.add_argument("--no-voice", action="store_true",
                     help="Start with voice output disabled")
    spe.add_argument("--cooldown", type=float, default=1.5, metavar="SECONDS",
                     help="Minimum seconds between speech events")
    spe.add_argument("--language",
                     choices=NumberWords.available_languages(),
                     default="english",
                     help="Language for spoken number words")

    # Logging
    log_grp = parser.add_argument_group("Logging")
    log_grp.add_argument("--log-level",
                         choices=["DEBUG", "INFO", "WARNING", "ERROR"],
                         default="INFO",
                         help="Logging verbosity")

    ns = parser.parse_args(argv)

    cfg = Config(
        CAMERA_INDEX=ns.camera,
        FRAME_WIDTH=ns.width,
        FRAME_HEIGHT=ns.height,
        DETECTION_CONFIDENCE=ns.det_conf,
        TRACKING_CONFIDENCE=ns.track_conf,
        MAX_HANDS=ns.max_hands,
        STABLE_FRAMES=ns.stable_frames,
        SPEECH_COOLDOWN=ns.cooldown,
        LOG_LEVEL=ns.log_level,
    )

    logger.info("CLI config: camera=%d, %dx%d, stable=%d, cooldown=%.1fs, lang=%s",
                cfg.CAMERA_INDEX, cfg.FRAME_WIDTH, cfg.FRAME_HEIGHT,
                cfg.STABLE_FRAMES, cfg.SPEECH_COOLDOWN, ns.language)

    # Store extra parsed values as dynamic attributes for use in main
    cfg._no_voice = ns.no_voice    # type: ignore[attr-defined]
    cfg._language = ns.language    # type: ignore[attr-defined]

    return cfg
