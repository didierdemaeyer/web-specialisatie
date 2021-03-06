import RPi.GPIO as GPIO, time, os

DEBUG = 1
GPIO.setmode(GPIO.BCM)

def RCtime (RCpin):
    reading = 0
    GPIO.setup(RCpin, GPIO.OUT)
    GPIO.output(RCpin, GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(RCpin, GPIO.IN)
    # This takes about 1 ms per loop cycle
    while(GPIO.input(RCpin) == GPIO.LOW):
        reading += 1

    return reading


while True:
    print (RCtime(15))


GPIO.cleanup()
