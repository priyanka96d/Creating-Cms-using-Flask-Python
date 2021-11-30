import mysql.connector
from requests import api
import apiCalling


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="purva123",
    database="ecommerce"
)
mycur = mydb.cursor()
#mycur.execute("CREATE DATABASE ecommerce")

#mycur.execute("CREATE TABLE products (id INT NOT NULL PRIMARY KEY ,title VARCHAR(300),price INT(100),category VARCHAR(100), desc VARCHAR(300),image VARCHAR(100))")

mycur.execute("""CREATE TABLE IF NOT EXISTS products 
(id INT  PRIMARY KEY AUTO_INCREMENT, title VARCHAR(255), price INT(100),category VARCHAR(100),
description LONGTEXT,image VARCHAR(100))""")

sql = "INSERT INTO products (id,title,price,category,description,image) VALUES (%s,%s,%s,%s,%s,%s)"

val = []
for i in range(20):
    val.append([apiCalling.id[i],apiCalling.title[i],apiCalling.price[i],apiCalling.category[i],apiCalling.desc[i],apiCalling.image[i]])

mycur.executemany(sql, val)

mydb.commit()

print(mycur.rowcount, "was inserted.")    