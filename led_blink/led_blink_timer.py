'''
 LED blink with timer

 This sketch shows how to blink an LED connected to GPIO 21 using a timer instead of a loop.

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

from machine import Pin, Timer

led = Pin(19, Pin.OUT)    # create output pin on GPIO21

def blink_isr(event):
    if led.value() == False:
        led.on()
    else:
        led.off()

blink_timer = Timer(1)
blink_timer.init(period=250, mode=Timer.PERIODIC, callback=blink_isr) #period: Sets the timer period to 250 milliseconds
                                                                      #mode: makes the timer run periodically (the timer keeps resetting and calling the callback function every period)
                                                                      #callback: specifies the function to call when the timer expires