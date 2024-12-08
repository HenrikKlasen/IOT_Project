import os
from pymongo import MongoClient
from db_utils import importDataIntoCollection

def setupExternalDB(client):
    #connect to the MongoDB server
    client = MongoClient("mongodb://localhost:27017/")
    #create database
    db = client["external_db"]
    #create collections to separate the data regarding rooms from the data regarding the sensors
    roomsCollection = db["rooms_collection"]

    #insert data from json files into the collections
    folderPath = './Project_sensor_data/room_facilities_data'
    for file in os.listdir(folderPath):
        if file.endswith('.json'):
            importDataIntoCollection(roomsCollection, folderPath, file)
    
    print("Database and collections have been set up and the data has been imported successfully.")
    
if __name__ == "__name__":
    setupExternalDB()
