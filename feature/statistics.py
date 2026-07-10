#feature/statistics.py



"""
=========================================================
Statistics Feature
=========================================================
"""

from __future__ import annotations

import numpy as np
import pandas as pd


class StatisticsFeature:
    """
    Basic statistical feature generator.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def frequency(self):

        values = self.df.values.flatten()

        freq = (
            pd.Series(values)
            .value_counts()
            .sort_index()
        )

        return freq

    def probability(self):

        freq = self.frequency()

        return freq / freq.sum()

    def summary(self):

        values = self.df.values.flatten()

        return {
            "mean": float(np.mean(values)),
            "std": float(np.std(values)),
            "min": int(np.min(values)),
            "max": int(np.max(values)),
            "median": float(np.median(values)),
        }