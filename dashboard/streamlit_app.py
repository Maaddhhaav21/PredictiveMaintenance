import streamlit as st
import joblib
import numpy as np


model = joblib.load("models/random_forest.pkl")

st.title("Predictive Maintenance - RUL Prediction")

features = st.text_input("Enter sensor values separated by comma")

if st.button("Predict"):

    values = np.array([float(x) for x in features.split(",")]).reshape(1,-1)

    prediction = model.predict(values)

    st.success(f"Predicted RUL: {prediction[0]}")