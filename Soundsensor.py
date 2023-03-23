import machine
import time
DigitalOutput = machine.Pin(17,machine.Pin.IN)
AnalogueOutput = machine.Pin(27,machine.Pin.IN)
Red = machine.Pin(0,machine.Pin.OUT)
Green = machine.Pin(1,machine.Pin.OUT)
Value=machine.ADC(1)
switch=1
while True:
    if DigitalOutput.value()==True and switch==1:
        Red.on()
        Green.off()
        switch=2
        DigitalOutput.low()
        time.sleep(1)
    if DigitalOutput.value()==True and switch==2:
        Red.off()
        Green.on()
        switch=3
        DigitalOutput.low()
        time.sleep(1)
    if DigitalOutput.value()==True and switch==3:
        Red.off()
        Green.off()
        switch=1
        DigitalOutput.low()
        time.sleep(1)
    
    

    
    
