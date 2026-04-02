def make_decision(score):
    if score > 0.6:
        return "approve"
    elif score > 0.4:
        return "review"
    else:
        return "reject"