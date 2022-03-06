from machine import ADC

sensor_temp = ADC(4)
conversion_factor = 3.3 / (65535)

def getTemperatureInCelcius(decimals = 1):
    
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = round(27 - ((reading - 0.706)/0.00172), decimals)
    print('Temperature: '+ str(temperature)+'\n')
    
    return temperature;

def getTemperatureSensorRaw():
    
    reading = sensor_temp.read_u16() * conversion_factor
    print('Temperature sensor Raw: '+ str(reading)+'\n')
    
    return reading;