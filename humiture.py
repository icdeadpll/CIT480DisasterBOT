import Adafruit_DHT as DHT
import RPi.GPIO as GPIO
from time import sleep

Sensor = 23
humiture = 24

def setup():
    print 'Setting up, please wait...'

def loop():
    while True:
        humidity, temperature = DHT.read_retry(Sensor, humiture)

        if humidity is not None and temperature is not None:
            temperature = (temperature*1.8)+32 
            print 'Temp={0:0.1f}*F  Humidity={1:0.1f}%'.format(temperature, humidity)
            sleep(1)
        else:
            print 'Failed to get reading. Try again!'

def destroy():
    GPIO.cleanup()

if __name__ == "__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()