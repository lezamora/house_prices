import os
from pathlib import Path
import numpy as np
import scipy.stats as st

ROOT_PATH = Path(__file__).resolve().parents[2]
DATA_PATH = os.path.join(ROOT_PATH, 'data')
DATA_RAW_PATH = os.path.join(DATA_PATH, 'raw')
OUTPUT_DATA_PROCESS_PATH = os.path.join(DATA_PATH, 'processed')
OUTPUT_PATH = os.path.join(ROOT_PATH, 'reports')
OUTPUT_REF_PATH = os.path.join(ROOT_PATH, 'references')
OUTPUT_MODEL_PATH = os.path.join(ROOT_PATH, 'models')
OUTPUT_REPORT_PATH = os.path.join(ROOT_PATH, 'reports')
OUTPUT_FIGURE_PATH = os.path.join(OUTPUT_REPORT_PATH, 'figures')

one_to_left = st.beta(10, 1)

GRID_PARAMS = {
    "n_estimators": np.array([100, 200, 300, 400, 500, 600]),  # Number of boosted trees to fit.
    "max_depth": st.randint(3, 12),  # Maximum tree depth for base learners.
    "learning_rate": st.uniform(0.05, 0.4),  # Boosting learning rate (xgb’s “eta”)
    "subsample": one_to_left  # Subsample ratio of the training instance.
}

TARGET = 'price'

