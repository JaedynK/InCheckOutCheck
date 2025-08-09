from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="InCheckOutCheck API")

class PredictRequest(BaseModel):
    features: list[float]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(req: PredictRequest):
    score = sum(req.features) / max(1, len(req.features))
    return {"prediction": 1 if score > 0.5 else 0, "score": score}