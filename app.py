from fastapi import FastAPI
import pickle
import pandas as pd

app = FastAPI()

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def home():
    return {"message": "Adult Income Prediction API"}

@app.post("/predict")
def predict(
    age: int,
    workclass: str,
    education: str,
    educational_num: int,
    marital_status: str,
    occupation: str,
    relationship: str,
    race: str,
    gender: str,
    capital_gain: int,
    capital_loss: int,
    hours_per_week: int
):
    
    data = pd.DataFrame([{
        "age": age,
        "workclass": workclass,
        "education": education,
        "educational_num": educational_num,
        "marital_status": marital_status,
        "occupation": occupation,
        "relationship": relationship,
        "race": race,
        "gender": gender,
        "capital_gain": capital_gain,
        "capital_loss": capital_loss,
        "hours_per_week": hours_per_week
        
    }])

    prediction = model.predict(data)[0]

    label = "<=50K" if prediction[0] == 0 else ">50K"

    return {"prediction": label}
