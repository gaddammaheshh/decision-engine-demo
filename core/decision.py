from config.settings import Settings

def make_decision(score):
    if score >= Settings.THRESHOLDS["approve"]:
        return "approve"
    elif score >= Settings.THRESHOLDS["review"]:
        return "review"
    return "reject"