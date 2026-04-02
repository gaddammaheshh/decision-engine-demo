from fastapi import FastAPI
from core.engine import run_engine

app = FastAPI()

@app.post("/analyze")
def analyze(data: dict):
    return run_engine(data)

    from models.schema import InputSchema

@app.post("/analyze")
def analyze(data: InputSchema):
    return run_engine(data.dict())

    weights = [0.2, 0.3, 0.3, 0.2]
score = sum(s * w for s, w in zip(signals, weights))