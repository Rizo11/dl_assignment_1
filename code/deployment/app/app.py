import streamlit as st
import requests


# Streamlit app title
st.title('Assignment Grade Prediction App')

# Input fields for user to enter data
assignment_in_class = st.number_input('Assignment: In-class participation', min_value=0.0, max_value=100.0)
assignment_1 = st.number_input('Assignment: Assignment 1', min_value=0.0, max_value=100.0)
assignment_midterm = st.number_input('Assignment: Midterm', min_value=0.0, max_value=100.0)

# Button to make prediction
if st.button('Predict Grade'):
    # Create input data in the required format for FastAPI
    input_data = {
        'assignment_in_class': assignment_in_class,
        'assignment_1': assignment_1,
        'assignment_midterm': assignment_midterm
    }

    # Send a request to FastAPI (make sure FastAPI is running and accessible)
    api_url = 'http://backend:8001/predict'  # Replace 'api' with the appropriate container name in Docker
    response = requests.post(api_url, json=input_data)
    
    # Process the response and display the prediction
    if response.status_code == 200:
        prediction = response.json().get('prediction')
        st.success(f'Predicted Course Grade: {prediction}')
    else:
        st.error('Error occurred while making the prediction')
