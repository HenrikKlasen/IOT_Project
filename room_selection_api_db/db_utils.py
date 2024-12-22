# this file contains methods that are used across multiple python files
# it avoids redundancy in code

from collections import defaultdict
import json
import os
from pymongo import MongoClient

def setupMongoConnection(uri, db, collection):
        client = MongoClient(uri)
        dbName = client[db]
        collectionName = dbName[collection]
        return collectionName

def dbExists(client):
# Connect to MongoDB
        client = client

        # List all databases
        databases = client.list_database_names()

        # Check if the database exists
        database_name = 'db'
        if database_name in databases:
                print(f"Database '{database_name}' exists.")
        
        # Access the database
                db = client[database_name]
        
        # List all collections in the database
                collections = db.list_collection_names()
                if collections:
                        print(f"Database '{database_name}' is not empty. Collections: {collections}")
                
                # Check if collections contain any documents
                        for collection_name in collections:
                                collection = db[collection_name]
                                document = collection.find_one()
                                if document:
                                        print(f"Collection '{collection_name}' contains documents.")
                                        result = collection.delete_many({})
                                        print(f"Deleting the documents {result.deleted_count()}")
                                else:
                                        print(f"Collection '{collection_name}' is empty.")
                else:
                        print(f"Database '{database_name}' has no collections.")
        else:
                print(f"Database '{database_name}' does not exist.")

def importDataIntoCollection(collection, folderPath, file):
        filePath = f"{folderPath}\\{file}"
        with open(filePath) as f:
                data = json.load(f)
                if isinstance(data, list):
                        for document in data:
                                collection.insert_one(document)
                else:
                        collection.insert_one(data)

# def checkAndInsertDocument(collection, document):
#         timestamp = 'timestamp'
#         existingDocument = collection.find_one({timestamp: document[timestamp]})
#         if not existingDocument: 
#                 collection.insert_one(document) 
#         else: 
#                 # Optionally update the existing document if needed 
#                 collection.update_one( 
#                         {timestamp: document[timestamp]}, 
#                         {"$set": document}
#                 )
                
#collection = roomData collection
def mergeInitDataInCollection(collection, folderPath):
        roomData = defaultdict(list)
        sensorsList = ['light_intensity_values', 'sound_values', 'air_quality_values', 'co2_values', 'humidity_values', 'temperature_values', 'voc_values']
        for fileName in os.listdir(folderPath):
                if fileName.endswith(".json"):
                        filePath = os.path.join(folderPath, fileName)
                        with open(filePath, 'r') as f:
                                data = json.load(f)
                                # merge new data with existing data
                                for room in data['rooms']:
                                        roomId = room['name']
                                        for valueType in sensorsList:
                                                if valueType in room: 
                                                        room['sensors_values'] = room.pop(valueType) 
                                        sensorData = room['sensors_values']
                                        roomData[roomId].extend(sensorData)
        # transform merged data
        for roomId, sensorList in roomData.items():
                groupedSensors = {}
                for sensor in sensorList:
                        timestamp = sensor["timestamp"]
                        if timestamp not in groupedSensors:
                                groupedSensors[timestamp] = {}
                        groupedSensors[timestamp].update(sensor)
                # convert grouped data to a list of dictionaries
                sensorsValues = []
                for timestamp, values in groupedSensors.items():
                        sensorEntry = {'timestamp': timestamp}
                        sensorEntry.update(values)
                        sensorsValues.append(sensorEntry)
                # sort the list by timestamp
                sensorsValues = sorted(sensorsValues, key=lambda x: x['timestamp'])
                
                # check for existing documents in MongoDB
                existingDocument = collection.find_one({"name": roomId})
                if existingDocument:
                        # Merge new sensor values with existing sensor values 
                        existingSensors = existingDocument.get('sensors_values', []) 
                        existingTimestamps = {sensor['timestamp'] for sensor in existingSensors} 
                        newSensors = [sensor for sensor in sensorsValues if sensor['timestamp'] not in existingTimestamps] 
                        updatedSensorsValues = existingSensors + newSensors 
                        collection.update_one( 
                                {"name": roomId}, 
                                {"$set": {"sensors_values": updatedSensorsValues}} 
                        ) 
                else: 
                        # Insert new document if it does not exist 
                        document = { 
                                "name": roomId, 
                                "sensors_values": sensorsValues 
                        }
        print("Data merging and insertion into db completed")

def mergeArduinoDataInCollection(collection, arduinoData):
        roomId = arduinoData['name']
        timestamp = arduinoData['timestamp']
        sensorsValues = arduinoData['sensors_values']
        
        # retrieve full data to ensure that there are no missing attributes
        sensorsValuesDetails = {
                "timestamp": timestamp,
                "temperature": sensorsValues.get("temperature"),
                "humidity": sensorsValues.get("humidity"),
                "light_intensity": sensorsValues.get("light_intensity"),
                "sound_level": sensorsValues.get("sound_level"),
                "co2_level": sensorsValues.get("co2_level"),
                "PM2.5": sensorsValues.get("PM2.5"),
                "PM10": sensorsValues.get("PM10"),
                "VOC_level": sensorsValues.get("VOC_level")
        }
        
        # check if a document with the room already exists
        existing_room = collection.find_one({"rooms.name": roomId})
        
        if existing_room:
                # update the existing document with new timestamp and sensor values
                collection.update_one(
                        {"rooms.name": roomId},
                        {"$push": {
                                "rooms.$.sensors_values": sensorsValuesDetails
                        }}
                )
        else:
                # insert new room with the sensor data
                newRoom = {
                        "name": roomId,
                        "sensors_values": [sensorsValuesDetails]
                }
                collection.update_one(
                {}, 
                {"$push": {"rooms": newRoom}},
                upsert=True
                )
        print("Data merging and insertion into db completed")
        
def getLatestSensorsData(collection, roomId):
        """Gets last data added to the db for a specified room number

        Args:
            collection (MongoDB Collection): sensors collection
            roomId: room number

        Returns:
            result list with the latest sensors data for room number roomId
        """
        result = collection.aggregate([
                {"$match": {"name": roomId}},
                {"$unwind": "$sensors_values"},
                {"$sort": {"sensors_values.timestamp": -1}}, 
                {"$limit": 1} 
        ]) 
        resultList = list(result)
        return resultList if resultList else None

# Function to get data in a date range 
def getSensorsDataInDateRange(collection, roomId, startDate, endDate): 
        result = collection.aggregate([ 
                {"$match": {"name": roomId}},
                {"$unwind": "$sensors_values"}, 
                {"$match": {"sensors_values.timestamp": {"$gte": startDate, "$lte": endDate}}}, 
                {"$sort": {"rooms.sensors_values.timestamp": 1}} 
        ]) 
        return list(result)