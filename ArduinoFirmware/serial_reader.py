import serial
import time
import serial_parser


def readserial(comport, baudrate, timestamp=False):

    ser = serial.Serial(comport, baudrate, timeout=0.1)         # 1/timeout is the frequency at which the port is read

    while True:

        temp = ser.readline().decode().strip()
        humidity = ser.readline().decode().strip()

        if temp and humidity and timestamp:
            timestamp = time.strftime('%H:%M:%S')
            print(serial_parser.parse_to_json(timestamp=timestamp, roomID=1, temp=temp, humidity=humidity))


if __name__ == '__main__':
    readserial('COM3', 9600, timestamp=True)
