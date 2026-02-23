import bluetooth
import time
from ble_simple_peripheral import BLESimplePeripheral

# Initialize BLE
ble = bluetooth.BLE()
sp = BLESimplePeripheral(ble, name="MicroPython_Gamepad")

def on_rx(data):
    # Decode command from dashboard
    # Commands: 'U' (Up), 'D' (Down), 'L' (Left), 'R' (Right), 'A', 'B'
    command = data.decode().strip()
    print("Received Gamepad Command:", command)
    
    if command == 'U':
        print("Action: MOVE FORWARD")
    elif command == 'D':
        print("Action: MOVE BACKWARD")
    elif command == 'L':
        print("Action: TURN LEFT")
    elif command == 'R':
        print("Action: TURN RIGHT")
    elif command == 'A':
        print("Action: JUMP / FIRE")
    elif command == 'B':
        print("Action: SPECIAL ATK")

sp.on_write(on_rx)

print("BLE Gamepad ready. Connect using your phone or IDE Dashboard!")
while True:
    if sp.is_connected():
        # Do something periodically if needed
        pass
    time.sleep_ms(100)
