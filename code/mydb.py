import mysql.connector

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
                   id INT AUTO_INCREMENT PRIMARY KEY,
                   username VARCHAR(15),
                   password VARCHAR(30),
                   user_id INT AUTO_INCREMENT,
                   created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                   updated_at ON UPDATE CURRENT_TIMESTAMP
                   FOREIGN KEY (user_id) REFERENCES userinfo(id)
                   )"""

userinfo_test = """CREATE TABLE userinfo (
                   id INT AUTO_INCREMENT PRIMARY KEY,
                   firstname VARCHAR(20) NOT NULL,
                   lastname VARCHAR(20) NOT NULL,
                   address VARCHAR(20) NOT NULL,
                   postalcode VARCHAR(4) NOT NULL,
                   phone VARCHAR(8) NOT NULL,
                   created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                   updated_at ON UPDATE CURRENT_TIMESTAMP
                   )"""

#mycursor.execute(brugere_test)
#mycursor.execute("CREATE TABLE prices (dato VARCHAR(255), price VARCHAR(255))")

def vis():
    mycursor.execute("SHOW DATABASES")
    for x in mycursor:
      print(x)

def std_insert(table: str, coulum_1: str, coulum_2: str, value_1: str, value_2: str): #Insert én række i et table
    sql = f"INSERT INTO {table} ({coulum_1}, {coulum_2}) VALUES (%s, %s)"
    val = (f"{value_1}", f"{value_2}")

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

def std_kundequery(table: str, coulumn: str, adress: str):
    
    sql = f"SELECT * FROM {table} WHERE address ='{adress}'"

    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)


#std_query("prices", "dato", "price", "all")
#std_insert("prices", "dato", "price", "16-09-2024", "1.05")

# Disconnect
mydb.close()