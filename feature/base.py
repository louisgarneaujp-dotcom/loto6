#feature/base.py




"""
=========================================================
Base Feature
Self-Evolving LOTO6 Prediction AI
=========================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod
import pandas as pd


class BaseFeature(ABC):
    """
    全てのFeatureの基底クラス
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    @abstractmethod
    def transform(self) -> dict:
        """
        特徴量辞書を返す
        """
        raise NotImplementedError