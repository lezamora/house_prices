import os
import pandas as pd


def load_data(data_path, ext_type):
    if ext_type == 'csv':
        return pd.read_csv(data_path)
    else:
        print('Incorrect format.')


def save_data(df, output_data_path, output_df_path):
    dest_path = os.path.join(output_data_path, output_df_path)
    if not os.path.exists(dest_path):
        pd.DataFrame.to_csv(df, dest_path, index_label=False)
