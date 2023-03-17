import machine
sda=machine.Pin(0)
scl=machine.Pin(1)
i2c=machine.I2C(0,sda=sda, scl=scl, freq=400000)

devices = i2c.scan()


if len(devices) == 0: #checks for any returns in the i2c scan
     print("No i2c device !")
else:
     print('i2c devices found:',len(devices)) #if there's a return it will print this and then 
#                                              #it goes to the for loop to finish it.
# 
for device in devices:
     print("Decimal address: ",device," | Hexa address: ",hex(device))