from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
#gpio.setwarnings(False)

mc = Minecraft.create()

#vars
air = block.AIR.id
stone = block.STONE.id
grass = block.GRASS.id
dirt = block.DIRT.id
wood_planks = block.WOOD_PLANKS.id
water = block.WATER_STATIONARY.id
gold_ore = block.GOLD_ORE.id
gold_block = block.GOLD_BLOCK.id
diamond_block = block.DIAMOND_BLOCK.id
neather_reactor_core = block.NETHER_REACTOR_CORE.id
wool = block.WOOL.id
flower = 38

stairs_wood = block.STAIRS_WOOD.id



#flicker led

##led = 15
##gpio.setup(led, gpio.OUT)
##
##i = 0
##
##while i < 50:
##    if (i % 2) == 0:
##        gpio.output(led, gpio.HIGH)
##        print("LED ON")
##    else:
##        gpio.output(led, gpio.LOW)
##        print("LED OFF")
##
##    i += 1
##    sleep(0.5)


#read input from button

sensor = 23
gpio.setup(sensor, gpio.IN)

while True:
    print(gpio.input(sensor))
    sleep(0.5)



##reset the status of all gpio pins
gpio.cleanup()


