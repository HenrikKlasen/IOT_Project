import json
def parse_to_json(timestamp: str, roomID: int, temp: float, humidity: float, tempUnit: str ="Celsius", humUnit: str= "%") -> json:
    json_string = {
        "roomID": roomID, 
        "timestamp": timestamp, 
        "sensors": {
            "roomTP": temp,
            "roomTPunit": tempUnit,
            "roomHumid": humidity,
            "roomHumidUnit": humUnit, 
            },
        }
    return json.dumps(json_string)