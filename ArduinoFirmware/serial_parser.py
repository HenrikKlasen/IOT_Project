import json
def parse_to_json(timestamp: str, roomID: int, temp: float, lum: float, noiseLv: float, tempUnit: str ="Celsius", lumUnit: str="Lux", noiseLvUnit:str= "dB") -> json:
    json_string = {
        "roomID": roomID, 
        "timestamp": timestamp, 
        "sensors": {
            "roomTP": temp,
            "roomTPunit": tempUnit,
            "roomLuminosity": lum,
            "roomLuminosityUnit": lumUnit,
            "roomNoise": noiseLv,
            "roomNoiseUnit": noiseLvUnit,
            },
        }
    return json.dumps(json_string)