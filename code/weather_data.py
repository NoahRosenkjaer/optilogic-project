import requests


try: 
    URL = "https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=60.10&lon=9.58"
    response = requests.get(URL)
    data = response.json()
except  ConnectionError as e:
    print(f"Error: {e}")

print(data)