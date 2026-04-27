"""
logger_setup.py
===============
Configures and returns the application-wide logger.
Call `get_logger()` from any module to obtain the shared logger instance.
"""

import logging
import sys
from config import Config


_logger: logging.Logger | None = None


def setup_logger(cfg: Config | None = None) -> logging.Logger:
    """
    Initialise the root logger once.  Subsequent calls return the same instance.
    """
    global _logger
    if _logger is not None:
        return _logger

    log_cfg = cfg or Config()
    level = getattr(logging, log_cfg.LOG_LEVEL.upper(), logging.INFO)

    fmt = logging.Formatter(
        fmt="%(asctime)s [%(levelname)-8s] %(name)s — %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    handlers: list[logging.Handler] = [
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(log_cfg.LOG_FILE, encoding="utf-8"),
    ]
    for h in handlers:
        h.setFormatter(fmt)

    root = logging.getLogger("finger_counter")
    root.setLevel(level)
    for h in handlers:
        root.addHandler(h)
    root.propagate = False

    _logger = root
    _logger.info("Logger initialised (level=%s).", log_cfg.LOG_LEVEL)
    return _logger


def get_logger(name: str = "finger_counter") -> logging.Logger:
    """Return (or create) the named child logger."""
    if _logger is None:
        setup_logger()
    return logging.getLogger(name)
