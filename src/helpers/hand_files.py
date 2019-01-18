import os
import pandas as pd
import joblib
import datetime


now_time = datetime.datetime.now()
now_time = now_time.strftime("%Y_%m_%d__%H_%M")


def load_data(data_path, ext_type):
    if os.path.exists(data_path):
        if ext_type == 'csv':
            return pd.read_csv(data_path)
        else:
            print('Incorrect format.')


def save_data(df, data_path):
    if not os.path.exists(data_path):
        pd.DataFrame.to_csv(df, data_path, index_label=False)


def load_trained_model(model_path):
    if os.path.exists(model_path):
        loaded_model = joblib.load(model_path)
    else:
        loaded_model = None
    return loaded_model


def save_trained_model(model, model_path, name):
    model_path = os.path.join(model_path, '{}{}.joblib'.format(name, now_time))
    if not os.path.exists(model_path):
        joblib.dump(model, model_path)
