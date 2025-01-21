'''
 LED fade

 This sketch shows how to control an LED connected to GPIO 21 using Pulse Width Modulation.

 Components
 ----------
  - ESP32
  - 330Ohm resistor for the LED
  - 5mm LED
  -     Connect anode to GPIO 21
  -     Connect cathode to GND via the resistor
  - Wires
  - Breadboard

'''

from machine import Pin, PWM
from time import sleep_ms

pwm0 = PWM(Pin(21))

'''
while True:
    pwm0.duty(100)
    sleep_ms(1000)

    pwm0.duty(200)
    sleep_ms(1000)

    pwm0.duty(500)
    sleep_ms(1000)

    pwm0.duty(1000)
    sleep_ms(1000)
'''

while True:
    for duty_cycle in range(0, 1023, 15):
        pwm0.duty(duty_cycle)
        sleep_ms(10)

    for duty_cycle in range(1023, 0, -15):
        pwm0.duty(duty_cycle)
        sleep_ms(10)