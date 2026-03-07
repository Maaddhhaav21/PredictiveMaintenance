from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
import joblib


def train_logistic_regression(X, y):

    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LogisticRegression(max_iter=500)

    model.fit(X_train, y_train)

    preds = model.predict(X_val)

    score = f1_score(y_val, preds, average="macro")

    print("F1 Score:", score)

    joblib.dump(model, "models/logistic_regression.pkl")

    return model