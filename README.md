## Real-world context

This project is a simplified version of a larger decision engine I’ve been building, designed to demonstrate the architecture, execution flow, and API integration in a safe and reproducible way.

def calculate_score(signals):
    if not signals:
        return 0.0

    weights = [0.2, 0.3, 0.3, 0.2]
    score = sum(s * w for s, w in zip(signals, weights[:len(signals)]))
    return score

    ## Architecture

This project follows a modular backend design with clear separation of concerns:

- API Layer → Handles requests
- Pipeline Layer → Orchestrates execution flow
- Service Layer → Handles computation logic
- Core Layer → Decision logic
- Config Layer → Threshold and system settings

Designed for scalability and integration into larger systems.