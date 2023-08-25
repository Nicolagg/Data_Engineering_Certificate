import mysql.connector
import yaml 

# define the name of the new database
newDb = 'mrts'


with open('connection.yaml', 'r') as f:
    connection = yaml.safe_load(f)
    
    
# establish a connection to the MySQL database
cnx = mysql.connector.connect(**connection, database = newDb)   
cursor = cnx.cursor()



# Exécutez la première requête et stockez les résultats dans une variable
query = """
SELECT YerlyValue
FROM controledata
WHERE IDcat = 65 AND Year = '1992';
"""
cursor.execute(query)

for row in cursor.fetchall():
    print(row)

cursor.close()
cnx.close()
print('donne')