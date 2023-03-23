import machine
from machine import Pin, SoftI2C
from lcd_api import LcdApi
from pico_i2c import I2cLcd
from time import sleep

I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16

i2c = SoftI2C(scl=Pin(17), sda=Pin(16), freq=1000)     #initializing the I2C method for ESP32
#i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)       #initializing the I2C method for ESP8266

lcd= I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

while True:
    lcd.putstr("Joker Smoker")
    sleep(1)
    lcd.clear()


