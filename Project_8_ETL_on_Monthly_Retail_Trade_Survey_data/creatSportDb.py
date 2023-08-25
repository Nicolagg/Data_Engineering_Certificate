import mysql.connector
import csv
import yaml


# Define the new database and table names
newDb = 'csvTest'
newTable ='sport'


# Define the CSV file to import
csvFile = 'csv/sport.csv'


#import connection yaml file 

with open('connection_test.yaml', 'r') as f:
    connection = yaml.safe_load(f)


# Connect to the MySQL server
cnx = mysql.connector.connect(**connection)

#  creates a cursor object that can be used to execute SQL queries
cursor = cnx.cursor()

# Drop the database if it already exists
dropDb = f'DROP DATABASE IF EXISTS {newDb}'
cursor.execute(dropDb)

# Create the new database
creatDB = f'CREATE DATABASE {newDb}'
cursor.execute(creatDB)

# Commit the changes to the database
cnx.commit()

# Connect to the newly created database
cnx = mysql.connector.connect(**connection, database = newDb)


cursor = cnx.cursor()


# Read the headers from the CSV file to create column names for the table
with open(csvFile) as csv_file:
    reader = csv.reader(csv_file, delimiter=";")
    headers = next(reader) # skip the header row
    columnNames = list(headers)

# Define the variable type for each column in the table
variableType = 'VARCHAR(50)'

# Generate the SQL statement to create the new table
tableCreation =f'CREATE TABLE {newTable}(\nID INT AUTO_INCREMENT PRIMARY KEY,\n'
tableList = []

# Generate column names for the new table based on the headers in the CSV file
for columnName in columnNames:
    colConcat = columnName.replace(" ", "_").replace(".", "").replace("(", "").replace(")", "").replace(",", "_").replace("'", "_")
    tableList.append(colConcat)
    tableCreation = f'{tableCreation} {colConcat} {variableType} NULL,\n'
    
# remove the last comma and whitespace character from a string     and add )
tableCreation=tableCreation[:-2]+ ')'

# Print the SQL statement to create the new table
print(f'SQL table creation:\n {tableCreation}')

# Execute the SQL statement to create the new table
cursor.execute(tableCreation)

# Commit the changes to the database
cnx.commit()

# Generate the SQL statement to insert new data into the table
columnsString = ', '.join(tableList)

ValuesString = 'VALUES ('
for s  in range(len(tableList)-1): # -1 because the last string must contain %s)
    ValuesString = f'{ValuesString}%s, '
ValuesString = f'{ValuesString}%s)'   

#Final INSERT INTO statment
tableInfo = f'INSERT INTO {newTable} ({columnsString}) {ValuesString}'

# Print the SQL statement to INSERT the new table
print(f'SQL insert into\n {tableInfo}')



# Read data from the CSV file and insert it into the new table
with open(csvFile) as csv_file:
    
    # Read CSV file
    reader = csv.reader(csv_file, delimiter=";")
    headers = next(reader) # skip the header row

    # Loop through data and insert each row into the new table
    for row in reader:
        print(row)
        cursor.execute(tableInfo,row)
        emp_no = cursor.lastrowid

# Commit the changes to the database
cnx.commit()

# Close the cursor and connection to the database
cursor.close()
cnx.close()

print("done")
