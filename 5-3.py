import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BCM)
led=[2,3,4,17,27,22,10,9]
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp=14
troyka=13

gpio.setup(dac, gpio.OUT)
gpio.setup(led, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial=gpio.HIGH)
gpio.setup(comp, gpio.IN)

def dec2bin(num):
    return [int(e) for e in bin(num)[2:].zfill(8)]

def adc():
    k=0
    for i in range(7, -1, -1):
        k += 2**i
        dac_val = dec2bin(k)
        gpio.output(dac, dac_val)
        cmp = gpio.input(comp)
        #print(k, cmp)
        sleep(0.01)
        if cmp:
            k -= 2**i
        #print(0, k)    
    return k

    """
    for i in range(2**8):
        dac_val = dec2bin(i)
        gpio.output(dac, dac_val)
        cmp = gpio.input(comp)
        sleep(0.01)
        if cmp:
            return i
    return 0"""

def volume(val):
    arr=[0 for _ in range(8)]
    val=int(val/256*10)
    for i in range(val - 1):
        arr[i] = 1
    return arr

try:
    while True:
        i=adc()
        if i and not(i in [127, 128, 129]):
            vol = volume(i)
            gpio.output(led, vol)
            print(int(i/256*10))


finally:
    gpio.output(dac, 0)
    gpio.output(led, 0)
    gpio.cleanup()
    print('Program terminated')