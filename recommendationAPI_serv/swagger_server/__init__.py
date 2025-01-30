from swagger_server import SensorNode, SensorNode2, SensorNode3
from threading import Thread

def __init__():
    s1 = Thread(target=SensorNode.main)
    s2 = Thread(target=SensorNode2.main)
    s3 = Thread(target=SensorNode2.main)
    s1.start()
    s2.start()
    s3.start()
