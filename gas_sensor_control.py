import PCF8591 as ADC
import RPi.GPIO as GPIO
import time
import math

DO = 4

def setup():
    GPIO.setmode(GPIO.BCM)
    ADC.setup(0x48)
    GPIO.setup(DO, GPIO.IN)

def Print(x):
    if x == 1:
        print 'Safe!'
    if x == 0:
        print 'Danger Gas!'

def check_for_gas():
    status = 1
    count = 0
    print ADC.read(3)
    tmp = GPIO.input(DO);
    if tmp != status:
        Print(tmp)
    else:
        Print(0)


def loop():
    status = 1
    while True:
        tmp = GPIO.input(DO);
        if tmp != status:
            Print(tmp)
            time.sleep(1)
        else:
           time.sleep(1)

def destroy():
    GPIO.cleanup()
