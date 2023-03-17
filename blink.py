from machine import Pin, Timer
led = Pin(25, Pin.OUT)
LED_state = True
time = Timer()
def tick(timer):
     global led, LED_state
     LED_state = not LED_state
     led.value(LED_state)
time.init(freq=1000,mode=Timer.PERIODIC, callback=tick)


