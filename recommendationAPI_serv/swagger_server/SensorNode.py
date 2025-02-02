from coapthon.client.helperclient import HelperClient
from swagger_server.controllers.globaldata import room_data
import json
from threading import Thread
class SensorNode:
    def __init__(self, room_name, room_data, index):
        self.room_name = room_name
        self.room_data = room_data
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
        self.room_data[self.index] = json.loads(response.payload)
        if self.room_data[self.index]['data'] != 'Sensor data resource':
            self.room_data[self.index] = json.loads(self.room_data[self.index]['data'])
            self.room_data[self.index] = json.loads(self.room_data[self.index]['data'])
            self.room_data[self.index] = self.room_data[self.index]['sensors_values']

            print(self.room_data[self.index])
            print(self.room_data)

