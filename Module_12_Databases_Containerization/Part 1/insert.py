import mysql.connector
from datetime import datetime
import uuid
import sys
sys.dont_write_bytecode = True

cnx = mysql.connector.connect(user='root', 
    password='password',
    host='127.0.0.1',
    database='My_snowboards',
    auth_plugin='mysql_native_password')

# create cursor
cursor = cnx.cursor()

# liste des données à insérer
snowboards = [
    {
        "brand": "Arbor",
        "size": 156,
        "boardType": "Freeride"
    },
    {
        "brand": "Jones",
        "size": 154,
        "boardType": "All mountain"
    },
    {
        "brand": "Burton",
        "size": 150,
        "boardType": "Freestyle"
    }
]

# boucle pour insérer les données dans la table
for board in snowboards:
    id = str(uuid.uuid4())
    brand = board["brand"]
    size = board["size"]
    boardType = board["boardType"]
    query = f'INSERT INTO `snowboard` VALUES ("{id}", "{brand}", {size}, "{boardType}")'
    cursor.execute(query)

# clean up
cnx.commit()
cursor.close()
cnx.close()    