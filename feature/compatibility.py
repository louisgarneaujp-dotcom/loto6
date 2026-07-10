#feature/compatibility.py



"""
=========================================================
Compatibility Feature
Self-Evolving LOTO6 Prediction AI Ver.7 Ultimate
=========================================================
"""

from __future__ import annotations

from itertools import combinations

import numpy as np
import pandas as pd


class CompatibilityFeature:
    """
    Analyze compatibility between numbers.
    """

    def __init__(self, df: pd.DataFrame):

        self.df = df.copy()

    def pair_frequency(self):

        pair_count = {}

        for row in self.df.values:

            row = sorted(row)

            for pair in combinations(row, 2):

                pair_count[pair] = pair_count.get(pair, 0) + 1

        pair_df = pd.DataFrame(
            [
                [k[0], k[1], v]
                for k, v in pair_count.items()
            ],
            columns=["num1", "num2", "count"]
        )

        return pair_df.sort_values(
            "count",
            ascending=False
        )

    def compatibility_matrix(self):

        numbers = sorted(
            np.unique(self.df.values)
        )

        matrix = pd.DataFrame(
            0,
            index=numbers,
            columns=numbers
        )

        for row in self.df.values:

            row = sorted(row)

            for a, b in combinations(row, 2):

                matrix.loc[a, b] += 1
                matrix.loc[b, a] += 1

        return matrix

    def top_pairs(self, n=20):

        pair_df = self.pair_frequency()

        return pair_df.head(n)