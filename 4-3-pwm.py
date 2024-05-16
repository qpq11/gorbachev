import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(24, gpio.OUT)

dac = [8,11,7,1,0,5,12,6]
gpio.setup(dac, gpio.OUT, initial = gpio.HIGH)

pwm=gpio.PWM(24, 1000)
pwm.start(0)

try:
    while(True):
        c = int(input())
        pwm.ChangeDutyCycle(c)
        print(3.3*c/100)

except ValueError:
    print("type in a NUMBER, please.")

finally:
    pwm.stop()
    gpio.output(14, 0)
    gpio.cleanup()
    print("program terminated")