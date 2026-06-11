import streamlit as st
import requests

API_URL = "http://api:8000/predict"

st.title("Used Car Price Predictor")

year = st.number_input("Year", min_value=1980, max_value=2026, value=2018)
mileage = st.number_input("Mileage", min_value=0.0, value=100000.0)
engine_capacity = st.number_input("Engine capacity", min_value=0.0, value=2.0)

fuel_type = st.text_input("Fuel type", "Petrol")
transmission = st.text_input("Transmission", "Manual")
brand = st.text_input("Brand", "Toyota")
model = st.text_input("Model", "Corolla")

if st.button("Predict"):
    payload = {
        "year": year,
        "mileage": mileage,
        "engine_capacity": engine_capacity,
        "fuel_type": fuel_type,
        "transmission": transmission,
        "brand": brand,
        "model": model,
    }

    response = requests.post(API_URL, json=payload)

    if response.ok:
        result = response.json()
        st.success(f"Predicted price: {result['predicted_price']}")
    else:
        st.error(response.text)