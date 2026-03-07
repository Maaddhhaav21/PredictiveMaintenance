from fastapi import FastAPI
from src.pipeline.prediction_pipeline import PredictionPipeline


app = FastAPI()

pipeline = PredictionPipeline()


@app.get("/")
def home():

    return {"message": "Predictive Maintenance API"}


@app.post("/predict")
def predict(features: list):

    prediction = pipeline.predict(features)

    return {"Predicted_RUL": prediction}