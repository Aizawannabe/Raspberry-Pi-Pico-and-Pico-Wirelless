import machine
import time

#Create an 'object' for our digital pin
Sound_Sensor = machine.Pin(16,machine.Pin.IN)
Green = machine.Pin(1,machine.Pin.OUT)
Red = machine.Pin(0,machine.Pin.OUT)       
while True:
    if Sound_Sensor.value() == 1:   
        Green.toggle()
        Red.off()					
    if Sound_Sensor.value() ==0: 
        Red.toggle()
        Green.off()
  