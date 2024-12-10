import serial
import sys
sys.path.append('../')
import time
import serial_parser
from aiocoap import *
from coap_comms import post_sensor_data
import asyncio
import serial_asyncio

async def readserial(comport, baudrate, timestamp=False):
    reader, writer = await serial_asyncio.open_serial_connection(url=comport, baudrate=baudrate)

    while True:
        temp = (await reader.readline()).decode().strip()
        #humidity = (await reader.readline()).decode().strip()
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
        
        print(temp)
        if timestamp:
            timestamp_str = time.strftime('%Y/%m/%d|%H:%M:%S')
            await post_sensor_data(serial_parser.parse_to_json(timestamp=timestamp_str, roomID=1, temp=temp, noiseLv=noiseAnalog, lum=luminosity).encode("utf-8"))


if __name__ == '__main__':
    asyncio.run(readserial('COM3', 9600, timestamp=True))

