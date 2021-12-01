import collections
from pymongo import MongoClient, errors



def connect_to_db():
    try:
        # try to instantiate a client instance
        client = MongoClient(
            host='test_mongodb',
            serverSelectionTimeoutMS = 3000, # 3 second timeout
            username = "root",
            password = "1234",
        )
        return client

    except errors.ServerSelectionTimeoutError as err:
        print ("pymongo ERROR:", err)
        return None


def search_data(param):
    client = connect_to_db()
    if client:
        db = client.garments
        collection = db.get_collection("garmentData")
        data = collection.find({"product_title" : { "$regex" : f"{param}" }})
        return data
    else:
        return None
        
