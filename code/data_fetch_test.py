from datetime import datetime
import mysql.connector
import requests

# Constant values
DATE_DATA = datetime.now().isoformat()[0:11] + "00:00:00"
TIME = datetime.now().strftime('%H')
DATE = datetime.now().strftime("%d-%m-%Y")

# Connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="mydatabase"
)

if (mydb.is_connected()) == True:
    print("Connected to database")

mycursor = mydb.cursor()



def clean(data):
    for hour in range(0, 24):
        if hour < 10:
            data['eastPrices']['2024-09-30T00:00:00']['prices'][int(f"0{hour}")].pop("tarifPrice")
            data['westPrices']['2024-09-30T00:00:00']['prices'][int(f"0{hour}")].pop("tarifPrice")
        else:
            data['eastPrices']['2024-09-30T00:00:00']['prices'][hour].pop("tarifPrice")
            data['westPrices']['2024-09-30T00:00:00']['prices'][hour].pop("tarifPrice")
    
    data.pop('customerPrices')
    data.pop('currentEastPowerPrice')
    data.pop('currentWestPowerPrice')
    data.pop('currentCustomerPowerPrice')

    return data

def fetch() -> dict:
    try: 
        URL = f"https://api.energifyn.dk/api/graph/consumptionprice?date={DATE}"
        response = requests.get(URL)
        data = response.json()
    except  ConnectionError as e:
        print(f"Error: {e}")
    data = clean(data)
    return data

def get(h: int, compas: str, data: dict, date: str) -> dict:
    if compas == "east":
        print(data['eastPrices'][str(date)]['prices'][h]) 
    else:
        print(data['westPrices'][str(date)]['prices'][h])

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


dagsdato = datetime.now().strftime("%d-%m-%Y")

data = fetch()
eastPrice, westPrice = format(data, DATE_DATA)

print(dagsdato)

for hour in range(0, 24):
    insert_prices3(westPrice[hour], eastPrice[hour], f"{dagsdato + hour}")
    #print(westPrice[hour], eastPrice[hour], f"{dagsdato} {hour}")