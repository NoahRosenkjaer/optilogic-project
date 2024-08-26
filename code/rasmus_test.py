import requests

URL = "https://api.energifyn.dk/api/graph/consumptionprice?date=26-08-2024"

responce = requests.get(URL)
data = responce.json()
data_iter = responce.iter_lines()
print(responce)
print(data)
