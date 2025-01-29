from swagger_server.controllers.room_recommendation import RoomRecommendation
import numpy as np
from pymongo import MongoClient

ABSTRACT_RECOMMENDATION = [
  {
    "roomID": "MSA 4.070",
    "dateTimeSlotStart": "2024-12-10T14:00:00Z",
    "dateTimeSlotEnd": "2024-12-10T15:00:00Z",
    "roomMetrics": {
      "temperature": 20,
      "co2": 500,
      "humidity": 0.5,
      "voc": 0.5,
      "light": 400,
      "sound": 25
    },
    "facilities": [
      {
        "name": "Projector",
        "quantity": 1
      }
    ],
    "rank": 1
  }
]

ABSTRACT_BODY = {
  "dateTimeSlotStart": "2024-12-10T14:00:00Z",
  "dateTimeSlotEnd": "2024-12-10T15:00:00Z",
  "roomSize": {
    "min": 6,
    "max": 15
  },
  "weightedCategories": {
    "temperature_weight": 0.5,
    "co2_weight": 0.5,
    "humidity_weight": 0.5,
    "voc_weight": 0.5,
    "light_weight": 0.5,
    "sound_weight": 25
  },
  "optimalValues": {
    "temperature_opt": {
      "min": 20,
      "max": 24
    },
    "co2_opt": 450,
    "humidity_opt": 0.45,
    "voc_opt": 0.4,
    "light_opt": 500,
    "sound_opt": 30
  },
  "flexibilityValues": {
    "temperature_flexibility": 1,
    "co2_flexibility": 0,
    "humidity_flexibility": 2,
    "voc_flexibility": 3,
    "light_flexibility": 2,
    "sound_flexibility": 1
  },
  "facilityRequirements": [
    {
      "name": "Projector",
      "quantity": 1
    }
  ]
}

INVALID_BODY_ERROR = {
    "detail": "Request body is not valid JSON",
    "status": 400,
    "title": "Bad Request",
    "type": "about:blank"
}

room_rec_sys = RoomRecommendation()

def add_error_cause(error, addtional_info):
  error["additional_info"] = addtional_info
  return error

def validate_keys(dict1, dict2):
    """
    Validates that dict1 has the same keys as dict2, including nested dictionaries.
    The order of keys does not matter, but all keys in dict2 must exist in dict1.

    :param dict1: The dictionary to validate.
    :param dict2: The reference dictionary.
    :return: True if dict1 has the same keys as dict2, False otherwise.
    """
    def extract_keys(d, parent_key=''):
        """
        Written by GPT

        Recursively extract all keys from a dictionary, including nested ones,
        as a set of flattened key paths.
        """
        keys = set()
        for key, value in d.items():
            full_key = f"{parent_key}.{key}" if parent_key else key
            keys.add(full_key)
            if isinstance(value, dict):
                keys.update(extract_keys(value, full_key))
        return keys

    # Extract all keys from both dictionaries
    keys1 = extract_keys(dict1)
    keys2 = extract_keys(dict2)

    # Validate that keys1 contains all keys from keys2 and vice versa
    return keys1 == keys2

def getLatestSensorsData(collection):
    """Gets the latest sensor data for all rooms from the specified document

    Args:
        collection (MongoDB Collection): sensors collection

    Returns:
        dict: A dictionary with room names as keys and their latest sensor data as values
    """
    pipeline = [
        {"$match": {"_id": {"$oid": "67682bfaee5c63733df5b3fb"}}},
        {"$unwind": "$rooms"},
        {"$unwind": "$rooms.sensors_values"},
        {"$sort": {"rooms.sensors_values.timestamp": -1}},
        {"$group": {
            "_id": "$rooms.name",
            "latest_sensor_data": {"$first": "$rooms.sensors_values"}
        }}
    ]
    result = collection.aggregate(pipeline)
    latest_data = {doc["_id"]: doc["latest_sensor_data"] for doc in result}
    return latest_data

def recommend_rooms_post(body):  # noqa: E501
    """Recommend rooms based on user-provided weights.

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: List[Room]
    """

    approriate_body = validate_keys(body,ABSTRACT_BODY)
    
    if not approriate_body:
      error_body = add_error_cause(INVALID_BODY_ERROR,"Inapproriate Request Body")
      return error_body

    client = MongoClient('localhost', 27017)
    db = client['db']  # Replace with your database name
    collection = db['sensors_collection']  # Replace with your collection name

    latest_sensor_updates = getLatestSensorsData(collection)
    client.close()

    if not latest_sensor_updates:
        return {"detail": "No sensor data available", "status": 404, "title": "Not Found", "type": "about:blank"}

    criteria_weights = body["weightedCategories"]
    optimal_values = body["optimalValues"]
    flexibility_values = body["flexibilityValues"]

    stuff = [{k: data[k] for k in ["temperature","co2","humidity","voc","light","sound"]} for data in latest_sensor_updates.values()]
    room_rec_sys.init_score_functions(optimal_values, flexibility_values)
    room_rec_sys.init_criterion(criteria_weights)
    room_rec_sys.init_alternatives(stuff)
    room_rec_sys.finalise()
    recommendations = room_rec_sys.recommend()

    return recommendations
