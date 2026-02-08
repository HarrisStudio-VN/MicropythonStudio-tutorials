from machine import Pin, PWM
import time

# Servo Pin (D18 cho ESP32)
servo = PWM(Pin(18), freq=50)

def set_angle(angle):
    # Map 0-180 degree to 20-120 duty (approx)
    # Tùy loại servo có thể cần điều chỉnh
    duty = int((angle / 180 * 100) + 20)
    servo.duty(duty)

print("Sweeping Servo...")
for i in range(0, 181, 10):
    set_angle(i)
    time.sleep(0.3)
for i in range(180, -1, -10):
    set_angle(i)
    time.sleep(0.3)
