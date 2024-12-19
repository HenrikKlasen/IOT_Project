from aiocoap import *
import asyncio
import json

async def get_sensor_data():
    protocol = await Context.create_client_context()

    request = Message(code=GET, uri='coap://127.0.0.1:5683/Room_1')

    try:
        response = await protocol.request(request).response
        print('Result: %s\n%r' % (response.code, response.payload))
    except Exception as e:
        print('Failed to fetch resource:')
        print(e)

async def post_sensor_data(data):
    protocol = await Context.create_client_context()

    request = Message(code=POST, uri='coap://127.0.0.1:5683/Room_1', payload=data)

    try:
        response = await protocol.request(request).response
        print(f"Successful! Data is published")
    except Exception as e:
        print('Failed to post resource:')
        print(e)
