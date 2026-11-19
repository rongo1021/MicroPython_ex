from machine import Pin
import time

LED_PIN = 4
ON_VALUE = 1
OFF_VALUE = 0
PERIOD = 0.01

MAX = 100

STEP = 1

led = Pin(LED_PIN, Pin.OUT, value=OFF_VALUE)


while True:
    for level in range(0, MAX+1, STEP):
        ratio = level / MAX
        on_time = PERIOD * ratio
        off_time = PERIOD - on_time
        led.value(ON_VALUE)
        time.sleep(on_time)
        led.value(OFF_VALUE)
        time.sleep(off_time)
    
    for level in range(MAX, 0, -STEP):
        ratio = level / MAX
        on_time = PERIOD * ratio
        off_time = PERIOD - on_time
        led.value(ON_VALUE)
        time.sleep(on_time)
        led.value(OFF_VALUE)
        time.sleep(off_time)