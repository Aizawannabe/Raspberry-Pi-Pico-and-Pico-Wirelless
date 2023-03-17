import machine
import time
TRIG = machine.Pin(14, machine.Pin.OUT)
ECHO = machine.Pin(15, machine.Pin.IN)
Green = machine.Pin(0,machine.Pin.OUT)
Red = machine.Pin(1,machine.Pin.OUT)
Switch=machine.Pin(12,machine.Pin.IN,machine.Pin.PULL_UP)
Buzzer=machine.Pin(16,machine.Pin.OUT)


def distance():
    # send a trigger pulse
    TRIG.value(0)
    time.sleep_us(10)
    TRIG.value(1)
    time.sleep_us(10)
    TRIG.value(0)

    # measure the time it takes for the echo to return
    while ECHO.value() == 0:
        pass

    start = time.ticks_us()
    while ECHO.value() == 1:
        pass
        
    stop = time.ticks_us()
    tt=(stop-start)

    # calculate the distance based on the time it took for the echo to return
    distance = (tt*0.000343/2)
    return distance
def Kill():
    if Switch.value()==1:
        Buzzer.value(0)   
while True:
    dist = distance()
    #print("Measured Distance = %.1f cm" % dist)
    print("Measured Distance = ",dist, "m","    ",dist*100,"cm")
    if dist<1:
        Red.on()
        Green.off()
        time.sleep(.1)
        Green.on()
        Red.off()
        time.sleep(.1)
        Buzzer.high()
        Kill()    
         
    if dist>1:
        Green.on()
        Red.off()
        Buzzer.low()
        
        
        
    