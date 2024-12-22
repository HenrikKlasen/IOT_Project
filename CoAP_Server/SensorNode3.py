from coapthon.client.helperclient import HelperClient
import sys
import json
import os
import aiocoap
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'room_selection_api_db'))
from db_utils import setupMongoConnection, mergeArduinoDataInCollection

sensorsCollection = setupMongoConnection("mongodb://localhost:27017/", "db", "sensors_collection")
def main():
    """Main function to start the CoAP client.
    """
    host = "127.0.0.1"
    port = 5683
    path = "Room3"


    client = HelperClient(server=(host, port))
    response = client.observe(path, callback)
    try:
        while True:
            pass
    except KeyboardInterrupt:
        client.cancel_observing(response, True)
        client.stop()

def callback(response):
    global sensorsCollection
    print("Notification received:")
    response = json.loads(response.payload.encode('utf-8'))
    response = json.loads(response['data'])
    response = json.loads(response['data'])
    print(response)
    mergeArduinoDataInCollection(sensorsCollection, response)

if __name__ == '__main__':
    main()