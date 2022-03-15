import serial
import sys
import time
arduino = serial.Serial('/dev/cu.usbmodem141101', 9600, timeout=10)
string = 'hello'
try:
    arduino.write(string.encode())
    arduino.flush()
except OsError:
    print("Write failed!")
arduino.close()
