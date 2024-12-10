from pymongo import MongoClient

def checkDB(database):
    print(database.list_collection_names())

if __name__ == "__main__":
    #connect to the MongoDB server
    client = MongoClient("mongodb://localhost:27017/")
    #create database
    db = client.db
    #create collections to separate the data regarding rooms from the data regarding the sensors
    roomsCollection = db.rooms
    sensorsCollection = db.sensors
    
    #verify that the collections have been created
    checkDB(db)
    
    # print("Rooms Collection:")
    # for room in roomsCollection.find():
    #     print(room)
    # print("\nSensors Collection:")
    # for sensor in sensorsCollection.find():
    #     print(sensor)
