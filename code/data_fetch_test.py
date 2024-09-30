from datetime import datetime
import mysql.connector
import requests

# Constant values
DATE_DATA = datetime.now().isoformat()[0:11] + '00:00:00'
TIME = datetime.now().strftime('%H')
DATE = datetime.now().strftime('%d-%m-%Y')
TODAY = "https://api.energifyn.dk/api/graph/consumptionprice?date=" + DATE 
TOMORROW = "https://api.energifyn.dk/api/graph/consumptionprice?date=" + DATE

'''
# Connect to database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="mydatabase"
)

if (mydb.is_connected()) == True:
    print("Connected to database")

mycursor = mydb.cursor()
'''

def fetch() -> dict:
    try: 
        response = requests.get(TODAY)
        data = response.json()
    except  ConnectionError as e:
        print(f"Error: {e}")
    return data

def format(data, date):
    east, west = [], []
    for hour in range(0, 24):
        if hour < 10:
            east.append(data['eastPrices'][date]['prices'][int(f"0{hour}")]['price'])
            west.append(data['westPrices'][date]['prices'][int(f"0{hour}")]['price'])
        else:
            east.append(data['eastPrices'][date]['prices'][hour]['price'])
            west.append(data['westPrices'][date]['prices'][hour]['price'])
    return east, west

def insert_prices3(west, east, datotid): #Insert én række i et table
    sql = f"INSERT INTO prices3 (west, east, datotid) VALUES (%s, %s, %s)"
    val = (west, east, datotid)
    print(sql)
    print(val)

    mycursor.execute(sql,val)
    mydb.commit()
    print("1 record inserted, ID:", mycursor.lastrowid)

data = fetch()
eastPrice, westPrice = format(data, DATE_DATA)
data.clear()

for hour in range(0, 24):
    if hour < 10:
        #insert_prices3(westPrice[hour], eastPrice[hour], hour, f"{DATE}")
        print(westPrice[hour], eastPrice[hour], hour, f"{DATE}")
    else:
        #insert_prices3(westPrice[hour], eastPrice[hour], hour, f"{DATE}")
        print(westPrice[hour], eastPrice[hour], hour, f"{DATE}")
