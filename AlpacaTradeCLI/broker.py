import requests
from config import ALPACA_API_KEY, ALPACA_SECRET_KEY, ALPACA_BASE_URL

SYMBOL = "SPY"
QTY = 10


def _get_headers():
    return {
        "APCA-API-KEY-ID": ALPACA_API_KEY,
        "APCA-API-SECRET-KEY": ALPACA_SECRET_KEY,
        "Content-Type": "application/json"
    }

def go_long():
    """Send market buy for SYMBOL x QTY, return order response dict"""
    url = f"{ALPACA_BASE_URL}/v2/orders"
    payload = {
        "symbol": SYMBOL,
        "qty": QTY,
        "side": "buy",
        "type": "market",
        "time_in_force": "day"
    }
    
    response = requests.post(url, json=payload, headers=_get_headers())
    
    if response.status_code == 200 or response.status_code == 201:
        return response.json()
    else:
        raise Exception(f"HTTP {response.status_code}: {response.text}")

def go_short():
    """Send market sell/short for SYMBOL x QTY, return order response dict"""
    url = f"{ALPACA_BASE_URL}/v2/orders"
    payload = {
        "symbol": SYMBOL,
        "qty": QTY,
        "side": "sell",
        "type": "market",
        "time_in_force": "day"
    }
    
    response = requests.post(url, json=payload, headers=_get_headers())
    
    if response.status_code == 200 or response.status_code == 201:
        return response.json()
    else:
        raise Exception(f"HTTP {response.status_code}: {response.text}")
