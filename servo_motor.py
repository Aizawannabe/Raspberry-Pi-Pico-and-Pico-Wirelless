import machine
import time
servo=machine.PWM(machine.Pin(9))
servo.freq(50)

while True:
    servo.duty_u16(1300)
    time.sleep(1)
    servo.duty_u16(8000)
    time.sleep(1)