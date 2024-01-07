import streamlit as st
import pickle
import pandas as pd

# Load the model (replace with the actual path to your saved model)
model = pickle.load(open("xgb_model.pkl", "rb"))

# Set app title and layout
st.set_page_config(page_title="Wind Energy Prediction App", layout="wide")

# Create sidebar for input features
st.sidebar.header("Enter Weather Conditions:")

temperature_2m = st.sidebar.number_input("Temperature (2m)", value=15.0, min_value=-50.0, max_value=50.0)
relativehumidity_2m = st.sidebar.number_input("Relative Humidity (2m)", value=50.0, min_value=0.0, max_value=100.0)
dewpoint_2m = st.sidebar.number_input("Dew Point (2m)", value=10.0, min_value=-50.0, max_value=50.0)
windspeed_10m = st.sidebar.number_input("Wind Speed (10m)", value=5.0, min_value=0.0)
windspeed_100m = st.sidebar.number_input("Wind Speed (100m)", value=10.0, min_value=0.0)
winddirection_10m = st.sidebar.number_input("Wind Direction (10m)", value=270.0, min_value=0.0, max_value=360.0)
winddirection_100m = st.sidebar.number_input("Wind Direction (100m)", value=270.0, min_value=0.0, max_value=360.0)
windgusts_10m = st.sidebar.number_input("Wind Gusts (10m)", value=10.0, min_value=0.0)

# Create a DataFrame with input features
df = pd.DataFrame({
    "temperature_2m": [temperature_2m],
    "relativehumidity_2m": [relativehumidity_2m],
    "dewpoint_2m": [dewpoint_2m],
    "windspeed_10m": [windspeed_10m],
    "windspeed_100m": [windspeed_100m],
    "winddirection_10m": [winddirection_10m],
    "winddirection_100m": [winddirection_100m],
    "windgusts_10m": [windgusts_10m]
})

# Make prediction when button is clicked
if st.sidebar.button("Predict Power"):
    prediction = model.predict(df)[0]
    st.header("Predicted Power Generation:")
    st.subheader(f"{prediction:.2f} MW")  # Display prediction with 2 decimal places