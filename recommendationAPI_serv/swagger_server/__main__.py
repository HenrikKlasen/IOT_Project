
import os
import connexion
from flask_cors import CORS
import sys
from threading import Thread
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from swagger_server.controllers.globaldata import room_data
from swagger_server.encoder import JSONEncoder  # Ensure correct import
from swagger_server.SensorNode import SensorNode



def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = JSONEncoder  # Correctly set the JSON encoder
    app.add_api('swagger.yaml', arguments={'title': 'Room Recommendation System'}, pythonic_params=True)

    # Create SensorNode instances for each room
    sensor_nodes = [
        SensorNode("Room1", room_data, 0),
        SensorNode("Room2", room_data, 1),
        SensorNode("Room3", room_data, 2)
    ]

    # Start each SensorNode in its own thread
    threads = [Thread(target=node.start) for node in sensor_nodes]
    for thread in threads:
        thread.start()

    CORS(app.app)
    app.run(port=8081)  # Change the port to avoid conflicts

if __name__ == '__main__':
    main()