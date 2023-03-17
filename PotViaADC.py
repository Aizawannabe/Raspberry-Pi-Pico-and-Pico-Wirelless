import machine
import time

adc = machine.ADC(26)  # Use Pin GP26 as analog input
while True:
    reading = adc.read_u16()  # Read the analog input value
    voltage = (reading * 3.3) / (65535)  # Convert the reading to voltage
    print("Voltage: {:.2f}V".format(voltage))  # Print the voltage
    time.sleep(0.1)  # Wait for 100 milliseconds
