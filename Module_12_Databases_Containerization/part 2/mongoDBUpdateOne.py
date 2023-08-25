from pymongo import MongoClient

# set up the MongoDB connection
client = MongoClient('mongodb://localhost:27017')
db = client['employee']

# get the employees collection
collection = db['employee']

# create a filter for the employee with last name "Rose"
filter = {"LastName": "Rose"}

# define the new values to be updated
newvalues = {"$set": {"Age": 32}}

# update the employee record
collection.update_one(filter, newvalues)

# print all employee records to verify the update
employeeCursor = collection.find()
for employee in employeeCursor:
    print(employee)
