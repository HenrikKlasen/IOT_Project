import json
def parse_to_json_dict(timestamp: str, roomID: int, temp: float = None, humidity: float = None, lum: float = None, noiseLv: float = None, co2: float = None, airPM2_5: float = None, airPM10: float = None, voc: float = None) -> dict:
    """Parses arduino sensors data to json dictionary
    All parameters are set to None for data consistency in cases where some data is not available through the sensors
    
    Args:
        timestamp (str): Time when data is caught from Arduino sensors
        roomID (int): Room number
        temp (float, optional):Temperature value in °C. Defaults to None.
        humidity (float, optional): Humidity value in %. Defaults to None.
        lum (float, optional): Light intesity value in cd. Defaults to None.
        noiseLv (float, optional): Sound level value in dB. Defaults to None.
        co2 (float, optional): Air quality CO2 level in ppm. Defaults to None.
        airPM2_5 (float, optional): Air quality PM 2.5 in ppm. Defaults to None.
        airPM10 (float, optional): Air quality PM 10 in ppm. Defaults to None.
        voc (float, optional): Air quality VOC level in ppm. Defaults to None.

    Returns:
        dict: dictionary with sensors data
    """
    json_data = {
        "name": roomID, 
        "timestamp": timestamp, 
        "sensors_values": {
            "temperature": temp,
            "humidity": humidity,
            "light_intensity": lum,
            "sound_level": noiseLv,
            "co2_level": co2,
            "PM2.5": airPM2_5,
            "PM10": airPM10,
            "VOC_level": voc
        }
    }
    return json_data

def parse_to_json_string(data: dict) -> json:
    return json.dumps(data)