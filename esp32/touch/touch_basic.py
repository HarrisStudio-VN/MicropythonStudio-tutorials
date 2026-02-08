from machine import TouchPad, Pin
import time

# ESP32 có các chân Touch: 0, 2, 4, 12, 13, 14, 15, 27, 32, 33
t = TouchPad(Pin(14))

print("Touch Sensor Debug. Value decreases when touched.")
while True:
    val = t.read()
    print("Touch Value:", val)
    time.sleep(0.5)
