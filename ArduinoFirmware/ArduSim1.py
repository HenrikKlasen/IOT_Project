from serial_parser import *
from coap_comms import *
import time
import random
import asyncio

async def readserial(timestamp=False):
    """
    timestamp: Timestamp
    Summary: Reads serial, and transforms them into JSON, sends them to coap_server.
    """
    while True:
        temp = random.uniform(15, 35)
        luminosityAnalog = random.uniform(0, 1023)
        noiseAnalog = random.uniform(0, 1023)
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
            await post_sensor_data(
                parse_to_json_string(
                    parse_to_json_dict(
                        timestamp=timestamp_str, roomID=1, temp=temp, noiseLv=noiseAnalog, lum=luminosity
                        )
                    ).encode("utf-8"), room_id=1
            )
        time.sleep(30)

if __name__ == '__main__':
    asyncio.run(readserial(timestamp=True))
