
# Decision Engine Demo

A deterministic backend system that processes structured inputs into actionable outputs using a modular scoring pipeline.

## Features
- Input → scoring → decision pipeline
- Deterministic outputs
- API-ready (FastAPI)

## Run Locally

```bash
pip install -r requirements.txt
uvicorn api.main:app --reload