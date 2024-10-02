from fastapi import FastAPI
import joblib
import pandas as pd
import numpy as np
from pydantic import BaseModel
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

app = FastAPI()

# Load the saved model
model = joblib.load("models/model.pkl")

# Example: Initialize imputer and scaler (ensure they are the same as used in training)
imputer = SimpleImputer(strategy='mean')
scaler = StandardScaler()

# Define input data structure
class InputData(BaseModel):
    assignment_in_class: float
    assignment_1: float
    assignment_midterm: float

# Define a prediction route
@app.post("/predict")
def predict(data: InputData):
    # Convert input data to a DataFrame
    input_df = pd.DataFrame([{
        'Assignment: In-class participation': data.assignment_in_class,
        'Assignment: Assignment 1': data.assignment_1,
        'Assignment: Midterm': data.assignment_midterm
    }])
    
    # Handle missing values and data preprocessing (just as in your notebook)
    input_df = input_df.replace(['', '-', ' '], np.NaN)
    
    # Convert to numeric values and apply imputation and scaling
    input_df['Assignment: In-class participation'] = pd.to_numeric(input_df['Assignment: In-class participation'], errors='coerce')
    input_df['Assignment: Assignment 1'] = pd.to_numeric(input_df['Assignment: Assignment 1'], errors='coerce')
    input_df['Assignment: Midterm'] = pd.to_numeric(input_df['Assignment: Midterm'], errors='coerce')
    
    # Apply imputer and scaler (ensure they match how they were trained)
    input_df = imputer.transform(input_df)
    input_df = scaler.transform(input_df)
    
    # Convert back to DataFrame for prediction
    input_df = pd.DataFrame(input_df, columns=['Assignment: In-class participation', 'Assignment: Assignment 1', 'Assignment: Midterm'])
    
    # Make prediction
    prediction = model.predict(input_df.values)
    
    return {"prediction": prediction[0]}
