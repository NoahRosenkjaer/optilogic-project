import requests
import datetime as dt

URL = "https://api.energifyn.dk/api/graph/consumptionprice?date=26-08-2024"
timenr = (dt.datetime.now().strftime('%H'))

def fetch(h, x):
    responce =requests.get(URL)
    data = responce.json()
    if x == "west":
        return data["westPrices"]["2024-08-26T00:00:00"]["prices"][h]["price"]
    elif x == "east":
        return data["eastPrices"]["2024-08-26T00:00:00"]["prices"][h]["price"]
        
print(fetch(int(timenr),"west"))
print(fetch(int(timenr),"east"))

