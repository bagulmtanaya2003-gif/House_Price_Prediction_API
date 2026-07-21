from fastapi import FastAPI
import pandas as pd
import joblib
from enum import Enum

# Load model and encoder
model = joblib.load("house_price_model.pkl")
encoder = joblib.load("encoder.pkl")

app = FastAPI(title="House Price Prediction API")

# Dropdown for Neighborhood
class Neighborhood(str, Enum):
    Rural = "Rural"
    Suburb = "Suburb"
    Urban = "Urban"

@app.get("/")
def home():
    return {
        "message": "Welcome to House Price Prediction API"
    }

@app.post("/predict")
def predict(
    squarefeet: int,
    bedrooms: int,
    bathrooms: int,
    neighborhood: Neighborhood,
    yearbuilt: int
):

    # Encode Neighborhood
    neighborhood_encoded = encoder.transform([neighborhood.value])[0]

    # Create DataFrame
    data = pd.DataFrame({
        "SquareFeet": [squarefeet],
        "Bedrooms": [bedrooms],
        "Bathrooms": [bathrooms],
        "Neighborhood": [neighborhood_encoded],
        "YearBuilt": [yearbuilt]
    })

    prediction = model.predict(data)

    return {
        "Predicted Price": round(float(prediction[0]), 2)
    }