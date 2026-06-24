import pickle
import sqlite3
from pathlib import Path

import pandas as pd
from fastapi import FastAPI, Query
from pydantic import BaseModel


MODEL_PATH = Path("/app/models/used_car_price_model.pkl")
DB_PATH = Path("/app/data/db.sqlite")

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
    clean_title: str = "Yes"
    engine_hp: float
    engine_liters: float
    engine_cylinders: float


def get_distinct_values(column_name: str) -> list[str]:
    allowed_columns = {
        "brand",
        "fuel_type",
        "transmission",
        "ext_col",
        "int_col",
        "accident",
    }

    if column_name not in allowed_columns:
        raise ValueError("Column is not allowed")

    query = f"""
        SELECT DISTINCT {column_name}
        FROM tabela_glowna
        WHERE {column_name} IS NOT NULL
        ORDER BY {column_name}
    """

    with sqlite3.connect(DB_PATH) as conn:
        rows = conn.execute(query).fetchall()

    return [row[0] for row in rows if row[0] is not None]


@app.get("/options")
def get_options():
    return {
        "brand": get_distinct_values("brand"),
        "fuel_type": get_distinct_values("fuel_type"),
        "transmission": get_distinct_values("transmission"),
        "ext_col": get_distinct_values("ext_col"),
        "int_col": get_distinct_values("int_col"),
        "accident": get_distinct_values("accident"),
    }


@app.get("/models")
def get_models(brand: str = Query(...)):
    query = """
        SELECT DISTINCT model
        FROM tabela_glowna
        WHERE brand = ?
          AND model IS NOT NULL
        ORDER BY model
    """

    with sqlite3.connect(DB_PATH) as conn:
        rows = conn.execute(query, (brand,)).fetchall()

    return {
        "brand": brand,
        "models": [row[0] for row in rows if row[0] is not None],
    }


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