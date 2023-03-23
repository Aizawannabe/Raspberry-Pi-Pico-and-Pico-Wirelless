from machine import Pin
from mfrc522 import MFRC522  #importing the neccesary libraries 
import utime
       
reader = MFRC522(spi_id=0,sck=6,miso=4,mosi=7,cs=5,rst=22)
  #we are defining the pins that are going to be used.
                                                  #and also defining the RFID scanner.
 
red = Pin(0, Pin.OUT) #we are defining the red led
green = Pin(1, Pin.OUT) #we are defining the green led
blue = Pin(2, Pin.OUT) #we are defining the blue led
 

 
 
while True:         #this is the main program
    reader.init()
    (stat, tag_type) = reader.request(reader.REQIDL)
    if stat == reader.OK:
        (stat, uid) = reader.SelectTagSN()
        if stat == reader.OK:
            card = int.from_bytes(bytes(uid),"little",False)
            print(card)
            
            if card == 2773932883:
                print("Card ID: "+ str(card)+" PASS: Green Light Activated")
                red.value(0)
                green.value(1)
                blue.value(0)
                
                
            elif card == 2774357219:
                print("Card ID: "+ str(card)+" PASS: Blue Light Activated")
                for x in range(10):
                    red.value(1)
                    green.value(0)
                    blue.value(0)
                    utime.sleep(.1)
                    red.value(0)
                    utime.sleep(.1)

                
            else:
                print("Card ID: "+ str(card)+" UNKNOWN CARD! Red Light Activated")
                red.value(0)
                green.value(0)
                blue.value(0)
                utime.sleep(.1)