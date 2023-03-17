import machine
import time
Button=machine.Pin(14,machine.Pin.IN,machine.Pin.PULL_DOWN)
Led=machine.Pin(15,machine.Pin.OUT)

def start():
       
        while True:
            if Button.value()==True:     
                print(Button.value())
                Led.on()
                
            time.sleep(.1)
            if Button.value()==False:
                Led.off()
                print('off')

start()

    
