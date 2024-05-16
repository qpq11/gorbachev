import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp=14
troyka=13

gpio.setup(dac, gpio.OUT)
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
        #print(k, cmp, dac, dac_val)
        sleep(0.005)
        if cmp:
            k -= 2**i
        #print(0, k)    
    return k

try:
    while True:
        i = adc()
        voltage = i* 3.3 / 256.0
        if i and not(i in [127, 128, 129]):
            print("{:.2f}V".format(voltage))
finally:
    gpio.output(dac, 0)
    gpio.cleanup()
    print('Program terminated')