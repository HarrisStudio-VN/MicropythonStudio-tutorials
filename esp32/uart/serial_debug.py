from machine import UART
import time

# Khởi tạo UART1 với baudrate 115200
# TX=17, RX=16 (tùy mạch có thể khác)
uart = UART(1, baudrate=115200, tx=17, rx=16)

print("UART Debug Started. Type something in Serial Terminal...")

while True:
    uart.write("Hello from ESP32 UART\n")
    if uart.any():
        data = uart.read()
        print("Received:", data)
    time.sleep(2)
