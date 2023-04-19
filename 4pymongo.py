from pymongo import MongoClient

#Create a client to connect to a MongoDB instance running on localhost
client = MongoClient('localhost', 27017)

# Access a database
db = client['mydatabase']

# Access a collection in the database
collection = db['mycollection']
print(collection)

#ERROR
doc = {'name': 'John Doe', 'age': 30}
result = collection.insert_one(doc)	
documents = collection.find()
for doc in documents:
    print(doc)
