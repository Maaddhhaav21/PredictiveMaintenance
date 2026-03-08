# Predictive Maintenance using NASA CMAPSS Dataset

A Machine Learning system that predicts the **Remaining Useful Life (RUL)** of turbofan engines using the NASA **CMAPSS (Commercial Modular Aero-Propulsion System Simulation)** dataset.

This project builds a **complete ML pipeline** including:

- Data ingestion
- Feature engineering
- Model training
- Model evaluation
- REST API deployment with FastAPI
- Interactive dashboard with Streamlit

---

# 📊 Project Overview

Predictive maintenance aims to estimate how long a machine will function before failure.

In this project we use **sensor and operational data from aircraft engines** to predict the **Remaining Useful Life (RUL)**.

The dataset contains multiple simulated engines with degradation patterns captured through **21 sensors and operational settings**.

The trained model predicts how many **cycles remain before engine failure**.

---

# 🧠 Machine Learning Models

The project implements the following models:

- Logistic Regression
- Random Forest Regressor
- LSTM (Deep Learning model)

Currently deployed model:

```
RandomForestRegressor
```

Evaluation metrics used:

- MAE (Mean Absolute Error)
- RMSE (Root Mean Square Error)
- F1-score (for classification experiments)

---

# 📂 Project Structure

```
predictiveMaintenance
│
├── api/
│   └── main.py                  # FastAPI inference server
│
├── dashboard/
│   └── streamlit_app.py         # Streamlit UI for predictions
│
├── data/
│   └── raw/                     # CMAPSS dataset files
│
├── models/
│   └── random_forest.pkl        # Trained model
│
├── notebooks/
│   ├── data_exploration.ipynb
│   └── feature_engineering.ipynb
│
├── src/
│   ├── config/
│   │   └── configuration.py
│   │
│   ├── data_ingestion/
│   │   └── ingest_data.py
│   │
│   ├── preprocessing/
│   │   └── feature_engineering.py
│   │
│   ├── models/
│   │   ├── train_random_forest.py
│   │   └── train_lstm.py
│   │
│   ├── evaluation/
│   │   └── evaluate_model.py
│   │
│   └── pipeline/
│       ├── training_pipeline.py
│       └── prediction_pipeline.py
│
├── tests/
│
├── config.yaml
├── requirements.txt
├── setup.py
└── README.md
```

---

# 📦 Dataset

Dataset used:

**NASA CMAPSS Turbofan Engine Degradation Dataset**

The dataset contains:

- Multiple engines
- Sensor readings over time
- Operational settings
- Failure simulation data

Dataset files:

```
train_FD001.txt
test_FD001.txt
RUL_FD001.txt
```

Features include:

- 3 operational settings
- 21 sensor measurements
- Engine cycles until failure

---

# ⚙️ Installation

Clone the repository:

```
git clone https://github.com/<your-username>/predictiveMaintenance.git
cd predictiveMaintenance
```

Create a virtual environment:

```
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# 🏋️ Training the Model

Run the training pipeline:

```
python -m src.pipeline.training_pipeline
```

This will:

```
Load dataset
↓
Perform feature engineering
↓
Train Random Forest model
↓
Save model → models/random_forest.pkl
```

---

# 🌐 Running the FastAPI Server

Start the API server:

```
python -m uvicorn api.main:app --reload
```

Open API documentation:

```
http://127.0.0.1:8000/docs
```

Example request:

```
{
 "features":[
 0.1,0.2,0.3,0.4,0.5,
 0.6,0.7,0.8,0.9,1.0,
 1.1,1.2,1.3,1.4,1.5,
 1.6,1.7,1.8,1.9,2.0,
 2.1,2.2,2.3,2.4
 ]
}
```

Example response:

```
{
 "Predicted_RUL": 220.95
}
```

---

# 📊 Running the Streamlit Dashboard

Launch the interactive dashboard:

```
streamlit run dashboard/streamlit_app.py
```

Streamlit allows users to:

- Input sensor values
- Run model inference
- Visualize predicted RUL

---

# 🔍 Machine Learning Pipeline

```
Raw Dataset
      ↓
Data Ingestion
      ↓
Feature Engineering
      ↓
Model Training
      ↓
Model Evaluation
      ↓
Model Saving
      ↓
Prediction API
      ↓
Streamlit Dashboard
```

---

# 🛠 Technologies Used

- Python
- Scikit-learn
- TensorFlow / Keras
- Pandas
- NumPy
- FastAPI
- Streamlit
- Joblib

---

# 🎯 Applications

Predictive maintenance systems like this are used in:

- Aerospace engine monitoring
- Industrial equipment maintenance
- Manufacturing predictive analytics
- IoT sensor monitoring systems

---

# 📈 Future Improvements

Possible enhancements:

- XGBoost model
- CNN-LSTM time-series model
- Feature scaling pipeline
- Docker deployment
- CI/CD pipeline
- Real-time streaming sensor data

---

# 👨‍💻 Author

**Madhav Manoj**

## Machine Learning & AI Enthusiast

# ⭐ Acknowledgments

Dataset provided by:

**NASA Prognostics Center of Excellence**

CMAPSS Turbofan Engine Simulation Dataset
