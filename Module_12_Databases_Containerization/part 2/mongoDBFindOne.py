from pymongo import MongoClient

# set up the MongoDB connection
client = MongoClient('mongodb://localhost:27017')
db = client['employee']

# get the employees collection
collection = db['employee']

# find the first employee with last name "Rigby"
employee = collection.find_one({"LastName": "Rigby"})

# print the employee record
print(employee)