import machine
import time

Relay=machine.Pin(14,machine.Pin.OUT)
Led=machine.Pin(15,machine.Pin.OUT)
x=0
while True:
    Relay.value(1)
    time.sleep(.1)
    Relay.value(0)
    time.sleep(1)
    print(x)
    x=x+1
    if x==11:
        x=0
        print("cycle done")
    
     
    
    