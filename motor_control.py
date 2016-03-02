import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

Motor1A = 17
Motor1B = 27
Motor1E = 22

Motor2A = 10
Motor2B = 9
Motor2E = 11

GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor1E, GPIO.OUT)

GPIO.setup(Motor2A, GPIO.OUT)
GPIO.setup(Motor2B, GPIO.OUT)
GPIO.setup(Motor2E, GPIO.OUT)

def forward_right():
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.HIGH)

def forward_left():
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.HIGH)
    
def forward(n):
    forward_right()
    forward_left()
    sleep(n)
    stop()

def backward(n):
    backward_right()
    backward_left()
    sleep(n)
    stop()
    
def backward_right():
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
    GPIO.output(Motor1E,GPIO.HIGH)

def backward_left():
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.HIGH)
    GPIO.output(Motor2E,GPIO.HIGH)
    
def right(n):
    backward_right()
    forward_left()
    sleep(n)
    stop()

def left(n):
    forward_right()    
    backward_left()
    sleep(n)
    stop()
    
def stop_right():
    GPIO.output(Motor1E,GPIO.LOW)

def stop_left():
    GPIO.output(Motor2E,GPIO.LOW)
    
def stop():
    GPIO.output(Motor1E,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.LOW)
    
