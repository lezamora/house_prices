import sys
sys.path.insert(0, './src')
print()
import os
import pandas as pd
import logging
from helpers import hand_files, constans


def __set_index(df, col_index):
    return df.set_index(col_index)


def __drop_columns(df, columns=[]):
    return df.drop(columns=columns)


def __drop_duplicates(df, columns=None):
    return df.drop_duplicates(subset=columns)


def __convert_type(df, dict_var):
    """ Funcion para poder corregir el tipo de datos de nuestros features.

    :param df: es el dataframe sobre el que estamos trabajando.
    :param dict_var: son las columnas con los tipos de datos a los que queremos convertir.
    :return: retorna el dataframe con las columnas con los tipos de datos correctos.
    """

    for column, data_type in dict_var.items():
        if data_type == 'int':
            df[column] = df[column].astype(int)
        elif data_type == 'date':
            df[column] = pd.to_datetime(df[column])
    return df


def __add_column_house_age(df, column_date, columns_date_build):
    """ Esta función agrega una columna donde guardaremos
    la antiguedad de cada cada.
    """

    df["house_age"] = df[column_date].dt.year - df[columns_date_build]
    return df


def __add_column_renovated(df, column_date_renovated):
    """ Con esta función agregamos una columna que indica si nuestra casa
    ha sido renovado o no. Una casa está renovada si la columna date_renovated
    está ingresada.
    """

    df["renovated"] = df[column_date_renovated].apply(lambda yr: 0 if yr == 0 else 1)
    return df


def main(input_file_name, output_file_name):
    """ Script para transformar nuestros datos en bruto (load in ../raw) en
        datos limpios para ser utilizados. (saved in ../processed).
    """

    logger = logging.getLogger(__name__)

    args_convert = {'price': 'int', 'bathrooms': 'int', 'floors': 'int', 'date': 'date'}

    # loading data
    logger.info('Loading raw data.')
    df = hand_files.load_data(input_file_name, 'csv')

    # cleaning data and feature engineering
    logger.info('Cleaning data.')
    df = __set_index(df, 'id')
    df = __drop_duplicates(df)
    df = __convert_type(df, args_convert)
    df = __add_column_house_age(df, 'date', 'yr_built')
    df = __add_column_renovated(df, 'yr_renovated')
    df = __drop_columns(df, ['date', 'yr_renovated'])

    # saving data
    hand_files.save_data(df, output_file_name)
    logger.info('Data limpia y guardada en {}.'.format(output_file_name))


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    raw_data_path = os.path.join(constans.DATA_RAW_PATH, 'kc_house_data.csv')
    processed_data_path = os.path.join(constans.OUTPUT_DATA_PROCESS_PATH, 'kc_house_data_clean_with_outliers.csv')
    print(raw_data_path)
    main(raw_data_path, processed_data_path)
