import os
from src.train import train_model

def test_model_creation():
    # Ensure the model is created after training
    train_model()
    assert os.path.exists("models/model.pkl")
    