import requests


try: 
    URL = "https://www.dmi.dk/lokation/show/DK/2615876/Odense/?api-key="
    response = requests.get(URL)
    data = response.json()
except  ConnectionError as e:
    print(f"Error: {e}")

print(data)