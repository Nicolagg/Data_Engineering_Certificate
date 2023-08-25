import mysql.connector
import pandas as pd
import yaml 

# define the name of the new database
newDb = 'mrts'


with open('connection.yaml', 'r') as f:
    connection = yaml.safe_load(f)
    
    
# establish a connection to the MySQL database
cnx = mysql.connector.connect(**connection, database = newDb)    


# create a cursor object to execute SQL queries
cursor = cnx.cursor()

# define a function to perform data verification
def totalVerification(IDcat, Year):
    
    # select yearly values from the 'controledata' table
    query1 = f"""
    SELECT YerlyValue
    FROM controledata
    WHERE IDcat = {IDcat} AND Year LIKE '{Year}%';
    """
    cursor.execute(query1)
    result1 = cursor.fetchall()
    
    # select the sum of values from the 'data' table
    query2 = (f"""
    SELECT SUM(data.Value) as Total_Value
    FROM data
    WHERE IDcat = {IDcat}  AND date LIKE '{Year}%';
    """)
    cursor.execute(query2)
    result2 = cursor.fetchall()
    cnx.commit()

    
    # compare the two results and return an error if they don't match
    if result1[0][0] !=  result2[0][0]:
        controledataValue = result1[0][0]
        SumDataValue = result2[0][0]
        category = IDcat
        year = Year
        sumError = [(controledataValue),int(SumDataValue) ,category,year ]
        return sumError

# create lists of category IDs and years to iterate over
categorys = [*range(1, 64, 1)]
Years = [*range(1992, 2021, 1)]

# iterate over each combination of category and year
for category in categorys:
    for Year in Years:
        # call the 'totalVerification' function and print any errors that are returned
        wrongRow = totalVerification(category, Year)
        if wrongRow != None:
            print(wrongRow)
            

# Close the cursor and connection to the database
cursor.close()
cnx.close()