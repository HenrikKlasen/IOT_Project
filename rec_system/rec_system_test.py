from pymongo import MongoClient 
from datetime import datetime
from room_selection_api_db.db_utils import setupMongoConnection, getLatestSensorsData, getSensorsDataInDateRange
from ahp import *

# Setup MongoDB connection 
uri = "mongodb://localhost:27017/" 
db_name = "central_db" 
collection_name = "sensor_collection"
collection = setupMongoConnection(uri, db_name, collection_name)

roomIds = [1, 2, 3]
rooms = []
startDate_str = "2024-12-08T14:00:00"
endDate_str = "2024-12-08T16:00:00" 
startDate = datetime.strptime(startDate_str, "%Y-%m-%dT%H:%M:%S") 
endDate = datetime.strptime(endDate_str, "%Y-%m-%dT%H:%M:%S")

# with latest data
for roomId in roomIds:
    latestData = getLatestSensorsData(collection, roomId)
    if latestData:
        sensorsValues = latestData["rooms"]["sensors_values"]
        for value in sensorsValues:
            rooms.append({
                "temperature": value.get("temperature"),
                "humidity": value.get("humidity"),
                "light_intensity": value.get("light_intensity"),
                "sound_level": value.get("sound_level"),
                "co2_level": value.get("co2_level"),
                "PM2.5": value.get("PM2.5"),
                "PM10": value.get("PM10"),
                "VOC_level": value.get("VOC_level")
            })

# with date range
for roomId in roomIds:
    dataInRange = getSensorsDataInDateRange(collection, roomId, startDate, endDate)
    for sensorsValues in dataInRange:
        value = sensorsValues["rooms"]["sensors_values"]
        rooms.append({
            "temperature": value.get("temperature"),
            "humidity": value.get("humidity"),
            "light_intensity": value.get("light_intensity"),
            "sound_level": value.get("sound_level"),
            "co2_level": value.get("co2_level"),
            "PM2.5": value.get("PM2.5"),
            "PM10": value.get("PM10"),
            "VOC_level": value.get("VOC_level")
        })

print("Data on the 3 rooms (retrieved from MongoDB):")
[print(r) for r in rooms]

c1 = Criterion("temperature",0.5, lambda x:x)
c2 = Criterion("humidity",0.5, lambda x:x)
c3 = Criterion("Co2",0.5, lambda x:x)
c4 = Criterion("RoomFeel",0.5, lambda x:x)
criterions = [c1,c2,c3]

alt = Alternatives(rooms,criterions)

print("\nHow the hirarchy looks like:")
g = Goal("Best Room",alt)
g.add_criterion(c4)
g.add_criterion(c1,"RoomFeel")
g.add_criterion(c2,"RoomFeel")
g.add_criterion(c3)
g.add_alt_to_leafs()
g.printTree()

g.compute_criterion_priorities()
decision_data = g.make_decision()
print("\nScores of all 3 rooms:", decision_data)
print("Check that 3 vals sum up to 1:", np.sum(decision_data))