import serial
import sys
sys.path.append('../')
import time
import serial_parser
from aiocoap import *
from coap_comms import post_sensor_data
import asyncio
import serial_asyncio
import json


async def readserial(comport, baudrate, timestamp=False):
    reader, writer = await serial_asyncio.open_serial_connection(url=comport, baudrate=baudrate)

    while True:
        temp = (await reader.readline()).decode().strip()
        humidity = (await reader.readline()).decode().strip()
        print(temp, humidity)
        if timestamp:
            timestamp_str = time.strftime('%Y/%m/%d|%H:%M:%S')
            await post_sensor_data(serial_parser.parse_to_json(timestamp=timestamp_str, roomID=1, temp=temp, humidity=humidity).encode("utf-8"))


if __name__ == '__main__':
    asyncio.run(readserial('COM3', 9600, timestamp=True))

