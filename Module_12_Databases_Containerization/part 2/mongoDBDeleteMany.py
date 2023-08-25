import pymongo

# Connect to the MongoDB server
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Access the employee database and employees collection
db = client["employee"]
collection = db["employee"]

# Define the filter
filter = {"LastName": "Smith"}

# Call the delete_many method with filter
collection.delete_many(filter)

# Print the updated collection
for employee in collection.find():
    print(employee)
