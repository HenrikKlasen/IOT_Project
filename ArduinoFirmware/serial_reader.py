import serial
import time


def readserial(comport, baudrate, timestamp=False):

    ser = serial.Serial(comport, baudrate, timeout=0.1)         # 1/timeout is the frequency at which the port is read

    while True:

        temp = ser.readline().decode().strip()
        humidity = ser.readline().decode().strip()

        if temp and humidity and timestamp:
            timestamp = time.strftime('%H:%M:%S')
            print(f'{timestamp} > Temp: {temp} > Humidity: {humidity}')
        elif temp and humidity:
            print(temp, humidity)


if __name__ == '__main__':
<<<<<<< HEAD
    readserial('COM3', 9600, timestamp=True)
=======
    readserial('COM3', 9600, True)
>>>>>>> 78282fb82aa1c1eddc4b5826c5879cc175054a0f
