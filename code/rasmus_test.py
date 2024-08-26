import requests
import datetime as dt
import datetime

URL = "https://api.energifyn.dk/api/graph/consumptionprice?date=26-08-2024"
timenr = (dt.datetime.now().strftime('%H'))
dato = datetime.datetime.now().isoformat()
dato1 = dato[0:11] + "00:00:00"

def fetch(h,x):
    responce =requests.get(URL)
    data = responce.json()

    if x == "west":
        return data["westPrices"][str(dato1)]["prices"][h]["price"]
    elif x == "east":
        return data["eastPrices"][str(dato1)]["prices"][h]["price"]
        
print(fetch(int(timenr),"west"))
print(fetch(int(timenr),"east"))