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


##def placeStairs():
    #place stairs
    x, y, z = mc.player.getPos()
    x = x+10
    y -= 1

    i = 0

    while i < 50:
        x += 1
        y += 1

        mc.setBlock(x, y, z-1, stairs_wood)
        mc.setBlock(x, y, z, stairs_wood)
        mc.setBlock(x, y, z+1, stairs_wood)
        i += 1
        sleep(0.2)


#wait for input
##sensor = 15
##gpio.setup(sensor, gpio.IN)
##
##while True:
##    sensorvalue = gpio.input(sensor)
##    print(sensorvalue)
##    
##    if sensorvalue == 1:
##        placeStairs()
##        break
##    
##    sleep(0.2)





##reset the status of all gpio pins
gpio.cleanup()
