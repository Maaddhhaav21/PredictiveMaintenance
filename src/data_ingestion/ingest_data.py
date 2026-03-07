import pandas as pd


def load_data(train_path, test_path):

    columns = ['unit_id','cycle','op1','op2','op3'] + \
              [f'sensor_{i}' for i in range(1,22)]

    train = pd.read_csv(train_path, sep="\s+", header=None)
    test = pd.read_csv(test_path, sep="\s+", header=None)

    train = train.iloc[:, :26]
    test = test.iloc[:, :26]

    train.columns = columns
    test.columns = columns

    return train, test