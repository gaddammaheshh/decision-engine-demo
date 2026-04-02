class ScoringService:
    def calculate(self, signals):
        if not signals:
            return 0.0
        return sum(signals) / len(signals)