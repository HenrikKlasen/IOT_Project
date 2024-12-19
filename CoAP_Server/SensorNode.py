from coapthon.client.helperclient import HelperClient
from room_selection_api_db.db_utils import setupMongoConnection, mergeArduinoDataInCollection

def main():
    host = "127.0.0.1"
    port = 5683
    path = "Room1"
    
    sensorsCollection = setupMongoConnection("mongodb://localhost:27017/", "db", "sensors_collection")

    client = HelperClient(server=(host, port))
    response = client.observe(path, callback)
    print(response.pretty_print())

    try:
        while True:
            pass
    except KeyboardInterrupt:
        client.cancel_observing(response, True)
        client.stop()

def callback(response, sensorsCollection):
    print("Notification received:")
    print(response.pretty_print())
    mergeArduinoDataInCollection(sensorsCollection, response)

if __name__ == '__main__':
    main()