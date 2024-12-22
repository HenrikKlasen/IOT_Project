import os
import sys
from pymongo import MongoClient
from db_utils import importDataIntoCollection, dbExists
import json

def setupExternalDB(client, folderPath):
    """Connects to the MongoDB server and sets up the database and collections for the external database.

    Args:
        client (_type_): MongoDB client
        folderPath (_type_): Path to the folder containing the JSON files with the data to be imported into the database
    """
    #connect to the MongoDB server
    
    #create database
    db = client["db"]
    #create collections to separate the data regarding rooms from the data regarding the sensors
    roomsCollection = db["rooms_collection"]

    #insert data from json files into the collections
    print(os.listdir(folderPath))
    for file in os.listdir(folderPath):
        if file.endswith('.json'):
            importDataIntoCollection(roomsCollection, folderPath, file)
    print("Database and collections have been set up and the data has been imported successfully.")
    
if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017/")
    print(client)
    setupExternalDB(client, os.getcwd()+"\\room_selection_api_db\\Project_sensor_data\\room_facilities_data")
