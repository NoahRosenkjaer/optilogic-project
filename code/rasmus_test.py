import requests
import datetime as dt
import datetime

DATE = dt.datetime.now().strftime("%d-%m-%Y")
URL = f"https://api.energifyn.dk/api/graph/consumptionprice?date={DATE}"

timenr = (dt.datetime.now().strftime('%H'))
dato = datetime.datetime.now().isoformat()
dato1 = dato[0:11] + "00:00:00"

def fetch(h, x):
    try:
        responce = requests.get(URL)
        data = responce.json()

        if x == "west":
            west = data["westPrices"][str(dato1)]["prices"][h]["price"]
            return west
        
        elif x == "east":
            east = data["eastPrices"][str(dato1)]["prices"][h]["price"]
            return east
        
    except Exception as e:
        print(e)

print(fetch(int(timenr),"west"))
print(fetch(int(timenr),"east"))