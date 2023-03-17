from machine import Pin
import utime
from time import sleep
trig= Pin(5,Pin.OUT)
echo= Pin(18,Pin.IN, Pin.PULL_DOWN)
Green = Pin(0,Pin.OUT)
Red = Pin(2,Pin.OUT)
def checkdistance():
    Speedofsound=0.344
    trig.low()
    utime.sleep_us(20)
    trig.high()
    utime.sleep_us(10)
    trig.low()
    exitLoop = False
    loopcount = 0
    while echo.value() == 0 and exitLoop==False:
        loopcount = loopcount+1
        delaytime=utime.ticks_us()
        
        if loopcount > 300000 : exitLoop ==True
    while echo.value()==1 and exitLoop==False:
        loopcount=loopcount+1
        receivetime=utime.ticks_us()
        if loopcount > 300000:exitLoop==True
    if exitLoop==True:
        return 0
        
    else:
        distance = ((receivetime-delaytime)* Speedofsound)/2
        return distance
while True:
    distance = checkdistance()
    print(distance)
    if checkdistance() < 900:
            print(distance)
            Green.on()
            Red.off()
            sleep(.1)
            Green.off()
            Red.on()
            sleep(.1)
    if checkdistance() > 900:
        print(distance)
        Green.on()
        Red.off()
        
        
            
            

            
        
        
        
    
                   