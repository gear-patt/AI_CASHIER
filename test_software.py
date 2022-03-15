import serial
import time


serialcomm = serial.Serial('/dev/cu.usbmodem14401', 9600)  # tf are ports really?
serialcomm.timeout = 1  # huh?

while True:
    i = input("input: ").strip()
    if i == 'done':
        print('finished program')
        break
    serialcomm.write(i.encode())
    time.sleep(0.5)
    print(serialcomm.readline().decode('ascii'))

serialcomm.close()
