import machine
import dht
import time

# ESP32 DHT11 Sensor reading
# Connect DHT11 to Pin 4
sensor = dht.DHT11(machine.Pin(4))

while True:
    try:
        time.sleep(2)
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        print(f"Temperature: {temp}C, Humidity: {hum}%")
    except OSError as e:
        print("Failed to read sensor.")
