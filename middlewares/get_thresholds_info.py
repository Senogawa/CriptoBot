import json

def get_thresholds() -> dict:
    with open("thresholds_stats.json", "r") as f:
        thresholds_meta = json.load(f)
    return thresholds_meta
