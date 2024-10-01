from datetime import datetime, timedelta
import mysql.connector
import requests

# Constant values
DATE_DATA = datetime.now().isoformat()[0:11] + '00:00:00'
DATE = datetime.now()
TODAY = "https://api.energifyn.dk/api/graph/consumptionprice?date=" + DATE.strftime('%d-%m-%Y')
TOMORROW = "https://api.energifyn.dk/api/graph/consumptionprice?date=" + (DATE + timedelta(days=1)).strftime('%d-%m-%Y')


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

# fetch price data from api
def fetch(day) -> dict:
    
    # Try to fetch data and return it, on error print it
    try: 
        response = requests.get(day)
        data = response.json()
    except  ConnectionError as e:
        print(f"Error: {e}")
    return data

# Extracts the wanted data and returns it in 2 lists
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

# Insert into database
def insert_prices3(west, east, time):
    sql = f"INSERT INTO prices3 (west, east, time) VALUES (%s, %s, %s)"
    val = (west, east, time)
    print(sql)
    print(val)

    mycursor.execute(sql,val)
    mydb.commit()
    print("1 record inserted, ID:", mycursor.lastrowid)

# Calls format and fetch to return 2 lists
eastPrice, westPrice = format(fetch(TODAY), DATE_DATA)

# Insert prices from all 24 hours into database
for hour in range(0, 24):
    if hour < 10:
        #insert_prices3(westPrice[hour], eastPrice[hour], f'0{hour}')
        print(westPrice[hour], eastPrice[hour], f'0{hour}')
    else:
        #insert_prices3(westPrice[hour], eastPrice[hour], hour)
        print(westPrice[hour], eastPrice[hour], hour)
