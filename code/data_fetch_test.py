import datetime as dt
import requests
import datetime

# Constant values
dato = datetime.datetime.now().isoformat()
DATO = dato[0:11] + "00:00:00"
TIME = (dt.datetime.now().strftime('%H'))

def fetch() -> dict:
    URL = "https://api.energifyn.dk/api/graph/consumptionprice?date=26-08-2024"
    response = requests.get(URL)
    data = response.json()

    return data

def get(h: int, compas: str, data: dict, date: str):
    if compas == "east":
        print(data['eastPrices'][str(date)]['prices'][h])
        return data['eastPrices'][str(date)]['prices'][h]
    else:
        print(data['westPrices'][str(date)]['prices'][h])
        return data['westPrices'][str(date)]['prices'][h]


data = fetch()
get(int(TIME), "west", data, DATO)
get(int(TIME), "east", data, DATO)
