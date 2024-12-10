from coapthon.client.helperclient import HelperClient
import sys
sys.path.insert(0, 'C:/Users/henri/Documents/Uni.lu/Semester 5/IOT/Project/IOT_Project')
from pymongo import MongoClient
from room_selection_api_db.db_utils import mergeArduinoDataInCollection
from room_selection_api_db.setup_central_db import setupCentralDB
import json
from collections import namedtuple

def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())
def json2obj(data): return json.loads(data, object_hook=_json_object_hook)

def main(sensorsCollection):
    """
    Subscribes to CoAP server and inserts data into DB
    """
    host = "127.0.0.1"
    port = 5683
    path = "Room1"

    client = HelperClient(server=(host, port))
    response = json2obj(client.observe(path, callback))
    print(response.pretty_print())

    try:
        while True:
            pass
    except KeyboardInterrupt:
        client.cancel_observing(response, True)
        client.stop()

def callback(response):
    print("Notification received:")
    print(response.pretty_print())

if __name__ == '__main__':
    client = MongoClient("mongodb://localhost:27017/")
    sensorsCollection = setupCentralDB(client)
    main(sensorsCollection)