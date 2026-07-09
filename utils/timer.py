"""
=========================================================
Self-Evolving LOTO6 Prediction AI Ver.7 Ultimate
timer.py
=========================================================
"""

from __future__ import annotations

import time
from contextlib import ContextDecorator


class Timer(ContextDecorator):
    """
    Simple execution timer.
    """

    def __init__(self, name: str = "Task", logger=None):
        self.name = name
        self.logger = logger
        self.start_time = 0.0
        self.elapsed = 0.0

    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc, tb):
        self.elapsed = time.perf_counter() - self.start_time

        message = f"{self.name} finished in {self.elapsed:.3f} sec"

        if self.logger:
            self.logger.info(message)
        else:
            print(message)

        return False


def time_function(func):
    """
    Decorator for measuring execution time.
    """

    def wrapper(*args, **kwargs):
        start = time.perf_counter()

        result = func(*args, **kwargs)

        elapsed = time.perf_counter() - start

        print(f"{func.__name__} : {elapsed:.3f} sec")

        return result

    return wrapper