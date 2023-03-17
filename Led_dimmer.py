import machine
import utime
potentiometer = machine.ADC(0)
led = machine.PWM(machine.Pin(0))
led.freq(1000)
Duty_cycle=0
while Duty_cycle<=65535:
    Duty_cycle=+1
    led.duty_u16(Duty_cycle)
    utime.sleep(.001)
    
Duty_cycle=65531
while Duty_cycle>0:
    Duty_cycle=-1
    led.duty_u16(Duty_cycle)
    time.sleep(.001)

led.duty_u16(1)
led.deinit()