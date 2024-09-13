import time

import serial

DataSerial = serial.Serial('COM6', 115200)
time.sleep(1)

while True:
    while DataSerial.inWaiting() == 0:
        pass
    # Đọc dữ liệu từ Arduino
    data = DataSerial.readline()
    data = str(data, 'utf-8')
    data = data.strip('\r\n')
    print(data)
