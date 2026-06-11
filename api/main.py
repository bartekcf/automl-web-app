import pickle
from pathlib import Path

import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel


MODEL_PATH = Path("/app/models/used_car_price_model.pkl")

with open(MODEL_PATH, "rb") as file:
    model_package = pickle.load(file)

pipeline = model_package["pipeline"]
features = model_package["features"]
max_year = model_package["max_year_used_for_car_age"]

app = FastAPI()


class CarInput(BaseModel):
    brand: str
    model: str
    model_year: int
    milage: float
    fuel_type: str
    engine: str
    transmission: str
    ext_col: str
    int_col: str
    accident: str
    clean_title: str
    engine_hp: float
    engine_liters: float
    engine_cylinders: float


@app.post("/predict")
def predict(data: CarInput):
    row = data.model_dump()

    row["car_age"] = max_year - row["model_year"]

    df = pd.DataFrame([row])
    df = df[features]

    prediction = pipeline.predict(df)[0]

    return {
        "predicted_price": round(float(prediction), 2)
    }