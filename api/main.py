
from fastapi import FastAPI
from pydantic import BaseModel
from pipeline.modeling.trained_model import QwenModel


app = FastAPI(title="InCheckOutCheck API")


class PredictRequest(BaseModel):
    features: list[float]

class GenerateRequest(BaseModel):
    prompt: str
    max_length: int = 50

qwen_model = QwenModel()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(req: PredictRequest):
    score = sum(req.features) / max(1, len(req.features))
    return {"prediction": 1 if score > 0.5 else 0, "score": score}

@app.post("/generate")
def generate(req: GenerateRequest):
    result = qwen_model.generate(req.prompt, max_length=req.max_length)
    return {"result": result}