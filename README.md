# Decision Engine Demo

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB.svg)](https://www.python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688.svg)](https://fastapi.tiangolo.com)
[![Pydantic](https://img.shields.io/badge/Pydantic-v2-FF6F00.svg)](https://docs.pydantic.dev)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A clean, modular, and extensible backend system that transforms structured inputs into **deterministic, auditable, and explainable decisions** using a pipeline-driven architecture.

This public repository is a **simplified demonstration** of core architectural patterns and engineering best practices from a larger private decision engine project. It focuses on showcasing professional backend development skills while keeping all proprietary logic, rules, and domain knowledge confidential.

## Overview

Decision systems often need to process complex structured data, apply configurable rules, and deliver consistent, transparent results. This demo implements a lightweight but realistic version of such a system with strong emphasis on:

- **Determinism** — Same input always produces the same output
- **Modularity & Extensibility** — Easy to add, modify, or remove processing steps
- **Explainability** — Clear reasoning behind every decision
- **Robust Validation** — Strong input validation and meaningful error responses
- **Clean Architecture** — Clear separation between API, services, core logic, and pipelines

## Key Features

- Configurable **pipeline orchestration** with independent, reusable steps
- FastAPI backend with automatic interactive Swagger/OpenAPI documentation
- Robust request/response models using **Pydantic v2**
- Pure, deterministic core logic for high testability
- Built-in explainability that returns factor-level contributions
- Health check and readiness endpoints
- Clean dependency injection and configuration management
- Well-structured, documented, and production-aware codebase

## Architecture

```mermaid
flowchart TD
    A[Client Request] --> B[API Layer\n(Routes + Schemas)]
    B --> C[Input Validation]
    C --> D[Pipeline Orchestrator]
    D --> E[Services Layer]
    E --> F[Core Decision Logic]
    F --> G[Explainability Engine]
    G --> H[Response Assembly]
    H --> I[JSON Response\nwith Explanation]
    
    style F fill:#e3f2fd,stroke:#1976d2



Design Principles:

Core logic is kept pure and side-effect free
Services handle domain rules while remaining decoupled from pipelines and API
Pipeline steps are independent and easily extensible
API layer focuses only on HTTP concerns (routing, validation, responses)

Project Structure

decision-engine-demo/
├── api/              # FastAPI routes, dependencies, and Pydantic schemas
├── core/             # Pure deterministic decision logic (highly testable)
├── pipelines/        # Pipeline definitions and step orchestration
├── services/         # Domain-specific services and rules
├── models/           # Internal data models and DTOs
├── config/           # Configuration and settings management
├── utils/            # Shared utilities and helper functions
├── data/             # Sample inputs for testing and demonstration
├── tests/            # Unit and integration tests
├── .gitignore
├── requirements.txt
└── README.md

Quick Start
# 1. Clone the repository
git clone https://github.com/gaddammaheshh/decision-engine-demo.git
cd decision-engine-demo

# 2. Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate          # Windows users: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the development server
uvicorn api.main:app --reload --port 8000


Open your browser and navigate to:
http://localhost:8000/docs — Interactive Swagger UI
API Usage Example
Main Endpoint
POST /decide
Request Body:

{
  "features": {
    "revenue": 1250000,
    "expenses": 890000,
    "cash_balance": 450000,
    "debt_ratio": 0.35,
    "growth_rate": 0.18,
    "customer_count": 420
  },
  "context": {
    "sector": "technology",
    "stage": "growth",
    "region": "APAC"
  }
}

{
  "decision": "APPROVED",
  "score": 78.4,
  "threshold": 65.0,
  "explanation": [
    {
      "factor": "revenue",
      "contribution": 24.5,
      "weight": 0.30,
      "description": "Strong revenue generation"
    },
    {
      "factor": "debt_ratio",
      "contribution": -9.2,
      "weight": 0.25,
      "description": "Moderate leverage"
    }
  ],
  "metadata": {
    "processing_time_ms": 14,
    "pipeline_steps_executed": 6
  }
}


What This Demonstrates
This project highlights key software engineering competencies valued in professional roles:

Designing and implementing clean, layered, modular architecture
Building extensible pipeline-based systems
Writing deterministic and highly testable core logic
Implementing production-grade validation and error handling
Adding explainability to decision-making systems
Maintaining clear separation of concerns for long-term maintainability
Creating well-documented, easy-to-run projects

These skills are directly transferable to domains such as fintech, risk engines, eligibility systems, workflow automation, and configurable business platforms.


# Run tests with coverage report
pytest tests/ -v --cov=. --cov-report=term-missing


Live Demo
The app can be deployed easily on free platforms like Render or Railway.
Once deployed, update this section with your actual URL (usually ends with .onrender.com/docs).
Future Enhancements (Planned Ideas)

Docker containerization
GitHub Actions CI/CD pipeline
Async support for heavier workloads
Advanced explainability features
Database integration examples

License
This project is licensed under the MIT License.
text


This version should now render the Mermaid diagram correctly on GitHub.

**Next recommendation:**  
Deploy the app on **Render** (free tier is sufficient). It’s the quickest way to have a working "Live Demo" link. If you want, reply with “deploy guide” and I’ll give you the exact step-by-step instructions for Render (including the correct start command).

Let me know if you want any other small tweaks (e.g., change the endpoint name to your actual one, update sample JSON, or shorten any section).
