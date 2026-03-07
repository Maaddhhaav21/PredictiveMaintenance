from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import joblib


def train_random_forest(X, y):

    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(
        n_estimators=200,
        max_depth=15,
        random_state=42
    )

    model.fit(X_train, y_train)

    preds = model.predict(X_val)

    mae = mean_absolute_error(y_val, preds)

    print("MAE:", mae)

    joblib.dump(model, "models/random_forest.pkl")

    return model