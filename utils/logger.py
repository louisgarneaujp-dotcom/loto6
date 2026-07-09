

"""
=========================================================
Self-Evolving LOTO6 Prediction AI Ver.7 Ultimate
logger.py
=========================================================
"""

from __future__ import annotations

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from datetime import datetime

try:
    from config import LOG_DIR, LOG_LEVEL
except ImportError:
    BASE = Path(__file__).resolve().parent.parent
    LOG_DIR = BASE / "logs"
    LOG_LEVEL = "INFO"

LOG_DIR.mkdir(parents=True, exist_ok=True)


def get_logger(name: str = "LOTO6_AI") -> logging.Logger:
    """
    Create or return a configured logger.
    """

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    level = getattr(logging, LOG_LEVEL.upper(), logging.INFO)
    logger.setLevel(level)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    log_file = LOG_DIR / f"{datetime.now():%Y%m%d}.log"

    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=5 * 1024 * 1024,
        backupCount=5,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logger.propagate = False

    return logger


logger = get_logger()