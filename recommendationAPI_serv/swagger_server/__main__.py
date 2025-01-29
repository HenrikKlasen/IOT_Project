#!/usr/bin/env python3

import sys
import os
import connexion

# Ensure the parent directory is in the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from swagger_server.encoder import JSONEncoder  # Ensure correct import


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json = JSONEncoder  # Correctly set the JSON encoder
    app.add_api('swagger.yaml', arguments={'title': 'Room Recommendation System'}, pythonic_params=True)
    app.run(port=8081)  # Change the port to avoid conflicts


if __name__ == '__main__':
    main()
