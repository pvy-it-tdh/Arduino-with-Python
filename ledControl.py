import tkinter as tk
import serial
import time

# Khởi tạo kết nối với Arduino
arduino = serial.Serial("COM8", 115200)  # Chọn cổng COM của Arduino và tốc độ truyền là 115200 baud
time.sleep(2)  # Đợi 2 giây để thiết lập kết nối ổn định

# Hàm để bật hoặc tắt LED
def toggle_led(state):
    if state == "ON":
        arduino.write(b'ON\n')  # Gửi lệnh "ON" cho Arduino
    elif state == "OFF":
        arduino.write(b'OFF\n')  # Gửi lệnh "OFF" cho Arduino

# Tạo giao diện người dùng
root = tk.Tk()  # Khởi tạo cửa sổ chính
root.title("Arduino LED Controller")  # Tiêu đề của cửa sổ

# Tạo nút bật LED
btn_on = tk.Button(root, text="Bật LED", command=lambda: toggle_led("ON"), width=20, height=2)
btn_on.pack(pady=10)  # Đặt nút bật LED vào cửa sổ với khoảng cách trên dưới là 10 pixel

# Tạo nút tắt LED
btn_off = tk.Button(root, text="Tắt LED", command=lambda: toggle_led("OFF"), width=20, height=2)
btn_off.pack(pady=10)  # Đặt nút tắt LED vào cửa sổ với khoảng cách trên dưới là 10 pixel

# Vòng lặp sự kiện của Tkinter để giao diện chạy
root.mainloop()

# Đóng kết nối serial khi cửa sổ bị đóng
arduino.close()
