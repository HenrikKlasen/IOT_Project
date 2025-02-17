import os
from db_utils import dbExists, mergeInitDataInCollection, importDataIntoCollection
from pymongo import MongoClient

def setupCentralDB(client, folderPath):
    #create database
    db = client["db"]
    #create sensors collections to seperate the sensor types
    sensorsCollection = db['sensors_collection']
    print("Hello")
    #insert data from json files into the collections
    print(os.listdir(folderPath))
    for file in os.listdir(folderPath):
        if file.endswith('.json'):
            importDataIntoCollection(sensorsCollection, folderPath, file)
    
    mergeInitDataInCollection(sensorsCollection, folderPath)
    print("Database and collections have been set up and the data has been imported successfully.")
    
    # add data from teacher in db central
    

if __name__ == "__main__":
    #connect to the MongoDB server
    client = MongoClient("mongodb://localhost:27017/")
    sensorsCollection = setupCentralDB(client, os.getcwd()+"\\room_selection_api_db\\Project_sensor_data\\sensors_data")
