import os
from dotenv import load_dotenv
from datetime import datetime
from dmi_open_data import DMIOpenDataClient, Parameter

load_dotenv()

api_key = os.getenv("DMI_API_KEY")

client = DMIOpenDataClient(api_key=api_key)
stations = client.get_stations(limit=10000)
#print(stations[0]['properties'].keys())

closest_station = client.get_closest_station(latitude=55.395922, longitude=10.388319)

print(closest_station)

# Get available parameters
parameters = client.list_parameters()

for station in stations:
    if station['properties'].get('stationId') == '06034':
        station1 = station

# Get temperature observations from DMI station in given time period
observations = client.get_observations(
    parameter=Parameter.TempDry,
    station_id=station1['properties']['stationId'],
    from_time=datetime(2024, 9, 9),
    to_time=datetime(2024, 9, 10),
    limit=1000)

