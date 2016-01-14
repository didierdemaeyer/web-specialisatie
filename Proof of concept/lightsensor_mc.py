from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
import RPi.GPIO as GPIO, time, os

mc = Minecraft.create()

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


#blocks
air = block.AIR.id
gold_block = block.GOLD_BLOCK.id


i = 0 
x,y,z = mc.player.getPos()
sensorvalue = 0

while i < 100:
    
    sensorvalue = RCtime(15)

    print (sensorvalue)
    
    mc.setBlocks(x+20, y, z-5, x+20, y + (sensorvalue / 10), z+5, gold_block)
    mc.setBlocks(x+20, y + (sensorvalue / 10), z-5, x+20, y + 100, z+5, air) 
