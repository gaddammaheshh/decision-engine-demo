def calculate_score(signals):
    if not signals:
        return 0.0

    total = sum(signals)
    return total / len(signals)