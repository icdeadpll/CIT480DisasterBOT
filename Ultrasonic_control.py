import RPi.GPIO as GPIO
import time

TRIG = 5
ECHO = 6

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

def distance():
    GPIO.output(TRIG, 0)
    time.sleep(0.000002)

    GPIO.output(TRIG, 1)
    time.sleep(0.000001)
    GPIO.output(TRIG, 0)

    while GPIO.input(ECHO) == 0:
        a = 0
    time1 = time.time()
    while GPIO.input(ECHO) == 1:
        a = 1
    time2 = time.time()

    during = time2 - time1
    return during

def distance_in_m(x):
    return x * 340/2 

def distance_in_ft(x):
    return x * 1130/2


def loop():
    while True:
        dis = distance()
        m = distance_in_m(dis)
        ft = distance_in_ft(dis)
        print ("Distance= %10.1f m" % (m))
        print ("Distance= %10.1f ft" % (ft))
        print ''
        time.sleep(1)
        
def destroy():
    GPIO.cleanup()
