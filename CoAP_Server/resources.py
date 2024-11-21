
from coapthon.resources.resource import Resource
import json

class SensorResource(Resource):
    def __init__(self, name="SensorResource", coap_server=None):
        super(SensorResource, self).__init__(name, coap_server, visible=True, observable=True, allow_children=True)
        self.payload = "Sensor data resource"

    def render_GET(self, request):
        response_payload = {
            "status": "success",
            "data": self.payload
        }
        self.payload = json.dumps(response_payload)
        return self

    def render_POST(self, request):
        try:
            data = json.loads(request.payload)
            self.payload = data
            response_payload = {
                "status": "success",
                "message": "Data received",
                "data": request.payload
            }
        except json.JSONDecodeError:
            response_payload = {
                "status": "error",
                "message": "Invalid JSON"
            }
        self.payload = json.dumps(response_payload)
        return self
    
class SimpleResource(Resource):
    def __init__(self, name="SimpleResource", coap_server=None):
        super(SimpleResource, self).__init__(name, coap_server, visible=True, observable=True, allow_children=True)
        self.payload = "Hello, CoAP!"

    def render_GET(self, request):
        return self

    def render_POST(self, request):
        self.payload = request.payload
        return self