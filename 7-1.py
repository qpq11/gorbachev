import RPi.GPIO as gpio
import matplotlib.pyplot as plt
import time as t

dac = [8, 11, 7, 1, 0, 5, 12, 6]
led = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13
bits = len(dac) #8
levels = 2**bits #256
maxU = 3.3
data_u = []
data_t = []

def decbin(n):
    return [int(i) for i in bin(n)[2:].zfill(8)]

'''def acp():
    val = 0
    for i in range(bits-1, -1, -1):
        val += 2**i
        ledsignal(val)
        t.sleep(0.002)
        compval = gpio.input(comp)
        #print("cmp:", compval)
        if (compval):
            val -= 2**i
    return val'''

def acp():
    value = 0
    for i in range(len(dac) - 1, -1, -1):
        value += 1 << i
        ledsignal(value)
        t.sleep(0.01)
        cmp = gpio.input(comp)
        if cmp:
            value -= 1 << i
    return value

def ledsignal(val):
    out = decbin(val)
    gpio.output(dac, out)
    return out

gpio.setmode(gpio.BCM)
gpio.setup(led, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial = gpio.LOW)
gpio.setup(dac, gpio.OUT, initial = gpio.LOW)
gpio.setup(comp, gpio.IN)
gpio.output(troyka, 1)
try:
    start = t.time()
    val = 0
    while (val < 207):
        val = acp()
        print("1volts:", val/levels * maxU)
        ledsignal(val)
        data_u.append(val)
        data_t.append(t.time() - start)
        
    gpio.output(troyka, 0)

    while(val > 170):
        val = acp()
        print("2volts:", val, val/levels * maxU)
        ledsignal(val)
        data_u.append(val)
        data_t.append(t.time() - start)
    
    end = t.time() - start

    with open("settings.txt", "w+") as f:
        f.write(str((end- start) / len(data_t)))
        f.write("\n")
        f.write(str(maxU/levels))

    print("data written in settings:", end-start, ' ', (end- start) / len(data_t), ' ', maxU / levels)

    with open("data.txt", "w+") as f:
        f.write('\n'.join([str(elem) for elem in data_u]))

finally:
    gpio.output(dac, 0)
    gpio.cleanup()
    plt.plot(data_t, data_u)
    plt.show()