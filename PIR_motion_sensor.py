import machine
import time
PIR=machine.Pin(16,machine.Pin.IN,machine.Pin.PULL_DOWN)
Led=machine.Pin(15,machine.Pin.OUT)

while True:
    if PIR.value()==True:
        Led.on()
    else:
        Led.off()
        
        
