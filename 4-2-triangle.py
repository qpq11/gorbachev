import RPi.GPIO as gpio
from time import sleep

dac = [8,11,7,1,0,5,12,6]

gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)

def dec2bin(value, n):
    return [int(i) for i in bin(value)[2:].zfill(n)]

try:
    while(True):
            per = input()
            if not(per.isdigit()):
                print('Enter a NUMBER, please')

            t = (int(per)/256)/2

            for j in range(10):
                for i in range(256):
                    gpio.output(dac, dec2bin(i, 8))
                    sleep(t)
                for i in range(255, -1, -1):
                    gpio.output(dac, dec2bin(i, 8))
                    sleep(t)

except ValueError:
    print("bad period value. try again!")

finally:
    gpio.output(dac, 0)
    gpio.cleanup()
    print("program terminated")