"""
File I/O Utility
"""

from __future__ import annotations

from pathlib import Path
import pandas as pd


def load_csv(path):

    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(path)

    return pd.read_csv(path)


def save_csv(df, path):

    path = Path(path)

    path.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(path, index=False)


def ensure_dir(path):

    path = Path(path)

    path.mkdir(parents=True, exist_ok=True)

    return path