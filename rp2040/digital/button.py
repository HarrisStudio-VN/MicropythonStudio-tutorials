from machine import Pin
import time

# Pin GP15 cho nút nhấn trên RP2040 Pico
button = Pin(15, Pin.IN, Pin.PULL_UP)
led = Pin(25, Pin.OUT)

print("Pico Button Tutorial started.")
while True:
    if button.value() == 0:  # Nút được nhấn (Low)
        led.value(1)
        print("Button Pushed!")
    else:
        led.value(0)
    time.sleep(0.1)
