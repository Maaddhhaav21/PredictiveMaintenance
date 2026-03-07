from fastapi import FastAPI
import joblib
import numpy as np


app = FastAPI()

model = joblib.load("models/random_forest.pkl")


@app.get("/")
def home():

    return {"message": "Predictive Maintenance API"}


@app.post("/predict")
def predict(features: list):

    features = np.array(features).reshape(1, -1)

    prediction = model.predict(features)

    return {"Predicted_RUL": float(prediction[0])}