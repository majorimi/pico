from machine import Pin, Timer

inbuiltLed = 25
led = Pin(inbuiltLed, Pin.OUT)

timer = Timer()

def ledBlink(timer):
    
    led.toggle()

timer.init(freq=2, mode=Timer.PERIODIC, callback=ledblink)