"""
GPU utility
"""

from __future__ import annotations

import platform


def get_device() -> str:
    """
    Returns available device.
    """

    try:
        import tensorflow as tf

        gpus = tf.config.list_physical_devices("GPU")

        if len(gpus) > 0:
            return "GPU"

    except Exception:
        pass

    return "CPU"


def print_device_info(logger=None):

    device = get_device()

    message = (
        f"Platform : {platform.system()} "
        f"{platform.release()} | Device : {device}"
    )

    if logger:
        logger.info(message)
    else:
        print(message)