import os
import sys
sys.path.insert(0, "C:/Users/henri/Documents/Uni.lu/Semester 5/IOT/Project/IOT_Project")
from room_selection_api_db.db_utils import importDataIntoCollection, mergeInitDataInCollection, mergeArduinoDataInCollection
from pymongo import MongoClient

def setupCentralDB(client):
    #create database
    db = client['central_db']
    #create sensors collections to seperate the sensor types
    sensorsCollection = db['sensor_collection']

    #insert data from json files into the collections
    folderPath = "C:/Users/henri/Documents/Uni.lu/Semester 5/IOT/Project/IOT_Project/room_selection_api_db/Project_sensor_data/sensors_data"
    sys.path.insert(0, folderPath)
    for file in os.listdir(folderPath):
        if file.endswith('.json'):
            importDataIntoCollection(sensorsCollection, folderPath, file)
    
    print("Database and collections have been set up and the data has been imported successfully.")
    
    # add data from teacher in db central
    mergeInitDataInCollection(sensorsCollection, folderPath)

if __name__ == "__name__":
    #connect to the MongoDB server
    client = MongoClient("mongodb://localhost:27017/")
    sensorsCollection = setupCentralDB(client)
