from machine import Pin
import time

# LED connected to GPIO 2 (common on ESP32 dev boards)
led = Pin(2, Pin.OUT)

print("Starting ESP32 Blink...")

while True:
    led.on()
    print("LED ON")
    time.sleep(0.5)
    led.off()
    print("LED OFF")
    time.sleep(0.5)
