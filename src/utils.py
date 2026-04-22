import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split

REQUIRED_COLUMNS = ["area", "bedrooms", "age", "price"]

# Function to load data from a csv file
def load_data(path):
    # Load dataset and validate require columns
    if not os.path.exists(path):
        raise FileNotFoundError(f"The data file at {path} was not found.")
    df = pd.read_csv(path)
    missing = set(REQUIRED_COLUMNS) - set(df.columns)
    if missing:
        raise ValueError(f"The following required columns are not in the dataset: {missing}")
    return df

# Function to split data into training and testing sets
def split_data(df, test_size=0.2):
    # Prepare features and target variable
    x = df[["area", "bedrooms", "age"]]
    y = df["price"]
    return train_test_split(x, y, test_size=test_size, random_state=42)

# Function to save the trained model
def save_model(model, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    joblib.dump(model, path)

# Function to load a trained model
def load_model(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"The model file at {path} was not found.")
    return joblib.load(path)