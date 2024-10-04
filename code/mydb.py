import mysql.connector
import datetime as dt


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

""" Lav en database """
#mycursor.execute("CREATE DATABASE mydatabase")

''' Lav et table '''

users_test = """CREATE TABLE users (
                   user_id INT AUTO_INCREMENT PRIMARY KEY,
                   username VARCHAR(15),
                   password VARCHAR(30),
                   info_id FOREIGN KEY REFERENCES userinfo(info_id)
                   created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                   updated_at ON UPDATE CURRENT_TIMESTAMP
                   )"""

userinfo_test = """CREATE TABLE userinfo (
                   info_id INT AUTO_INCREMENT PRIMARY KEY,
                   firstname VARCHAR(20) NOT NULL,
                   lastname VARCHAR(20) NOT NULL,
                   address VARCHAR(20) NOT NULL,
                   postalcode VARCHAR(4) NOT NULL,
                   phone VARCHAR(8) NOT NULL UNIQUE,
                   created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                   updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
                   )"""

userinfo_test1 = "CREATE TABLE userinfo (info_id INT AUTO_INCREMENT PRIMARY KEY, firstname VARCHAR(20) NOT NULL, lastname VARCHAR(20) NOT NULL, address VARCHAR(20) NOT NULL, postalcode VARCHAR(4) NOT NULL, phone VARCHAR(8) NOT NULL, created_at DATETIME DEFAULT CURRENT_TIMESTAMP, updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)"

ny_priser = """CREATE TABLE prices3 (
            id INT AUTO_INCREMENT PRIMARY KEY, 
            west FLOAT, 
            east FLOAT, 
            time VARCHAR(2),
            dato DATE
            )"""

"""Til efter prices3 er oprettet"""
#ALTER TABLE prices3 
#ADD UNIQUE INDEX idx_unique_date_time (dato, time);

#print(userinfo_test)
#mycursor.execute(ny_priser)

""" Funktioner til alt muligt """

def vis():
    mycursor.execute("SHOW DATABASES")
    for x in mycursor:
      print(x)

def insert_prices3(west, east, time, dato): #Insert én række i et table
    sql = f"INSERT INTO prices3 (west, east, time, dato) VALUES (%s, %s, %s, %s)"
    val = (west, east, time, dato)
    print(sql)
    print(val)

    mycursor.execute(sql,val)
    mydb.commit()
    print("1 record inserted, ID:", mycursor.lastrowid)


def std_query(table: str, coulum_1: str, all: str,): #Fetcher kolonner fra et table.
    
    if all == "all":
        query = f"SELECT * FROM {table}"

    elif all == "0":
        query = f"SELECT {coulum_1} FROM {table}" 
    print(query)

    mycursor.execute(query)
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

def std_kundequery(table: str, adress: str): # Find et row
    
    sql = f"SELECT * FROM {table} WHERE address ='{adress}'"

    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

def insert_userinfo(firstname_1, lastname_1, address_1, postalcode_1, phone_1): # Insæt data i userinfo

    sql = f"INSERT INTO userinfo (firstname, lastname, address, postalcode, phone) VALUES (%s, %s, %s, %s, %s)"
    val = (firstname_1, lastname_1, address_1, postalcode_1, phone_1)

    print(sql)
    print(val)

    mycursor.execute(sql,val)
    mydb.commit()
    print("1 record inserted, ID:", mycursor.lastrowid)

dagsdato = dt.datetime.now().strftime("%Y-%m-%d") #("%Y-%m-%d") ("%d-%m-%Y")
#std_query("prices3", "west", "0")
#insert_prices3("6.69", "9.69", "01", f"{dagsdato}")
#insert_userinfo("Rasmus", "Jørgensen", "Bredstedgade 36", "5000", "41191137")
#std_kundequery("userinfo", "Bredstedgade 36")

""" Disconnect """
#mydb.commit()
mydb.close()



### Notater
"""Skydække, vindhastighed"""


'''testtt = mycursor.execute("SHOW TABLES;")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)'''

#docker exec -it OptiLogic mysql -u root -p