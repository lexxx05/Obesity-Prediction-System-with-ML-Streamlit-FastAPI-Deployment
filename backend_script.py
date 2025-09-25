from fastapi import FastAPI
import pickle
import pandas as pd
from pydantic import BaseModel
from custom_transformer_2 import CleanAgeTransformer
import category_encoders as ce

with open("best_pipeline_3.pkl", "rb") as f:
  model = pickle.load(f)

app = FastAPI()

class InputData(BaseModel):
    Gender: str
    Age: float
    Height: float
    Weight: float
    family_history_with_overweight: str
    FAVC: str
    FCVC: float
    NCP: float
    CAEC: str
    SMOKE: str
    CH2O: float
    SCC: str
    FAF: float
    TUE: float
    CALC: str
    MTRANS: str

label_map = {
    0: "Insufficient Weight",
    1: "Normal Weight",
    2: "Overweight Level I",
    3: "Overweight Level II",
    4: "Obesity Type I",
    5: "Obesity Type II",
    6: "Obesity Type III"
}

@app.get("/api-endpoint")

def read_root():
  return {"message" : "Welcome to Obesity Model API!"}

@app.post("/predict")

def predict(data: InputData):
  dfInput = pd.DataFrame([data.dict()])
  prediction = model.predict(dfInput)[0]
  prediction_labelled = label_map.get(prediction, "Unknown")
  return prediction_labelled
