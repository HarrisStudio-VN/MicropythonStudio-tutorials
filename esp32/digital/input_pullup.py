from machine import Pin
import time

# Button connected to GPIO 0 (BOOT button on ESP32)
# using internal pull-up resistor
button = Pin(0, Pin.IN, Pin.PULL_UP)
led = Pin(2, Pin.OUT)

print("Starting ESP32 Input Pull-up sample...")
print("Press the BOOT button to light up the LED.")

while True:
    if button.value() == 0:  # Pressed (Logic Low)
        led.on()
    else:
        led.off()
    time.sleep(0.1)
