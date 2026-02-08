from machine import Pin, PWM
import time

# PWM on LED pin (GPIO 2)
led_pwm = PWM(Pin(2), freq=1000)

print("Starting ESP32 PWM Fade...")

while True:
    for i in range(0, 1024):
        led_pwm.duty(i)
        time.sleep_ms(2)
    for i in range(1023, -1, -1):
        led_pwm.duty(i)
        time.sleep_ms(2)
