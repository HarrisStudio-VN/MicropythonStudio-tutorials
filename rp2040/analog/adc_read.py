from machine import ADC, Pin
import time

# RP2040 có 3 kênh ADC: 26, 27, 28
adc = ADC(Pin(26))

print("RP2040 Analog Read (GP26)")
while True:
    val = adc.read_u16() # 0 - 65535
    voltage = (val / 65535) * 3.3
    print(f"ADC Value: {val} | Voltage: {voltage:.2f}V")
    time.sleep(0.5)
