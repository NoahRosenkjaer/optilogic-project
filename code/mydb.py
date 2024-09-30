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
                   phone VARCHAR(8) NOT NULL,
                   created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                   updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
                   )"""

userinfo_test1 = "CREATE TABLE userinfo (info_id INT AUTO_INCREMENT PRIMARY KEY, firstname VARCHAR(20) NOT NULL, lastname VARCHAR(20) NOT NULL, address VARCHAR(20) NOT NULL, postalcode VARCHAR(4) NOT NULL, phone VARCHAR(8) NOT NULL, created_at DATETIME DEFAULT CURRENT_TIMESTAMP, updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)"

ny_priser = """CREATE TABLE prices3 (
            id INT AUTO_INCREMENT PRIMARY KEY, 
            west float, 
            east float, 
            datotid VARCHAR(16) UNIQUE)"""

#print(userinfo_test)
#mycursor.execute(userinfo_test)

""" Funktioner til alt muligt """

def vis():
    mycursor.execute("SHOW DATABASES")
    for x in mycursor:
      print(x)

def insert_prices3(west, east, datotid): #Insert én række i et table
    sql = f"INSERT INTO prices3 (west, east, datotid) VALUES (%s, %s, %s)"
    val = (west, east, datotid)
    print(sql)
    print(val)

    mycursor.execute(sql,val)
    mydb.commit()
    print("1 record inserted, ID:", mycursor.lastrowid)


def std_query(table: str, coulum_1: str, coulumn_2: str, all: str,): #Fetcher kolonner fra et table.
    
    if all == "all":
        query = f"SELECT * FROM {table}"

    elif all == "0":
        query = f"SELECT {coulum_1},{coulumn_2} FROM {table}" 
    print(query)

    mycursor.execute(query)
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

def std_kundequery(table: str, adress: str):
    
    sql = f"SELECT * FROM {table} WHERE address ='{adress}'"

    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

def insert_userinfo(firstname_1, lastname_1, address_1, postalcode_1, phone_1):

    sql = f"INSERT INTO userinfo (firstname, lastname, address, postalcode, phone) VALUES (%s, %s, %s, %s, %s)"
    val = (firstname_1, lastname_1, address_1, postalcode_1, phone_1)

    print(sql)
    print(val)

    mycursor.execute(sql,val)
    mydb.commit()
    print("1 record inserted, ID:", mycursor.lastrowid)



dagsdato = dt.datetime.now().strftime("%d-%m-%Y %H")
#std_query("prices", "west", "east", "all")
insert_prices3("6.69", "9.69", f"{dagsdato}")
#insert_userinfo("Rasmus", "Joergensen", "Bredstedgade 36", "5000", "41191137")
#std_kundequery("userinfo", "Bredstedgade 36")

'''sql = "INSERT INTO prices (west, east, datotid) VALUES (%s, %s, %s)"
val = ("1.05", "5.05", f"{dagsdato}")
mycursor.execute(sql, val)'''

# Disconnect
#mydb.commit()
mydb.close()

"""Pris west + øst + timetal + dato/tid(manuel indsættelse)(primarykey)"""
"""Skydække, vindhastighed"""


'''testtt = mycursor.execute("SHOW TABLES;")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)'''

#docker exec -it OptiLogic mysql -u root -p