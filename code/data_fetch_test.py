import datetime as dt
import requests
from datetime import datetime

# Constant values
DATE_DATA = datetime.now().isoformat()[0:11] + "00:00:00"
TIME = (dt.datetime.now().strftime('%H'))
DATE = datetime.now().strftime("%d-%m-%Y")
TARIF = 0.0925

def fetch() -> dict:
    try: 
        URL = f"https://api.energifyn.dk/api/graph/consumptionprice?date={DATE}"
        response = requests.get(URL)
        data = response.json()
    except  ConnectionError as e:
        print(f"Error: {e}")
    return data

def get(h: int, compas: str, data: dict, date: str) -> dict:
    if compas == "east":
        print(data['eastPrices'][str(date)]['prices'][h])
        return data['eastPrices'][str(date)]['prices'][h]
    else:
        print(data['westPrices'][str(date)]['prices'][h])
        return data['westPrices'][str(date)]['prices'][h]

def graph(data, date):
    import matplotlib.pyplot as plt
    import numpy as np

    x, y = [], []

    for element in data['westPrices'][str(date)]['prices']:
        x.append(element['hour'][11:13])
        y.append(element['price'])

    fig, ax = plt.subplots()

    ax.bar(x, y, width=1, edgecolor="white", linewidth=0.5)
    ax.set_ylabel("Price [kr./kWh]")
    ax.set_xlabel("Time [Hours]")

    plt.show()

data = fetch()
print(data)
#get(int(TIME), "west", data, DATE_DATA)
#get(int(TIME), "east", data, DATE_DATA)
#graph(data, DATE_DATA)
