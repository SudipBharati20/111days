"""
main.py
=======
Entry point for the modular Finger Counter application.

Wires together:
  CLI argument parsing → app_builder → event_loop

Usage
-----
python main.py                           # default settings
python main.py --camera 1               # use second webcam
python main.py --no-voice               # silent mode
python main.py --language nepali        # speak Nepali numbers
python main.py --stable-frames 12       # slower confirmation
python main.py --help                   # full option list
"""

import sys
from cli import parse_args
from app_builder import build_app
from event_loop import run_event_loop
from logger_setup import get_logger


def main(argv: list[str] | None = None) -> int:
    """
    Application entry point.

    Parameters
    ----------
    argv : list[str] | None
        Override sys.argv for testing.

    Returns
    -------
    int
        Exit code (0 = success).
    """
    # 1. Parse CLI
    cfg = parse_args(argv)

    # 2. Build all components
    components = build_app(cfg)

    log = get_logger("finger_counter.main")
    log.info("Finger Counter starting…")

    # 3. Apply CLI-only overrides
    if getattr(cfg, "_no_voice", False):
        components["voice"].enabled = False
        log.info("Voice disabled via CLI flag.")

    # Swap number words language if specified
    lang = getattr(cfg, "_language", "english")
    if lang != "english":
        from number_words import NumberWords
        new_words = NumberWords(language=lang)
        components["hud"]._words   = new_words   # patch HUDRenderer
        components["speech"]._words = new_words  # patch SpeechController
        log.info("Language set to %r.", lang)

    # 4. Run
    try:
        run_event_loop(
            camera    = components["camera"],
            processor = components["processor"],
            window    = components["window"],
            keyboard  = components["keyboard"],
            stats     = components["stats"],
            voice     = components["voice"],
        )
    except Exception as exc:
        log.exception("Unhandled exception in event loop: %s", exc)
        return 1

    log.info("Application exited normally.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
