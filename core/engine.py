from core.scoring import calculate_score
from core.decision import make_decision

def run_engine(data: dict):
    signals = data.get("signals", [])

    score = calculate_score(signals)
    decision = make_decision(score)

    return {
        "score": score,
        "decision": decision
    }