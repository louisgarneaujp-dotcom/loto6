"""
=========================================================
Self-Evolving LOTO6 Prediction AI Ver.7 Ultimate
seed.py
=========================================================
"""

from __future__ import annotations

import os
import random
import numpy as np


def set_seed(seed: int = 42) -> None:
    """
    Set random seed for reproducibility.
    """

    os.environ["PYTHONHASHSEED"] = str(seed)

    random.seed(seed)

    np.random.seed(seed)

    try:
        import tensorflow as tf

        tf.random.set_seed(seed)

        os.environ["TF_DETERMINISTIC_OPS"] = "1"

    except Exception:
        pass

    try:
        import torch

        torch.manual_seed(seed)

        torch.cuda.manual_seed(seed)

        torch.cuda.manual_seed_all(seed)

        torch.backends.cudnn.deterministic = True

        torch.backends.cudnn.benchmark = False

    except Exception:
        pass