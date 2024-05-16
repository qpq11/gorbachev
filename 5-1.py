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
    for i in range(2**8):
        dac_val = dec2bin(i)
        gpio.output(dac, dac_val)
        cmp = gpio.input(comp)
        sleep(0.005)
        if cmp:
            return i
    return 0

try:
    while True:
        i = adc()
        voltage = i* 3.3 / 256.0
        if i:
            print("{:.2f}V".format(voltage))
finally:
    gpio.output(dac, 0)
    gpio.cleanup()
    print('Program terminated')