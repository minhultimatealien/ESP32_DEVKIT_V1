from machine import Pin, PWM
from time import sleep_ms

input_pin = Pin(34,Pin.IN)

while True:
    input_value = input_pin.value()  # Read the state of the pin (0 or 1)
    
    if input_value == 1:
        print("No obstacle")
    else:
        print("There is a mysterious obstacle")
    
    sleep_ms(5)  # Delay between readings

