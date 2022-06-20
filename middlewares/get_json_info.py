import json

def get_thresholds() -> dict:
    with open("thresholds_stats.json", "r") as f:
        thresholds_meta = json.load(f)
    return thresholds_meta

def set_thresholds(thresholds_data):
    with open("thresholds_stats.json", "w") as f:
        json.dump(thresholds_data, f)

def get_binance_orders_json():
    with open("binance_orders.json") as f:
        binance_orders_json = json.load(f)
    return binance_orders_json

def set_binance_orders_json(binance_orders_data):
    with open("binance_orders.json", "w") as f:
        json.dump(binance_orders_data, f)