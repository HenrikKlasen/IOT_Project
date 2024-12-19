import os
from db_utils import dbExists, mergeInitDataInCollection
from pymongo import MongoClient

def setupCentralDB(client, folderPath):
    #create database
    db = client["db"]
    #create sensors collections to seperate the sensor types
    sensorsCollection = db['sensors_collection']

    #insert data from json files into the collections
    # for file in os.listdir(folderPath):
    #     if file.endswith('.json'):
    #         importDataIntoCollection(sensorsCollection, folderPath, file)
    
    mergeInitDataInCollection(sensorsCollection, folderPath)
    print("Database and collections have been set up and the data has been imported successfully.")
    
    # add data from teacher in db central
    

if __name__ == "__name__":
    #connect to the MongoDB server
    client = MongoClient("mongodb://localhost:27017/")
    sensorsCollection = setupCentralDB(client)
