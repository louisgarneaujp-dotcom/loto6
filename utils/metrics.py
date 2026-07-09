"""
=========================================================
Self-Evolving LOTO6 Prediction AI Ver.7 Ultimate
metrics.py
=========================================================
"""

from __future__ import annotations

import numpy as np


def mae(y_true, y_pred):
    """
    Mean Absolute Error
    """
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    return float(np.mean(np.abs(y_true - y_pred)))


def rmse(y_true, y_pred):
    """
    Root Mean Squared Error
    """
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    return float(np.sqrt(np.mean((y_true - y_pred) ** 2)))


def accuracy(y_true, y_pred):
    """
    Exact Match Accuracy
    """
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    return float(np.mean(y_true == y_pred))


def hit_count(y_true, y_pred):
    """
    Number of matched values.
    """

    y_true = set(np.asarray(y_true).tolist())
    y_pred = set(np.asarray(y_pred).tolist())

    return len(y_true & y_pred)


def hit_rate(y_true, y_pred):
    """
    Match rate.
    """

    return hit_count(y_true, y_pred) / len(y_true)