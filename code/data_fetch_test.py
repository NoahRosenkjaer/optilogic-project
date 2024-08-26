import datetime as dt
import requests
import datetime

# Constant values
DATO = datetime.datetime.now().isoformat()[0:11] + "00:00:00"
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

def graph(data):
    import matplotlib.pyplot as plt
    import numpy as np

    x, y = [], []

    for element in data['westPrices']['2024-08-26T00:00:00']['prices']:
        x.append(element['hour'][11:13])
        y.append(element['price'])

    fig, ax = plt.subplots()

    ax.bar(x, y, width=1, edgecolor="white", linewidth=0.5)
    ax.set_ylabel("Price [kr./kWh]")
    ax.set_xlabel("Time [Hours]")

    plt.show()

data = fetch()
get(int(TIME), "west", data, DATO)
get(int(TIME), "east", data, DATO)
graph(data)
