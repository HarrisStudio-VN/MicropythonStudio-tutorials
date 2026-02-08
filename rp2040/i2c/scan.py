from machine import Pin, I2C

# I2C0: SCL=GP9, SDA=GP8
i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=400000)

print("Scanning Pico I2C0 bus (SCL=GP9, SDA=GP8)...")
devices = i2c.scan()

if not devices:
    print("No devices found.")
else:
    print(f"Found {len(devices)} device(s):")
    for d in devices:
        print(f" - Hex: {hex(d)} (Dec: {d})")
