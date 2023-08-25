import csv
import mysql.connector
from datetime import datetime
import yaml

#csv file names
csvFile = [*range(1992, 2021, 1)]

#string to exclud during importation
listOfStrings = ['(NA)','','(S)']   

# New database name
newDb = 'mrts'

# Import connection YAML file 
with open('connection.yaml', 'r') as f:
    connection = yaml.safe_load(f)

# Connect to the MySQL server and create a new database named "newDb"
cnx = mysql.connector.connect(**connection)

# Create a new database named "newDb"
cursor = cnx.cursor()
cursor.execute(f'DROP DATABASE IF EXISTS {newDb}')           
cursor.execute(f'CREATE DATABASE {newDb}')
cnx.commit()

# Connect to the "newDb" database
cnx = mysql.connector.connect(**connection, database = newDb)
cursor = cnx.cursor()
# Create three new tables in the "newDb" database: "category", "data", and "controledata"

cursor.execute("""
                    CREATE TABLE category (
                    ID INT AUTO_INCREMENT PRIMARY KEY,                    
                    Kind_of_Business VARCHAR(255) NULL,
                    NAICS_Code VARCHAR(50) NULL
                    );
                """)

cursor.execute("""
                    CREATE TABLE data (
                    ID INT AUTO_INCREMENT PRIMARY KEY,
                    date DATE,
                    Value INT NULL,
                    IDcat INT,
                    FOREIGN KEY (IDcat) REFERENCES Category(ID)
                    );
                """)

cursor.execute("""
                    CREATE TABLE controledata (
                    ID INT AUTO_INCREMENT PRIMARY KEY,
                    YerlyValue INT NULL,
                    Year YEAR,
                    IDcat INT,
                    FOREIGN KEY (IDcat) REFERENCES Category(ID)
                    );      
""")

cnx.commit()


# Print "done" to indicate that the script has finished executing
print('Table creation done')


# Connect to the MySQL server and create a new database named "newDb"
cnx = mysql.connector.connect(**connection, database = newDb)
cursor = cnx.cursor()
  

# Define the columns for the category table
columns = ("""
            INSERT INTO category
            (NAICS_Code, Kind_of_Business)
            VALUES (%s, %s)
            """
            )

# Import data into the category table for the first CSV file

with open(f'csv/{csvFile[0]}.csv') as csv_file:
    
    # Read CSV file
    csv_reader = csv.reader(csv_file, delimiter=';')

    # Get the rows as a list
    rows = list(csv_reader)

    # Get the desired row and cell
    for y in range(1, 66):
        # loop troo row 
        desired_row = rows[y]
        
        #select naics_code column in the csv file
        naics_code = desired_row[0]
        
        #select kind_of_business column in the csv file
        kind_of_business = desired_row[1]
    
        data = (naics_code, kind_of_business)

        cursor.execute(columns, data)
        
# Commit the changes
cnx.commit()



def addData (columns, fileNale, excludList):
    
    with open(f'csv/{fileNale}.csv') as csv_file:

        # Read CSV file
        csv_reader = csv.reader(csv_file, delimiter=';')

        # Get the rows as a list
        rows = list(csv_reader)

        for y in range(1, 66):

            desired_row = rows[y]
            data = (y,)
            date_str = ()
            for x in range(2, 14):

                date_str = f'{x-1}.{fileNale}' #date in fomat mm.yyyyy
                date_object = datetime.strptime(date_str, '%m.%Y').strftime('%Y-%m-%d')
                
            
                # Check if the cell is empty
                if desired_row[x] in excludList:
                    cell= None
                    
                else: 
                    cell = int(desired_row[x].replace(" ", ""))
                    


                data = (date_object, cell, y)

                #print(data)

                cursor.execute(columns, data)


                data = (y,)
    # Commit the changes
    cnx.commit()
    
    
listOfStrings = ['(NA)','','(S)']    

columns = ("""
            INSERT INTO data
            (date, Value, IDcat)
            VALUES (%s, %s, %s)
            """)

for fil in csvFile:   
    addData(columns,fil,listOfStrings)
            
# Commit the changes
cnx.commit()



def addControlData(columns, fileNale,excludList):
    with open(f'csv/{fileNale}.csv') as csv_file:

        # Read CSV file
        csv_reader = csv.reader(csv_file, delimiter=';')

        # Get the rows as a list
        rows = list(csv_reader)

        for IDcat in range(1, 66):

            desired_row = rows[IDcat]
            data = (IDcat,)
            date_str = ()


            date_str = fileNale

            if desired_row[14] in excludList:
                cell= None
                    
            else: 
                cell = int(desired_row[14].replace(" ", ""))
                

            data = (cell,) + ((date_str),  IDcat)

            #print(data)

            #cursor.execute(columns, data)

            cursor.execute(columns, data)
            data = (y,)
    # Commit the changes
    cnx.commit()
    
columns = ("""
            INSERT INTO controledata 
            (YerlyValue, Year, IDcat) 
            VALUES (%s, %s, %s)
            """)

for file in csvFile:             
    addControlData(columns, file,listOfStrings)
            
            
# Commit the changes
cnx.commit()

# Close the cursor and the connection
cursor.close()
cnx.close()

print('Insert value done')


