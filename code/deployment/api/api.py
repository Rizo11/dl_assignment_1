from fastapi import FastAPI
import joblib
import pandas as pd
import numpy as np
from pydantic import BaseModel

app = FastAPI()

# Load the saved model
model = joblib.load("models/model.pkl")

# Min-Max Scaling function for new data
def min_max_scale(a, b, c):
    min_a = 0
    max_a = 5
    min_b = 0
    max_b = 100
    min_c = 0
    max_c = 30
    return (a - min_a) / (max_a - min_a), (b - min_b) / (max_b - min_b), (c - min_c) / (max_c - min_c)

def unscale(scaled_value):
        max_val = 100
        min_val = 0
        return scaled_value * (max_val - min_val) + min_val

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
    
    print("=============================================")
    print(data.assignment_1)
    print(data.assignment_in_class)
    print(data.assignment_midterm)
    # Convert to numeric values and apply imputation and scaling
    input_df['Assignment: In-class participation'] = pd.to_numeric(input_df['Assignment: In-class participation'], errors='coerce')
    input_df['Assignment: Assignment 1'] = pd.to_numeric(input_df['Assignment: Assignment 1'], errors='coerce')
    input_df['Assignment: Midterm'] = pd.to_numeric(input_df['Assignment: Midterm'], errors='coerce')
    
    # Convert back to DataFrame for prediction
    input_df = pd.DataFrame(input_df, columns=['Assignment: In-class participation', 'Assignment: Assignment 1', 'Assignment: Midterm'])
    
    print(type(input_df), "-===================")
    a, b, c = min_max_scale(input_df['Assignment: In-class participation'],
                            input_df['Assignment: Assignment 1'],
                            input_df['Assignment: Midterm'])
    input_df['Assignment: In-class participation'] = a
    input_df['Assignment: Assignment 1'] = b
    input_df['Assignment: Midterm'] = c

    print(a, b, c)

    # Make prediction
    prediction = model.predict(input_df.values)


    # To revert back to original values
    prediction = unscale(prediction)
    
    return {"prediction": prediction[0]}
