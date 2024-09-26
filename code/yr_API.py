import yr_weather
from geopy.geocoders import Nominatim

# User agents
headers = {
    "User-Agent": "MyTestApp"
}
geolocator = Nominatim(user_agent="MyTestApp")

# Get location
location = input("Enter you address eksample: Seebladsgade 1, 5000\n> ")
location = geolocator.geocode(location)
print(location.address)
print(f"Koordinates are: {(location.latitude, location.longitude)}")

# Init client
my_client = yr_weather.Locationforecast(headers=headers)

# Get forecast based on location
forecast = my_client.get_forecast(location.latitude, location.longitude)

# Define needed data
skyet = forecast.now().details.cloud_area_fraction_medium
wind_speed = forecast.now().details.wind_speed

print(f"Skyet: {skyet} %\nVind hastighed: {wind_speed} m/s")