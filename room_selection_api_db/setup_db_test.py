import json
import os
from pymongo import MongoClient
from check_db import checkDB

def importDataIntoCollection(collection, folderPath, file):
    filePath = os.path.join(folderPath, file)
    try:
        with open(filePath) as f:
            data = json.load(f)
            #all data json files have "rooms" as key, 
            # access the key of the document, 
            # returns empty list if key does not exist
            dataKey = data.get("rooms", [])
            # check if data is a non-empty list  
            if isinstance(dataKey, list) and dataKey: 
                result = collection.insert_many(dataKey).inserted_ids
                return result 
            else:
                print(f"Warning: {file} does not contain a non-empty list of documents.") 
                return 0 
    except json.JSONDecodeError as e: 
        print(f"Error decoding JSON from {file}: {e}") 
        return 0

if __name__ == "__main__":
    #connect to the MongoDB server with MongoDB URI format
    client = MongoClient("mongodb://localhost:27017/")
    #create database
    db = client.db
    #create collections to separate the data regarding rooms from the data regarding the sensors
    roomsCollection = db.rooms
    sensorsCollection = db.sensors

    #insert data from json files into the collections
    folderPath = './Project_sensor_data'
    for file in os.listdir(folderPath):
        if file.endswith('.json'):
            if file == 'rooms_facilities_data.json': 
                importDataIntoCollection(roomsCollection, folderPath, file)
            else:
                importDataIntoCollection(sensorsCollection, folderPath, file)

    print("Database and collections have been set up and the data has been imported successfully.")

    checkDB(db)
