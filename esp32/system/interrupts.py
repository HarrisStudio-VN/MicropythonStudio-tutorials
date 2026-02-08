from machine import Pin
import time

led = Pin(2, Pin.OUT)
button = Pin(0, Pin.IN, Pin.PULL_UP)

def handle_interrupt(pin):
    print("Button Pressed! Interrupt Triggered.")
    led.value(not led.value())

# Ngắt khi nhấn nút (FALLING edge)
button.irq(trigger=Pin.IRQ_FALLING, handler=handle_interrupt)

print("Interrupt Tutorial. Press EN/Boot button (GPIO 0) to toggle LED.")
while True:
    time.sleep(1)
