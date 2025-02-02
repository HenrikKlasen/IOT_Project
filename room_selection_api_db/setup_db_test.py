import json
import os
from pymongo import MongoClient
from check_db import checkDB
from setup_central_db import setupCentralDB
from setup_external_db import setupExternalDB

if __name__ == "__main__":
    #connect to the MongoDB server with MongoDB URI format
    client = MongoClient("mongodb://localhost:27017/")
    #create database
    db = client.db
    
    #create collections to separate the data regarding rooms from the data regarding the sensors
    original_path = os.getcwd()
    os.chdir(original_path+"\\room_selection_api_db\\Project_sensor_data\\room_facilities_data")
    externalDbPath = os.getcwd()
    setupExternalDB(client, externalDbPath)
    os.chdir(original_path+"\\room_selection_api_db\\Project_sensor_data\\sensors_data")
    centralDbPath = os.getcwd()
    setupCentralDB(client, centralDbPath)

    print("Database and collections have been set up and the data has been imported successfully.")

    checkDB(db)
