import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="mydatabase"
)
print(mydb.is_connected())
mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE mydatabase")
#mycursor.execute("CREATE TABLE prices (dato VARCHAR(255), price VARCHAR(255))")

#mycursor.execute("SHOW DATABASES")
#mycursor.execute("SHOW TABLES")

# for x in mycursor:
#     print(x)

#print(mydb)

# Indsættelse af daa
'''
sql = "INSERT INTO prices (dato, price) VALUES (%s, %s)"
val = ("28-08-2024", "1.2")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
'''



mycursor = mydb.cursor()
  
query = "SELECT dato, price FROM prices"
mycursor.execute(query)
   
myresult = mycursor.fetchall()
   
for x in myresult:
    print(x)

