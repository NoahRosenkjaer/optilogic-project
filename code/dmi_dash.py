import os
from dotenv import load_dotenv
from datetime import datetime
from dmi_open_data import DMIOpenDataClient, Parameter

load_dotenv()

api_key = os.getenv("DMI_API_KEY")

url = "https://dmigw.govcloud.dk/v2/metObs/collections/observation/items?api-key=" + api_key

client = DMIOpenDataClient(api_key=api_key)
stations = client.get_stations(limit=10000)
#print(stations[0]['properties'].keys())

closest_station = client.get_closest_station(
    latitude=55.395922,
    longitude=10.388319)

#print(closest_station['properties'])

# Get available parameters
parameters = client.list_parameters()
#print(parameters)
# Nøgle til cloud cover: 'cloud_cover'

'''for station in stations:
    if station['properties'].get('stationId') == '22162':
        station1 = station'''

#station = stations[5]
#print(station['properties']['parameterId'])

count = 0

stationer_med_cloud_cover = []
stationer_med_temperatur = []

# for station in stations:
#     for parameter in station['properties']['parameterId']:
#         if parameter == 'cloud_cover':
#             stationer_med_cloud_cover.append(station)


for station in stations: 
    if 'cloud_cover' in station['properties'].get('parameterId'):
        stationer_med_cloud_cover.append(station)
    if 'temp_dry' in station['properties'].get('parameterId'):
        stationer_med_temperatur.append(station)

'''stationer = []
for station in stations: 
    if 'cloud_cover' in station['properties'].get('parameterId') and 'temp_dry' in station['properties'].get('parameterId'):
        stationer.append(station['properties']['stationId'])'''


odense_coord = [10.3883, 55.3959]

def min_distance(my_coords: list, station_coords: list):
    distance = abs(my_coords[0] - station_coords[0]), abs(my_coords[1] - station_coords[1])
    averaged = (distance[0]+distance[1])/2
    return averaged

distances = []
for station in stationer_med_cloud_cover:
    station_coords = station['geometry']['coordinates']
    dist = min_distance(odense_coord, station_coords)
    distances.append(dist)

counter = 0
for station in stationer_med_cloud_cover:
    if distances[counter] == min(distances):
        break
    counter += 1

print(counter)
closest_stationid = stationer_med_cloud_cover[counter]['properties']['stationId']        
print(closest_stationid)

# Get temperature observations from DMI station in given time period
observations = client.get_observations(
    parameter=Parameter.CloudCover,
    station_id=closest_stationid,
    from_time=datetime(2020, 7, 20),
    to_time=datetime(2024, 7, 24),
    limit=100000)

# observations = client.get_observations(
#     parameter=Parameter.TempDry,
#     station_id=stationer[1],
#     from_time=datetime(2020, 7, 20),
#     to_time=datetime(2024, 7, 24),
#     limit=1000)

# print(observations)

# def json_serialization(json_frag: dict, file_name: str):
#     file_name = file_name+".json"
#     with open(file_name, 'w') as file:
#         json.dump(json_frag, file)

# #print(observations[0]['properties']['value'])
list_of_obs = []
for observation in observations:
    list_of_obs.append(observation['properties']['value']) 

# json_serialization(observations, "obs")
print(list_of_obs)
