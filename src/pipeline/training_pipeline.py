from src.config.configuration import Configuration
from src.data_ingestion.ingest_data import load_data
from src.preprocessing.feature_engineering import add_rul
from src.models.train_random_forest import train_random_forest


def run_training():

    config = Configuration()

    train_path, test_path, _ = config.get_data_paths()

    train, test = load_data(train_path, test_path)

    train = add_rul(train)

    X = train.drop(["unit_id","cycle","RUL"], axis=1)

    y = train["RUL"]

    model = train_random_forest(X, y)

    return model


if __name__ == "__main__":

    run_training()