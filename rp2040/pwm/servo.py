from machine import Pin, PWM
import time

# GP16 for Servo
servo = PWM(Pin(16))
servo.freq(50)

def set_servo_angle(angle):
    # RP2040 PWM use duty_u16 (0-65535)
    # 50Hz = 20ms period
    # 0.5ms (0 deg) to 2.5ms (180 deg) pulse
    # 0.5ms/20ms * 65535 = 1638
    # 2.5ms/20ms * 65535 = 8192
    min_duty = 1638
    max_duty = 8192
    duty = int(min_duty + (max_duty - min_duty) * (angle / 180))
    servo.duty_u16(duty)

print("RP2040 Servo Control started.")
while True:
    for a in range(0, 181, 45):
        set_servo_angle(a)
        print("Angle:", a)
        time.sleep(1)
