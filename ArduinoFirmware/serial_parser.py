import json
def parse_to_json(timestamp: str, roomID: int, temp: float, humidity: float, lum: float, noiseLv: float, tempUnit: str ="Celsius", humUnit: str= "%", lumUnit: str="Lux", noiseLvUnit:str= "dB") -> json:
    json_string = {
        "roomID": roomID, 
        "timestamp": timestamp, 
        "sensors": {
            "roomTP": temp,
            "roomTPunit": tempUnit,
            "roomHumid": humidity,
            "roomHumidUnit": humUnit, 
            "roomLuminosity": lum,
            "roomLuminosityUnit": lumUnit,
            "roomNoise": noiseLv,
            "roomNoiseUnit": noiseLvUnit,
            },
        }
    return json.dumps(json_string)