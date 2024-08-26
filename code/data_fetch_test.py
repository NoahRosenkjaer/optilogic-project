import requests
import datetime
import datetime as dt

def get(h: int, compas: str, data: dict) -> dict:
    dato = datetime.datetime.now().isoformat()
    dato = dato[0:11] + "00:00:00"
    if compas == "east":
        return data['eastPrices'][str(dato)]['prices'][h]
    else:
        return data['westPrices'][str(dato)]['prices'][h]
    

def fetch():
    URL = "https://api.energifyn.dk/api/graph/consumptionprice?date=26-08-2024"
    timenr = (dt.datetime.now().strftime('%H'))
    response = requests.get(URL)
    data = response.json()
    print(get(int(timenr), "west", data))
    print(get(int(timenr), "east", data))
    print(response)
    
fetch()
