import pandas as pd


def add_rul(df):

    max_cycle = df.groupby("unit_id")["cycle"].max()

    df = df.merge(
        max_cycle.to_frame(name="max_cycle"),
        left_on="unit_id",
        right_index=True
    )

    df["RUL"] = df["max_cycle"] - df["cycle"]

    df.drop("max_cycle", axis=1, inplace=True)

    return df
