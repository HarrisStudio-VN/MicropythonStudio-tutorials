from machine import Pin, PWM
import time

# Pin GP25 (Onboard LED)
pwm = PWM(Pin(25))
pwm.freq(1000)

print("Pico LED Breathing...")
while True:
    for duty in range(0, 65535, 1000):
        pwm.duty_u16(duty)
        time.sleep(0.01)
    for duty in range(65535, 0, -1000):
        pwm.duty_u16(duty)
        time.sleep(0.01)
