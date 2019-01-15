import os
from pathlib import Path

ROOT_PATH = Path(__file__).resolve().parents[2]
DATA_PATH = os.path.join(ROOT_PATH, 'data')
DATA_RAW_PATH = os.path.join(DATA_PATH, 'raw')
OUTPUT_DATA_PROCESS_PATH = os.path.join(DATA_PATH, 'processed')
OUTPUT_PATH = os.path.join(ROOT_PATH, 'reports')
OUTPUT_REF_PATH = os.path.join(ROOT_PATH, 'references')
OUTPUT_MODEL_PATH = os.path.join(ROOT_PATH, 'models')
