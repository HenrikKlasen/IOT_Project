from coapthon.client.helperclient import HelperClient
import sys
import json
import os
from threading import Thread
import aiocoap
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'room_selection_api_db'))
from db_utils import setupMongoConnection, mergeArduinoDataInCollection

sensorsCollection = setupMongoConnection("mongodb://localhost:27017/", "db", "sensors_collection")
class SensorNode:
    def __init__(self, room_name, index):
        self.room_name = room_name
        self.room_data = None
        self.index = index

    def start(self):
        host = "127.0.0.1"
        port = 5683
        client = HelperClient(server=(host, port))
        response = client.observe(self.room_name, self.callback)
        try:
            while True:
                pass
        except KeyboardInterrupt:
            client.cancel_observing(response, True)
            client.stop()

    def callback(self, response):
        print(f"[{self.room_name}]: Notification received:")
        self.room_data = json.loads(response.payload)
        if self.room_data['data'] != 'Sensor data resource':
            self.room_data = json.loads(self.room_data['data'])
            self.room_data = json.loads(self.room_data['data'])
            print(self.room_data)
            mergeArduinoDataInCollection(sensorsCollection, self.room_data)

sensor_nodes = [
        SensorNode("Room1",  0),
        SensorNode("Room2", 1),
        SensorNode("Room3", 2)
    ]

    # Start each SensorNode in its own thread
threads = [Thread(target=node.start) for node in sensor_nodes]
for thread in threads:
    thread.start()