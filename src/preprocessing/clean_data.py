import pandas as pd


def remove_constant_sensors(df):

    cols_to_drop = [col for col in df.columns if df[col].std() == 0]

    df = df.drop(columns=cols_to_drop)

    return df