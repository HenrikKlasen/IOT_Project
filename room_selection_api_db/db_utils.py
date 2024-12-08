# this file contains methods that are used across multiple python files
# it avoids redundancy in code

from collections import defaultdict
import json
import os

def importDataIntoCollection(collection, folderPath, file):
        filePath = os.path.join(folderPath, file)
        with open(filePath) as f:
                data = json.load(f)
                collection.insert_many(data)

#collection = roomData collection
def mergeDataInCollection(collection, folderPath):
        roomData = defaultdict(list)
        # loop through all sensors file in the directory
        for fileName in os.listdir(folderPath):
                if fileName.endswith(".json"):
                        filePath = os.path.join(folderPath, fileName)
                        with open(filePath, 'r') as f:
                                data = json.load(f)
                                # merge new data with existing data
                                for room in data['rooms']:
                                        roomId = room['name']
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
                # insert or update document in MongoDB
                document = {
                        "name": roomId,
                        "sensors_values": sensorsValues
                }
                collection.update_one(
                        {"name": roomId},
                        {"$set": document},
                        upsert=True
                )
        print("Data merging and insertion into db completed")