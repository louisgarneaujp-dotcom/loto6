#feature/transition.py




"""
=========================================================
Transition Feature
Self-Evolving LOTO6 Prediction AI Ver.7 Ultimate
=========================================================
"""

from __future__ import annotations

from collections import defaultdict

import pandas as pd


class TransitionFeature:
    """
    Analyze transitions between consecutive draws.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def transition_matrix(self):

        matrix = defaultdict(lambda: defaultdict(int))

        values = self.df.values

        for i in range(len(values) - 1):

            current = sorted(values[i])
            nxt = sorted(values[i + 1])

            for a in current:
                for b in nxt:
                    matrix[a][b] += 1

        return pd.DataFrame(matrix).fillna(0).astype(int)

    def transition_probability(self):

        mat = self.transition_matrix()

        return mat.div(mat.sum(axis=0), axis=1).fillna(0)

    def strongest_transition(self, top_n=30):

        prob = self.transition_probability()

        rows = []

        for src in prob.columns:

            for dst in prob.index:

                rows.append(
                    (
                        src,
                        dst,
                        float(prob.loc[dst, src])
                    )
                )

        result = pd.DataFrame(
            rows,
            columns=[
                "from",
                "to",
                "probability"
            ]
        )

        return result.sort_values(
            "probability",
            ascending=False
        ).head(top_n)