import _thread
import time
from machine import Pin

# Dual Core - RP2040 specific
led = Pin(25, Pin.OUT)

def core1_task():
    while True:
        led.toggle()
        print("Core 1: Toggling LED")
        time.sleep(0.5)

_thread.start_new_thread(core1_task, ())

while True:
    print("Core 0: Hello from main loop")
    time.sleep(1)
