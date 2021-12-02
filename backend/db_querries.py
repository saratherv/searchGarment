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


def search_data(param, offset):
    client = connect_to_db()
    if client:
        db = client.garments
        collection = db.get_collection("garmentDataNew")
        data = collection.find({"product_title" : { "$regex" : f"{param}", "$options" : "i"}}).skip(offset).limit(offset + 50)
        return data
    else:
        return None
        
