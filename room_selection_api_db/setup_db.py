import json
import os
from pymongo import MongoClient

def setupDB(client):
    #connect to the MongoDB server
    #client = MongoClient("mongodb://localhost:27017/")
    #create database
    db = client.db
    #create collections to separate the data regarding rooms from the data regarding the sensors
    roomsCollection = db.rooms
    sensorsCollection = db.sensors

    def importDataIntoCollection(collection, folderPath, file):
        filePath = os.path.join(folderPath, file)
        with open(filePath) as f:
                data = json.load(f)
                collection.insert_many(data)

    #insert data from json files into the collections
    folderPath = './Project_sensor_data'
    for file in os.listdir(folderPath):
        if file.endswith('.json'):
            filePath = os.path.join(folderPath, file)
            if file == 'rooms_facilities_data.json': 
                importDataIntoCollection(roomsCollection, folderPath, file)
            else:
                importDataIntoCollection(sensorsCollection, folderPath, file)
    
    print("Database and collections have been set up and the data has been imported successfully.")
    
if __name__ == "__name__":
    setupDB()
