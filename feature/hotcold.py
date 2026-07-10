#feature/hotcold.py




"""
=========================================================
Hot / Cold Feature
Self-Evolving LOTO6 Prediction AI Ver.7 Ultimate
=========================================================
"""

from __future__ import annotations

import pandas as pd


class HotColdFeature:
    """
    Analyze recently hot and cold numbers.
    """

    def __init__(self, df: pd.DataFrame):

        self.df = df.copy()

    def frequency(self, window=50):

        recent = self.df.tail(window)

        freq = (
            pd.Series(recent.values.flatten())
            .value_counts()
            .sort_index()
        )

        return freq

    def hot_numbers(self, top_n=10):

        freq = self.frequency()

        return freq.sort_values(
            ascending=False
        ).head(top_n)

    def cold_numbers(self, top_n=10):

        freq = self.frequency()

        all_numbers = range(1, 44)

        result = {}

        for n in all_numbers:

            result[n] = int(freq.get(n, 0))

        return (
            pd.Series(result)
            .sort_values()
            .head(top_n)
        )

    def hotcold_score(self):

        freq = self.frequency()

        score = {}

        max_freq = freq.max()

        for n in range(1, 44):

            score[n] = float(
                freq.get(n, 0) / max_freq
            ) if max_freq > 0 else 0

        return pd.Series(score)