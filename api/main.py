import pickle
from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel

MODEL_PATH = Path("/app/models/used_car_price_model.pkl")

with open(MODEL_PATH, "rb") as file:
    model_package = pickle.load(file)

pipeline = model_package["pipeline"]
features = model_package["features"]

app = FastAPI()


class CarInput(BaseModel):
    year: int
    mileage: float
    engine_capacity: float
    fuel_type: str
    transmission: str
    brand: str
    model: str


@app.post("/predict")
def predict(data: CarInput):
    import pandas as pd

    row = data.model_dump()
    df = pd.DataFrame([row])

    df = df[features]

    prediction = pipeline.predict(df)[0]

    return {
        "predicted_price": round(float(prediction), 2)
    }