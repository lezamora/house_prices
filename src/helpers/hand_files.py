import os
import pandas as pd
import pickle
from helpers import constans


def load_data(file_name, ext_type):
    data_path = os.path.join(constans.DATA_RAW_PATH, file_name)
    print(data_path)
    if os.path.exists(data_path):
        if ext_type == 'csv':
            return pd.read_csv(data_path)
        else:
            print('Incorrect format.')


def save_data(df, file_name):
    data_path = os.path.join(constans.OUTPUT_DATA_PROCESS_PATH, file_name)
    if not os.path.exists(data_path):
        pd.DataFrame.to_csv(df, data_path, index_label=False)


def load_trained_model(model):
    model_path = os.path.join(constans.OUTPUT_MODEL_PATH, model)
    if os.path.exists(model_path):
        with open(model_path, 'wb') as f:
            loaded_model = pickle.load(f)
    else:
        loaded_model = None
    return loaded_model


def save_trained_model(model):
    model_path = os.path.join(constans.OUTPUT_MODEL_PATH, model + '.pickle')
    if not os.path.exists(model_path):
        with open(model_path, 'wb') as f:
            pickle.dump(model, f)
