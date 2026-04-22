from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib
import os

app = Flask(__name__)

# Path to the model
MODEL_PATH = "models/model.pkl"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Load the trained model
        if not os.path.exists(MODEL_PATH):
            return jsonify({"error": "Model file not found. Please train the model first."}), 404
        
        model = joblib.load(MODEL_PATH)
        
        # Get data from the request
        data = request.json
        area = float(data.get("area", 0))
        bedrooms = int(data.get("bedrooms", 0))
        age = int(data.get("age", 0))
        
        # Validate inputs
        if area <= 0 or bedrooms <= 0 or age < 0:
            return jsonify({"error": "Invalid input values. Area and bedrooms must be > 0, age must be >= 0."}), 400

        # Create a dataframe for the model
        input_data = pd.DataFrame([[area, bedrooms, age]], columns=["area", "bedrooms", "age"])
        
        # Predict the price
        prediction = model.predict(input_data)[0]
        
        return jsonify({"price": round(prediction, 2)})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
