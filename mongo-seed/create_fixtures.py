from pymongo import MongoClient, errors
import json_lines
# global variables for MongoDB host (default port is 27017)
DOMAIN = '0.0.0.0'
PORT = 27017

# use a try-except indentation to catch MongoClient() errors
try:
    # try to instantiate a client instance
    client = MongoClient(
        host='test_mongodb',
        serverSelectionTimeoutMS = 3000, # 3 second timeout
        username = "root",
        password = "1234",
    )

    # print the version of MongoDB server if connection successful
    print ("server version:", client.server_info()["version"])

    db = client.garments
    collection = db.garmentDataNew
    with open('garment_items.jl', 'rb') as f:
        for item in json_lines.reader(f):
            collection.insert_one(item)
    

except errors.ServerSelectionTimeoutError as err:
    # set the client and DB name list to 'None' and `[]` if exception
    client = None

    # catch pymongo.errors.ServerSelectionTimeoutError
    print ("pymongo ERROR:", err)
