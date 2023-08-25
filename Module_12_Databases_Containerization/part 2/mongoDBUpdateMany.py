import pymongo

# Connect to the MongoDB server
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Access the employee database and employees collection
db = client["employee"]
collection = db["employee"]

# Define the filter and new values
filter = {"LastName": "Smith"}
newvalues = {"$set": {"Department": "Computer Science"}}

# Call the update_many method with filter and newvalues
collection.update_many(filter, newvalues)

# Print the updated collection
for employee in collection.find():
    print(employee)