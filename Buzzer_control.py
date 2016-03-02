import RPi.GPIO as GPIO
import time

Buzzer = 12

def setup():
    global BuzzerPin
    BuzzerPin = Buzzer
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BuzzerPin, GPIO.OUT)
    GPIO.output(BuzzerPin, GPIO.HIGH)

def on():
    GPIO.output(BuzzerPin, GPIO.LOW)

def off():
    GPIO.output(BuzzerPin, GPIO.HIGH)

def beep(x):
    on()
    time.sleep(x)
    off()
    time.sleep(x)

def destroy():
    GPIO.output(BuzzerPin, GPIO.HIGH)
    GPIO.cleanup()

def loop():
    while True:
        beep(0.5)
