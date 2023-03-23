from machine import UART, Pin
import time

uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

while True:
   uart.write('hello') # writes 5 bytes
   val = uart.read(5)  # reads up to 5 bytes
   print(val) # prints data
   time.sleep(1)