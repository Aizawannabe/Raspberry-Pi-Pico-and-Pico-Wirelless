import machine
import time
AnalogueOutput = machine.Pin(26,machine.Pin.IN)
Red = machine.Pin(2,machine.Pin.OUT)
Green = machine.Pin(1,machine.Pin.OUT)
Led = machine.PWM(machine.Pin(0))
Led.freq(1000)

Value=machine.ADC(0)

while True:
    Sound=(Value.read_u16()/65535*100)
    print("Sound available:",Sound)
    time.sleep(1)
    Led.duty_u16(Value.read_u16())
    