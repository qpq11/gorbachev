import RPi.GPIO as gpio
import sys

dac = [8,11,7,1,0,5,12,6]

gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)

def decimal2binary(value, n):
    return [int(i) for i in bin(value)[2:].zfill(n)]

try:
    while(True):
        value = input('type in integer from 0 to 255: ')
        if (value == 'q'):
            print('program terminated')
            sys.exit(0)
        elif (value.isdigit()) and (int(value) % 1 == 0) and (0 <= int(value) <=255):
            gpio.output(dac, decimal2binary(int(value), 8))
            print("Out voltage is about", round(float(value) / 256.0 * 3.3, 4))
        elif(not(value.isdigit())):
            print('type in a POSITIVE NUMBER, please.')
        elif(int(value) % 1):
            print('type in an INT, please.')
        elif(int(value)>255):
            print('type in an int NOT BIGGER THAN 256, please.')

except ValueError:
    print('type in integer from 0 to 255, please.')

except KeyboardInterrupt:
    print('program terminated')

finally:
    gpio.output(dac, 0)
    gpio.cleanup()