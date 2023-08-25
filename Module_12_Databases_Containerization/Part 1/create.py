import mysql.connector
import sys
sys.dont_write_bytecode = True

cnx = mysql.connector.connect(user='root', 
    password='password',
    host='127.0.0.1',
    database='',
    auth_plugin='mysql_native_password')

# create cursor
cursor = cnx.cursor()

# delete previous db
query = ("DROP DATABASE IF EXISTS `My_snowboards`;")
cursor.execute(query)

# create db
query = ("CREATE DATABASE IF NOT EXISTS My_snowboards")
cursor.execute(query)

# use db
query = ("USE My_snowboards")
cursor.execute(query)

# create table
query = ('''
CREATE TABLE snowboard(
    id VARCHAR(36),
    brand VARCHAR(20),
    size int,
    boardType VARCHAR(20)
)
''')
cursor.execute(query)

# clean up
cnx.commit()
cursor.close()
cnx.close()    