import RPi.GPIO as GPIO
from time import sleep

Headlight = 26
def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Headlight,GPIO.OUT)
    GPIO.output(Headlight,GPIO.HIGH)

def on():
    GPIO.output(Headlight,GPIO.LOW)

def off():
    GPIO.output(Headlight,GPIO.HIGH)

