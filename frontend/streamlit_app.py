import streamlit as st
import requests

API_URL = "http://api:8000/predict"
OPTIONS_URL = "http://api:8000/options"
MODELS_URL = "http://api:8000/models"

st.title("Used Car Price Predictor")

@st.cache_data
def load_options():
    response = requests.get(OPTIONS_URL)
    response.raise_for_status()
    return response.json()

@st.cache_data
def load_models(brand):
    response = requests.get(MODELS_URL, params={"brand": brand})
    response.raise_for_status()
    return response.json()["models"]

options = {}
try:
    options = load_options()
except requests.RequestException as error:
    st.error(f"Could not load options from API: {error}")
    st.stop()


brand = st.selectbox("Brand", options["brand"])
models = load_models(brand)

if not models:
    st.warning(f"No models found for brand: {brand}")
    st.stop()

model = st.selectbox("Model", models)

model_year = st.number_input("Model year", min_value=1980, max_value=2026, value=2018)
milage = st.number_input("Milage", min_value=0.0, value=100000.0)

fuel_type = st.selectbox("Fuel type", options["fuel_type"])
engine = st.text_input("Engine", "2.0L I4")
transmission = st.selectbox("Transmission", options["transmission"])
engine_hp = st.number_input("Engine HP", min_value=0.0, value=150.0)
engine_liters = st.number_input("Engine liters", min_value=0.0, value=2.0)
engine_cylinders = st.number_input("Engine cylinders", min_value=0.0, value=4.0)


ext_col = st.selectbox("Exterior color", options["ext_col"])
int_col = st.selectbox("Interior color", options["int_col"])

accident = st.selectbox("Accident", options["accident"])

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
        "engine_hp": float(engine_hp),
        "engine_liters": float(engine_liters),
        "engine_cylinders": float(engine_cylinders),
    }

    response = requests.post(API_URL, json=payload)

    if response.ok:
        result = response.json()
        st.success(f"Predicted price: ${result['predicted_price']:,.2f}")
    else:
        st.error(response.text)