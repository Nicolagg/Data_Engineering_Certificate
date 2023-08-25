from pymongo import MongoClient

# set up the MongoDB connection
client = MongoClient('mongodb://localhost:27017')
db = client['employee']

# get the employees collection
collection = db['employee']

# find all employees with last name "Smith"
employeeCursor = collection.find({"LastName": "Smith"})

# print the employee records
for employee in employeeCursor:
    print(employee)