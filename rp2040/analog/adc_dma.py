from machine import ADC, Pin
import time

adc = ADC(Pin(26))

print("RP2040 High Speed ADC Polling (Simple intro to fast read)")

samples = 100
data = [0] * samples

start = time.ticks_us()

# Thu thập 100 mẫu nhanh nhất có thể
for i in range(samples):
    data[i] = adc.read_u16()

end = time.ticks_us()

print(f"Collected {samples} samples in {time.ticks_diff(end, start)} uS")
print("First 10 values:", data[:10])
