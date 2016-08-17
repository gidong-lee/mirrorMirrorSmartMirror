import RPi.GPIO as GPIO

LED = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

def ledon():
    GPIO.output(LED, True)

def ledoff():
    GPIO.output(LED, False)
