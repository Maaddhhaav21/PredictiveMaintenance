import joblib
import numpy as np


class PredictionPipeline:

    def __init__(self):

        self.model = joblib.load("models/random_forest.pkl")

    def predict(self, features):

        features = np.array(features).reshape(1, -1)

        prediction = self.model.predict(features)

        return float(prediction[0])