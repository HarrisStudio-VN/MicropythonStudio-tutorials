from machine import Pin
import time

# Built-in LED on RP2040 (Raspberry Pi Pico)
led = Pin(25, Pin.OUT)

print("Starting RP2040 Blink...")

while True:
    led.toggle()
    print("Toggled LED")
    time.sleep(0.5)
