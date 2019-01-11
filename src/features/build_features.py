import pandas as pd

def add_column_house_age(dataframe, column_date, columns_date_build):
    dataframe["house_age"] = dataframe["date"].dt.year - dataframe['yr_built']
    return dataframe

def add_column_renovated(dataframe, column_date_renovated):
    dataframe["renovated"] = dataframe[column_date_renovated].apply(lambda yr: 0 if yr == 0 else 1)
    return dataframe