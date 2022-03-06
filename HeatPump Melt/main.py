from machine import Pin, Timer
import temperature

inbuiltLed = 25
led = Pin(inbuiltLed, Pin.OUT)


timer = Timer()

def ledblink(timer):

    tempInCelsius = temperature.getTemperatureInCelcius(3)
    if(tempInCelsius > 26):
        print('hot....')
        
    #temperature.getTemperatureSensorRaw()
                
    led.toggle()

timer.init(freq=2, mode=Timer.PERIODIC, callback=ledblink)
