from machine import Pin, I2C

# Khởi tạo I2C trên ESP32 (SCL=22, SDA=21 là mặc định)
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)

print("Scanning I2C bus...")
devices = i2c.scan()

if len(devices) == 0:
    print("No I2C device found!")
else:
    print("I2C devices found:", len(devices))
    for device in devices:
        print("Address: ", hex(device))
