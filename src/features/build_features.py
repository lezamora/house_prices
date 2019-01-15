import pandas as pd


def add_column_house_age(df, column_date, columns_date_build):
    df["house_age"] = df[column_date].dt.year - df[columns_date_build]
    return df


def add_column_renovated(df, column_date_renovated):
    df["renovated"] = df[column_date_renovated].apply(lambda yr: 0 if yr == 0 else 1)
    return df
