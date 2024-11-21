from coapthon.client.helperclient import HelperClient

def main():
    host = "127.0.0.1"
    port = 5683
    path = "Room1"

    client = HelperClient(server=(host, port))
    response = client.observe(path, callback)
    print(response.pretty_print())

    try:
        while True:
            pass
    except KeyboardInterrupt:
        client.cancel_observing(response, True)
        client.stop()

def callback(response):
    print("Notification received:")
    print(response.pretty_print())

if __name__ == '__main__':
    main()