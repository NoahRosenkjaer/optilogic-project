import requests

def get(h, compas, data):
    if compas == "east":
        return data['eastPrices']['2024-08-26T00:00:00']['prices'][h]
    else:
        return data['westPrices']['2024-08-26T00:00:00']['prices'][h]
        

def fetch():
    URL = "https://api.energifyn.dk/api/graph/consumptionprice?date=26-08-2024"

    response = requests.get(URL)
    data = response.json()
    print(get(10, "west", data))
    print(get(10, "east", data))
    print(response)
    
fetch()