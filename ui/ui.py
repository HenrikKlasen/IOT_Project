from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime
from room_selection_api_db.db_utils import setupMongoConnection, getDashboardData

app = Flask(__name__)

uri = "mongodb://localhost:27017/" 
dbName = "db"
sensorCollectionName = "sensor_collection"
sensorCollection = setupMongoConnection(uri, dbName, sensorCollectionName)
roomsCollectionName = "rooms_collection"
roomsCollection = setupMongoConnection(uri, dbName, roomsCollectionName)

@app.route('/api/dashboard_data', methods=['GET'])
def getDashboardData():
    roomId = request.args.get("roomId")
    startDateStr = request.args.get("startDate")
    endDateStr = request.args.get("endDate")
    
    startDate = datetime.strptime(startDateStr, "%Y-%m-%dT%H:%M:%S") 
    endDate = datetime.strptime(endDateStr, "%Y-%m-%dT%H:%M:%S")
    
    result = sensorCollection.aggregate([ 
            {"$match": {"rooms.name": roomId}}, 
            {"$unwind": "$rooms"}, 
            {"$unwind": "$rooms.sensors_values"}, 
            {"$match": {"rooms.name": roomId, "rooms.sensors_values.timestamp": {"$gte": startDate, "$lte": endDate}}}, 
            {"$sort": {"rooms.sensors_values.timestamp": 1}},
            {
                    "$group": {
                        "_id": "$rooms.name",
                        "data": {
                            "$push": {
                                "timestamp": "$rooms.sensors_values.timestamp",
                                "temperature": "$rooms.sensors_values.temperature",
                                "humidity": "$rooms.sensors_values.humidity",
                                "light_intensity": "$rooms.sensors_values.light_intensity",
                                "sound_level": "$rooms.sensors_values.sound_level",
                                "co2_level": "$rooms.sensors_values.co2_level",
                                "PM2.5": "$rooms.sensors_values.PM2.5",
                                "PM10":"$rooms.sensors_values.PM10",
                                "VOC_level": "$rooms.sensors_values.VOC_level"
                            }
                        }
                    }
            }
    ])
    return jsonify(list(result))

@app.route('/api/rooms', methods=['GET'])
def getRooms():
    # get all rooms, exclude _id field
    rooms = list(roomsCollection.find({}, {'_id':0}))
    return jsonify(rooms)

if __name__ == "__main__":
    app.run(debug=True)