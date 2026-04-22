import pandas as pd
import joblib
from sklearn.metrics import r2_score
import os

MODEL_PATH = "models/model.pkl"
DATA_PATH = "data/housing.csv"

def evaluate_model():
    # Load dataset
    df = pd.read_csv(DATA_PATH)

    # Prepare features and target variable
    x = df[["area", "bedrooms", "age"]]
    y = df["price"]

    # Load the trained model
    model = joblib.load(MODEL_PATH)
    preds = model.predict(x)

    # Calculate R^2 score
    score = r2_score(y, preds)
    print(f"R^2 Score of the model: {score:.4f}")

    # Check if the score meets the threshold
    if score < 0.8:
        raise ValueError("MODEL ACCURACY NOT CORRECT")
    print("MODEL ACCURACY IS CORRECT")

if __name__ == "__main__":
    evaluate_model()