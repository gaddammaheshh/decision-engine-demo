from fastapi import FastAPI
from core.engine import run_engine

app = FastAPI()

@app.post("/analyze")
def analyze(data: dict):
    return run_engine(data)