from aiocoap import *
import asyncio
import json

async def get_sensor_data():
    """
    Retrieve the data from the CoAP server.
    """
    protocol = await Context.create_client_context()

    request = Message(code=GET, uri='coap://127.0.0.1:5683/Room1')

    try:
        response = await protocol.request(request).response
        print('Result: %s\n%r' % (response.code, response.payload))
    except Exception as e:
        print('Failed to fetch resource:')
        print(e)

async def post_sensor_data(data, room_id=1):
    """Post the data to the CoAP server.

    Args:
        data (_type_): Sensor data to be posted
        room_id (int, optional): room number. Defaults to 1.
    """
    protocol = await Context.create_client_context()

    request = Message(code=POST, uri=f'coap://127.0.0.1:5683/Room{room_id}', payload=data)

    try:
        response = await protocol.request(request).response
        print(f"Successful! Data is published")
    except Exception as e:
        print('Failed to post resource:')
        print(e)
