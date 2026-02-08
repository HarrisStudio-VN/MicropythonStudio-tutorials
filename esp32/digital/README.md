# ESP32 - Digital IO Basic

## Objective
Learn how to control digital outputs (LED) and read digital inputs (Button).

## Wiring Table
| Component | ESP32 Pin |
|-----------|-----------|
| Built-in LED | GPIO 2 |
| BOOT Button | GPIO 0 |

## How to run
1. Open `blink.py` and click **Run**.
2. Open `input_pullup.py`, click **Run**, and press the BOOT button.

## Notes
- GPIO 2 is the default LED for many ESP32 boards.
- BOOT button is usually active-low (connected to GND when pressed).
