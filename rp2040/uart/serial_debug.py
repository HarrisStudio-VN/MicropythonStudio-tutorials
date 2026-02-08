from machine import UART, Pin
import time

# UART0: TX=GP0, RX=GP1
uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

print("RP2040 UART Loopback test. Connect GP0 to GP1.")

while True:
    uart.write("DATA_FROM_PICO\n")
    if uart.any():
        rx_data = uart.read()
        print("Received:", rx_data)
    time.sleep(1)
