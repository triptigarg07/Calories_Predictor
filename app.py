import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("calories_regressor.pkl")

# Streamlit UI
st.title("Calories Prediction App 🍽️")
st.write("Enter the required details to predict the calories burned.")

# Input fields for the user
duration = st.number_input("Exercise Duration (minutes)", min_value=1, max_value=180, value=60)
pulse = st.number_input("Pulse (bpm)", min_value=60, max_value=200, value=110)
maxpulse = st.number_input("Max Pulse (bpm)", min_value=80, max_value=220, value=130)

# Convert input to numpy array (Ensure correct order as per model training)
features = np.array([[duration, pulse, maxpulse]])

if st.button("Predict Calories"):
    prediction = model.predict(features)
    st.success(f"Estimated Calories Burned: {prediction[0]:.2f}")