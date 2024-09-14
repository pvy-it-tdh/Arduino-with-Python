import time

import serial
DataSerial = serial.Serial('COM8', 115200)
time.sleep(1)

while True:

    data = input("Vui long nhap lenh dieu khien: ")
    data = data + '\r'
    # Mã hóa chuỗi
    DataSerial.write(data.encode())


