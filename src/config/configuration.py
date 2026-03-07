import yaml


class Configuration:

    def __init__(self, config_path="config.yaml"):

        with open(config_path, "r") as file:
            self.config = yaml.safe_load(file)

    def get_data_paths(self):

        return (
            self.config["data"]["train_file"],
            self.config["data"]["test_file"],
            self.config["data"]["rul_file"],
        )

    def get_model_config(self):

        return self.config["model"]

    def get_training_config(self):

        return self.config["training"]