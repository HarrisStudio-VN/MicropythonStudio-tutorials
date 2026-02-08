from machine import Pin
import rp2
import time

# PIO Blink - RP2040 specific
@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
def blink():
    wrap_target()
    set(pins, 1)   [31]
    nop()          [31]
    nop()          [31]
    nop()          [31]
    nop()          [31]
    set(pins, 0)   [31]
    nop()          [31]
    nop()          [31]
    nop()          [31]
    nop()          [31]
    wrap()

# Instantiate state machine 0 on Pin 25 (LED) at 2000Hz
sm = rp2.StateMachine(0, blink, freq=2000, set_base=Pin(25))
sm.active(1)
print("PIO Blinking active!")
