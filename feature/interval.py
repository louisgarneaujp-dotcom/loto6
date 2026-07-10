#feature/interval.py



"""
=========================================================
Interval Feature
Self-Evolving LOTO6 Prediction AI Ver.7 Ultimate
=========================================================
"""

from __future__ import annotations

import pandas as pd
import numpy as np


class IntervalFeature:
    """
    Analyze appearance intervals for each number.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def interval_table(self):

        values = self.df.values

        history = {}

        interval = {}

        for draw_idx, row in enumerate(values):

            for n in row:

                if n not in history:
                    history[n] = []

                history[n].append(draw_idx)

        for number, idx in history.items():

            if len(idx) <= 1:

                interval[number] = {
                    "mean": np.nan,
                    "last_gap": np.nan,
                    "max_gap": np.nan,
                    "min_gap": np.nan,
                }

                continue

            gaps = np.diff(idx)

            interval[number] = {
                "mean": float(np.mean(gaps)),
                "last_gap": int(gaps[-1]),
                "max_gap": int(np.max(gaps)),
                "min_gap": int(np.min(gaps)),
            }

        return pd.DataFrame(interval).T