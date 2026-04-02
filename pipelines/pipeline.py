class ProcessingPipeline:
    def __init__(self, scorer, decision_fn):
        self.scorer = scorer
        self.decision_fn = decision_fn

    def run(self, signals):
        normalized = self._normalize(signals)
        score = self.scorer.calculate(normalized)
        decision = self.decision_fn(score)

        return {
            "score": score,
            "decision": decision
        }

    def _normalize(self, signals):
        return [min(max(s, 0), 1) for s in signals]


        return {
    "score": score,
    "decision": decision,
    "details": {
        "input": signals,
        "normalized": normalized
    }
}