import os
import pandas as pd

def load_data(data_path, ext_type):
    if ext_type == 'CSV':
        dataframe = pd.read_csv(data_path)
    else:
        print('Formato incorrecto')
    return dataframe

def save_data(dataframe, output_data_path, output_df_path):
    dest_path = os.path.join(output_data_path, output_df_path)
    if not os.path.exists(dest_path):
        pd.DataFrame.to_csv(dataframe, dest_path, index_label=False)