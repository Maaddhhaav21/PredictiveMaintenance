from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib
import traceback

app = FastAPI()

model = joblib.load("models/random_forest.pkl")


class Features(BaseModel):
    features: list[float]


@app.get("/")
def home():
    return {"message": "Predictive Maintenance API running"}


@app.post("/predict")
def predict(data: Features):

    try:
        features = np.array(data.features).reshape(1, -1)

        prediction = model.predict(features)

        return {"Predicted_RUL": float(prediction[0])}

    except Exception as e:
        print("\n ERROR OCCURRED:")
        traceback.print_exc()
        return {"error": str(e)}