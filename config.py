
"""
=========================================================
 Self-Evolving LOTO6 Prediction AI Ver.7 Ultimate
 config.py
=========================================================
"""

from pathlib import Path
import os
import random
import numpy as np

# =====================================================
# Project Information
# =====================================================

PROJECT_NAME = "Self-Evolving LOTO6 Prediction AI"

VERSION = "7.0 Ultimate"

AUTHOR = "OpenAI + User"

# =====================================================
# Base Directory
# =====================================================

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"

FEATURE_DIR = BASE_DIR / "feature"

GRAPH_DIR = BASE_DIR / "graph"

MODEL_DIR = BASE_DIR / "models"

TRAIN_DIR = BASE_DIR / "training"

PREDICT_DIR = BASE_DIR / "prediction"

UTIL_DIR = BASE_DIR / "utils"

OUTPUT_DIR = BASE_DIR / "output"

LOG_DIR = BASE_DIR / "logs"

SAVE_MODEL_DIR = BASE_DIR / "saved_models"

# =====================================================
# Automatically create directories
# =====================================================

DIRECTORIES = [

    DATA_DIR,

    FEATURE_DIR,

    GRAPH_DIR,

    MODEL_DIR,

    TRAIN_DIR,

    PREDICT_DIR,

    UTIL_DIR,

    OUTPUT_DIR,

    LOG_DIR,

    SAVE_MODEL_DIR

]

for directory in DIRECTORIES:
    directory.mkdir(parents=True, exist_ok=True)

# =====================================================
# Dataset
# =====================================================

CSV_FILE = DATA_DIR / "l6-v2.csv"

ROUND_COLUMN = "A"

NUMBER_COLUMNS = [

    "L1",

    "L2",

    "L3",

    "L4",

    "L5",

    "L6"

]

BONUS_COLUMN = "B"

LOT_MIN = 1

LOT_MAX = 43

TOTAL_NUMBERS = 6

# =====================================================
# Window Size
# =====================================================

TRAIN_WINDOW = 600

VALID_WINDOW = 100

TEST_WINDOW = 50

SEQUENCE_LENGTH = 20

# =====================================================
# Random Seed
# =====================================================

RANDOM_SEED = 42

random.seed(RANDOM_SEED)

np.random.seed(RANDOM_SEED)

# =====================================================
# GPU
# =====================================================

USE_GPU = True

MIXED_PRECISION = True

# =====================================================
# TensorFlow Settings
# =====================================================

TF_ENABLE_XLA = True

TF_DETERMINISTIC = False

# =====================================================
# PyTorch
# =====================================================

TORCH_DEVICE = "auto"

# =====================================================
# Feature Engineering
# =====================================================

ENABLE_FREQUENCY = True

ENABLE_PAIR = True

ENABLE_TRIPLE = True

ENABLE_GAP = True

ENABLE_CYCLE = True

ENABLE_TREND = True

ENABLE_SUM = True

ENABLE_ODD_EVEN = True

ENABLE_HIGH_LOW = True

ENABLE_VARIANCE = True

ENABLE_STD = True

ENABLE_MARKOV = True

ENABLE_GRAPH = True

ENABLE_DELAY = True

ENABLE_HOT_COLD = True

ENABLE_ENTROPY = True

# =====================================================
# Graph Analysis
# =====================================================

GRAPH_WINDOW = 300

MIN_EDGE_WEIGHT = 2

PAGERANK_ALPHA = 0.85

USE_NODE2VEC = False

# =====================================================
# Logging
# =====================================================

LOG_LEVEL = "INFO"

SAVE_LOG = True

LOG_FILE = LOG_DIR / "training.log"

# =====================================================
# Output
# =====================================================

SAVE_PREDICTION = True

SAVE_BACKTEST = True

SAVE_MODEL = True

SAVE_FEATURE = True

PREDICTION_FILE = OUTPUT_DIR / "prediction.csv"

BACKTEST_FILE = OUTPUT_DIR / "backtest.csv"

FEATURE_FILE = OUTPUT_DIR / "features.csv"

# =====================================================
# Deep Learning Configuration
# =====================================================

TRANSFORMER_CONFIG = {

    "enabled": True,

    "d_model": 256,

    "num_heads": 8,

    "num_layers": 4,

    "dropout": 0.20,

    "ff_dim": 512

}

# =====================================================

BILSTM_CONFIG = {

    "enabled": True,

    "units": [256, 128],

    "dropout": 0.30,

    "recurrent_dropout": 0.20

}

# =====================================================

CNN_CONFIG = {

    "enabled": True,

    "filters": [64, 128, 256],

    "kernel_size": [3, 5, 7],

    "dropout": 0.30

}

# =====================================================
# LightGBM
# =====================================================

LIGHTGBM_CONFIG = {

    "enabled": True,

    "n_estimators": 500,

    "learning_rate": 0.02,

    "num_leaves": 31,

    "max_depth": -1,

    "subsample": 0.90,

    "colsample_bytree": 0.90,

    "random_state": RANDOM_SEED

}

# =====================================================
# XGBoost
# =====================================================

XGBOOST_CONFIG = {

    "enabled": True,

    "n_estimators": 500,

    "learning_rate": 0.03,

    "max_depth": 6,

    "subsample": 0.90,

    "colsample_bytree": 0.90,

    "objective": "reg:squarederror",

    "random_state": RANDOM_SEED

}

# =====================================================
# CatBoost
# =====================================================

CATBOOST_CONFIG = {

    "enabled": True,

    "iterations": 500,

    "learning_rate": 0.03,

    "depth": 8,

    "loss_function": "RMSE",

    "random_seed": RANDOM_SEED,

    "verbose": False

}

# =====================================================
# Training Configuration
# =====================================================

TRAIN_CONFIG = {

    "epochs": 300,

    "batch_size": 32,

    "validation_split": 0.20,

    "shuffle": False,

    "early_stopping": True,

    "patience": 30,

    "reduce_lr": True,

    "reduce_lr_factor": 0.50,

    "reduce_lr_patience": 10,

    "min_learning_rate": 1e-6

}

# =====================================================
# Ensemble
# =====================================================

ENSEMBLE_CONFIG = {

    "transformer_weight": 0.25,

    "bilstm_weight": 0.20,

    "cnn_weight": 0.15,

    "lightgbm_weight": 0.15,

    "xgboost_weight": 0.15,

    "catboost_weight": 0.10

}

# =====================================================
# Hyper Parameter Search
# =====================================================

OPTUNA_CONFIG = {

    "enabled": True,

    "n_trials": 100,

    "timeout": None

}

# =====================================================
# Cross Validation
# =====================================================

CV_CONFIG = {

    "enabled": True,

    "n_splits": 5,

    "shuffle": False

}

# =====================================================
# Prediction Configuration
# =====================================================

PREDICTION_CONFIG = {

    "prediction_count": 20,

    "remove_duplicates": True,

    "sort_output": True,

    "minimum_number": LOT_MIN,

    "maximum_number": LOT_MAX

}

# =====================================================
# Score Weight
# =====================================================

SCORE_WEIGHT = {

    "frequency": 0.10,

    "pair": 0.10,

    "gap": 0.08,

    "cycle": 0.08,

    "trend": 0.10,

    "graph": 0.12,

    "transformer": 0.15,

    "bilstm": 0.10,

    "cnn": 0.07,

    "lightgbm": 0.04,

    "xgboost": 0.03,

    "catboost": 0.03

}

# =====================================================
# Self Learning Configuration
# =====================================================

SELF_LEARNING_CONFIG = {

    "enabled": True,

    "retrain_after_prediction": False,

    "save_prediction_history": True,

    "save_training_history": True,

    "history_file": OUTPUT_DIR / "prediction_history.csv",

    "training_history_file": OUTPUT_DIR / "training_history.csv"

}

# =====================================================
# Backtest Configuration
# =====================================================

BACKTEST_CONFIG = {

    "enabled": True,

    "rolling_window": 100,

    "prediction_window": 20,

    "save_result": True,

    "result_file": OUTPUT_DIR / "backtest_result.csv"

}

# =====================================================
# Model Save Configuration
# =====================================================

MODEL_SAVE_CONFIG = {

    "save_best_only": True,

    "overwrite": True,

    "transformer": SAVE_MODEL_DIR / "transformer.keras",

    "bilstm": SAVE_MODEL_DIR / "bilstm.keras",

    "cnn": SAVE_MODEL_DIR / "cnn.keras",

    "lightgbm": SAVE_MODEL_DIR / "lightgbm.pkl",

    "xgboost": SAVE_MODEL_DIR / "xgboost.pkl",

    "catboost": SAVE_MODEL_DIR / "catboost.pkl"

}

# =====================================================
# Runtime Configuration
# =====================================================

RUNTIME_CONFIG = {

    "use_gpu": USE_GPU,

    "mixed_precision": MIXED_PRECISION,

    "seed": RANDOM_SEED,

    "workers": os.cpu_count(),

    "verbose": 1

}

# =====================================================
# Utility Functions
# =====================================================

def get_number_columns():
    """
    Return lottery number columns.
    """
    return NUMBER_COLUMNS.copy()


def get_csv_path():
    """
    Return CSV file path.
    """
    return CSV_FILE


def get_output_directory():
    """
    Return output directory.
    """
    return OUTPUT_DIR


def get_model_directory():
    """
    Return model save directory.
    """
    return SAVE_MODEL_DIR


def validate_config():
    """
    Validate important settings.
    """
    assert LOT_MIN < LOT_MAX
    assert TOTAL_NUMBERS == len(NUMBER_COLUMNS)
    assert TRAIN_WINDOW > TEST_WINDOW
    assert SEQUENCE_LENGTH > 0


def print_config():
    """
    Display configuration summary.
    """
    print("=" * 60)
    print(PROJECT_NAME)
    print("Version :", VERSION)
    print("=" * 60)
    print("CSV File :", CSV_FILE)
    print("Columns  :", NUMBER_COLUMNS)
    print("GPU      :", USE_GPU)
    print("Output   :", OUTPUT_DIR)
    print("Model    :", SAVE_MODEL_DIR)
    print("=" * 60)


# =====================================================
# Initialize
# =====================================================

validate_config()

if SAVE_LOG:
    print("[INFO] Configuration Loaded Successfully")
