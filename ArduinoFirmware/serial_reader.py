from pymongo import MongoClient
import serial
import sys
sys.path.append('../')
import time
from serial_parser import parse_to_json_dict, parse_to_json_string
from aiocoap import *
from coap_comms import post_sensor_data
import asyncio
import serial_asyncio
from room_selection_api_db.db_utils import mergeArduinoDataInCollection
from room_selection_api_db.setup_central_db import setupCentralDB

async def readserial(comport, baudrate, sensorsCollection, timestamp=False):
    reader, writer = await serial_asyncio.open_serial_connection(url=comport, baudrate=baudrate)

    while True:
        temp = (await reader.readline()).decode().strip()
        luminosityAnalog = (await reader.readline()).decode().strip()
        noiseAnalog = (await reader.readline()).decode().strip()
        luminosityAnalog = int(luminosityAnalog)
        if luminosityAnalog < 20:
            luminosity = 0
        elif luminosityAnalog < 50:
            luminosity = 1
        elif luminosityAnalog < 150:
            luminosity = 2
        elif luminosityAnalog < 250:
            luminosity = 3
        elif luminosityAnalog < 350:
            luminosity = 4
        elif luminosityAnalog < 450:
            luminosity = 5
        elif luminosityAnalog < 500:
            luminosity = 6
        elif luminosityAnalog < 650:
            luminosity = 7
        elif luminosityAnalog < 750:
            luminosity = 8
        elif luminosityAnalog <= 1024:
            luminosity = 9
        else: 
            luminosity = -1
            
        if timestamp:
            timestamp_str = time.strftime('%Y-%m-%dT%H:%M:%S')
            sensor_data = parse_to_json_string(parse_to_json_dict(timestamp=timestamp_str, roomID=1, temp=temp, humidity=humidity, noiseLv=noiseAnalog, lum=luminosity))
            print(sensor_data)
            mergeArduinoDataInCollection(sensorsCollection, sensor_data)
            await post_sensor_data(sensor_data.encode("utf-8"))

if __name__ == '__main__':
    client = MongoClient("mongodb://localhost:27017/")
    sensorsCollection = setupCentralDB(client)
    asyncio.run(readserial('COM4', 9600, sensorsCollection=sensorsCollection, timestamp=True))

