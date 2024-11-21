import serial
import time
import serial_parser
from aiocoap import *
import asyncio
import json

def readserial(comport, baudrate, timestamp=False):

    ser = serial.Serial(comport, baudrate, timeout=0.1)         # 1/timeout is the frequency at which the port is read

    while True:

        temp = ser.readline().decode().strip()
        humidity = ser.readline().decode().strip()

        timestamp = time.strftime('%Y/%m/%d|%H:%M:%S')
        asyncio.run(
            post_sensor_data(serial_parser.parse_to_json(timestamp=timestamp, roomID=1, temp=temp, humidity=humidity).encode("utf-8"))
            )
        asyncio.run(
            get_sensor_data()
        )

async def get_sensor_data():
    protocol = await Context.create_client_context()

    request = Message(code=GET, uri='coap://127.0.0.1:5683/Room1')

    try:
        response = await protocol.request(request).response
        print('Result: %s\n%r' % (response.code, response.payload))
    except Exception as e:
        print('Failed to fetch resource:')
        print(e)

async def post_sensor_data(data):
    protocol = await Context.create_client_context()

    request = Message(code=POST, uri='coap://127.0.0.1:5683/Room1', payload=data)

    try:
        response = await protocol.request(request).response
        print('Result: %s\n%r' % (response.code, response.payload))
    except Exception as e:
        print('Failed to post resource:')
        print(e)

if __name__ == '__main__':
    #print(asyncio.run(get_sensor_data()))
    readserial('COM3', 9600, timestamp=True)


