import pandas as pd
import logging
from features import build_features
from helpers import hand_data, constans


def __set_index(df, col_index):
    return df.set_index(col_index)


def __drop_columns(df, columns=[]):
    return df.drop(columns=columns)


def __drop_duplicates(df, columns=None):
    return df.drop_duplicates(subset=columns)


def __convert_type(df, dict_var):
    for column, data_type in dict_var.items():
        if data_type == 'int':
            df[column] = df[column].astype(int)
        elif data_type == 'date':
            df[column] = pd.to_datetime(df[column])
    return df


def main(input_file_path, output_file_path):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """

    logger = logging.getLogger(__name__)

    args_convert = {'price': 'int', 'bathrooms': 'int', 'floors': 'int', 'date': 'date'}

    # loading data
    df = hand_data.load_data(input_file_path, 'csv')
    # cleaning data
    df = __set_index(df, 'id')
    df = __drop_duplicates(df)
    df = __convert_type(df, args_convert)
    # feature engineering
    df = build_features.add_column_house_age(df, 'date', 'yr_built')
    df = build_features.add_column_renovated(df, 'yr_renovated')
    df = __drop_columns(df, ['date', 'yr_renovated'])
    # saving data
    hand_data.save_data(df, output_file_path, 'test.csv')

    logger.info('Making final data set from raw data.')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    main(constans.DATA_RAW_PATH, constans.OUTPUT_DATA_PROCESS_PATH)
