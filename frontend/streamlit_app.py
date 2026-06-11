import streamlit as st
import requests

API_URL = "http://api:8000/predict"

st.title("Used Car Price Predictor")

brand = st.text_input("Brand", "Toyota")
model = st.text_input("Model", "Corolla")

model_year = st.number_input("Model year", min_value=1980, max_value=2026, value=2018)
milage = st.number_input("Milage", min_value=0.0, value=100000.0)

fuel_type = st.text_input("Fuel type", "Gasoline")
engine = st.text_input("Engine", "2.0L I4")
transmission = st.text_input("Transmission", "Automatic")

ext_col = st.text_input("Exterior color", "White")
int_col = st.text_input("Interior color", "Black")

accident = st.selectbox("Accident", ["None reported", "At least 1 accident or damage reported"])
clean_title = st.selectbox("Clean title", ["Yes", "No"])

engine_hp = st.number_input("Engine HP", min_value=0.0, value=150.0)
engine_liters = st.number_input("Engine liters", min_value=0.0, value=2.0)
engine_cylinders = st.number_input("Engine cylinders", min_value=0.0, value=4.0)

if st.button("Predict"):
    payload = {
        "brand": brand,
        "model": model,
        "model_year": int(model_year),
        "milage": float(milage),
        "fuel_type": fuel_type,
        "engine": engine,
        "transmission": transmission,
        "ext_col": ext_col,
        "int_col": int_col,
        "accident": accident,
        "clean_title": clean_title,
        "engine_hp": float(engine_hp),
        "engine_liters": float(engine_liters),
        "engine_cylinders": float(engine_cylinders),
    }

    response = requests.post(API_URL, json=payload)

    if response.ok:
        result = response.json()
        st.success(f"Predicted price: {result['predicted_price']}")
    else:
        st.error(response.text)