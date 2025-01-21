# LED blink with loop

# This sketch shows how to blink an LED connected to GPIO 18 using a loop.
# 
#  Components
#  ----------
#   - ESP32
#   - 330Ohm resistor for the LED
#   - 5mm LED
#   -     Connect anode to GPIO 18
#   -     Connect cathode to GND via the resistor
#   - Wires
#   - Breadboard

from machine import Pin
from utime import sleep_ms # "utime" is an optimized subset version of the CPython time module

led = Pin(18, Pin.OUT)    # create output pin on GPIO18

while True:
    led.on()                 # set pin to "on" (high) level
    sleep_ms(500)
    led.off()                # set pin to "off" (low) level
    sleep_ms(500)
