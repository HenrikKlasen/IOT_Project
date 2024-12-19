from pymongo import MongoClient

def checkDB(database):
    print(database.list_collection_names())

if __name__ == "__main__":
    #connect to the MongoDB server
    client = MongoClient("mongodb://localhost:27017/")
    #create database
    db = client.db
    #create collections to separate the data regarding rooms from the data regarding the sensors
    roomsCollection = db["rooms_collection"]
    sensorsCollection = db['sensors_collection']
    
    #verify that the collections have been created
    checkDB(db)
    
    print("Rooms Collection:")
    for room in roomsCollection.find():
        print(room)
