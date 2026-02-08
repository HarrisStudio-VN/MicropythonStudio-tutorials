from machine import Pin, ADC
import time

# Analog input on GPIO 34
adc = ADC(Pin(34))
adc.atten(ADC.ATTN_11DB)  # Full range: 3.3V

print("Starting ESP32 ADC Read...")

while True:
    val = adc.read()
    print("ADC Value:", val)
    time.sleep(0.5)
