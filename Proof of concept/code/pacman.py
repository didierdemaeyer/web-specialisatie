from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
#gpio.setwarnings(False)

mc = Minecraft.create()

#vars
air = block.AIR.id
wool = block.WOOL.id



#place food
def placeFood():
    j = 0
    new_z = z + 20

    while j < 10:

        mc.setBlock(x, y+5, new_z-1, wool)
        mc.setBlock(x, y+5, new_z, wool)
        mc.setBlock(x, y+5, new_z+1, wool)
        mc.setBlock(x, y+6, new_z-1, wool)
        mc.setBlock(x, y+6, new_z, wool)
        mc.setBlock(x, y+6, new_z+1, wool)
        mc.setBlock(x, y+7, new_z-1, wool)
        mc.setBlock(x, y+7, new_z, wool)
        mc.setBlock(x, y+7, new_z+1, wool)
        sleep(0.05)

        new_z += 20
        j += 1



#build pacman
def buildPacman():
    #get player pos
    global x, y, z
    x, y, z = mc.player.getPos()
    x = x+10

    #layer 1
    mc.setBlock(x, y, z-1, wool, 4)
    mc.setBlock(x, y, z, wool, 4)
    mc.setBlock(x, y, z+1, wool, 4)
    mc.setBlock(x, y, z+2, wool, 4)
    sleep(0.5)

    #layer 2
    mc.setBlock(x, y+1, z-3, wool, 4)
    mc.setBlock(x, y+1, z-2, wool, 4)
    mc.setBlock(x, y+1, z-1, wool, 4)
    mc.setBlock(x, y+1, z, wool, 4)
    mc.setBlock(x, y+1, z+1, wool, 4)
    mc.setBlock(x, y+1, z+2, wool, 4)
    mc.setBlock(x, y+1, z+3, wool, 4)
    mc.setBlock(x, y+1, z+4, wool, 4)
    sleep(0.5)

    #layer 3
    mc.setBlock(x, y+2, z-4, wool, 4)
    mc.setBlock(x, y+2, z-3, wool, 4)
    mc.setBlock(x, y+2, z-2, wool, 4)
    mc.setBlock(x, y+2, z-1, wool, 4)
    mc.setBlock(x, y+2, z, wool, 4)
    mc.setBlock(x, y+2, z+1, wool, 4)
    mc.setBlock(x, y+2, z+2, wool, 4)
    mc.setBlock(x, y+2, z+3, wool, 4)
    mc.setBlock(x, y+2, z+4, wool, 4)
    mc.setBlock(x, y+2, z+5, wool, 4)
    sleep(0.5)

    #layer 4
    mc.setBlock(x, y+3, z-4, wool, 4)
    mc.setBlock(x, y+3, z-3, wool, 4)
    mc.setBlock(x, y+3, z-2, wool, 4)
    mc.setBlock(x, y+3, z-1, wool, 4)
    mc.setBlock(x, y+3, z, wool, 4)
    mc.setBlock(x, y+3, z+1, wool, 4)
    mc.setBlock(x, y+3, z+2, wool, 4)
    mc.setBlock(x, y+3, z+3, wool, 4)
    mc.setBlock(x, y+3, z+4, wool, 4)
    mc.setBlock(x, y+3, z+5, wool, 4)
    sleep(0.5)

    #layer 5
    mc.setBlock(x, y+4, z-5, wool, 4)
    mc.setBlock(x, y+4, z-4, wool, 4)
    mc.setBlock(x, y+4, z-3, wool, 4)
    mc.setBlock(x, y+4, z-2, wool, 4)
    mc.setBlock(x, y+4, z-1, wool, 4)
    mc.setBlock(x, y+4, z, wool, 4)
    mc.setBlock(x, y+4, z+1, wool, 4)
    mc.setBlock(x, y+4, z+2, wool, 4)
    mc.setBlock(x, y+4, z+3, wool, 4)
    sleep(0.5)

    #layer 6
    mc.setBlock(x, y+5, z-6, wool, 4)
    mc.setBlock(x, y+5, z-5, wool, 4)
    mc.setBlock(x, y+5, z-4, wool, 4)
    mc.setBlock(x, y+5, z-3, wool, 4)
    mc.setBlock(x, y+5, z-2, wool, 4)
    mc.setBlock(x, y+5, z-1, wool, 4)
    mc.setBlock(x, y+5, z, wool, 4)
    sleep(0.5)

    #layer 7
    mc.setBlock(x, y+6, z-6, wool, 4)
    mc.setBlock(x, y+6, z-5, wool, 4)
    mc.setBlock(x, y+6, z-4, wool, 4)
    mc.setBlock(x, y+6, z-3, wool, 4)
    mc.setBlock(x, y+6, z-2, wool, 4)
    sleep(0.5)

    #layer 8
    mc.setBlock(x, y+7, z-6, wool, 4)
    mc.setBlock(x, y+7, z-5, wool, 4)
    mc.setBlock(x, y+7, z-4, wool, 4)
    mc.setBlock(x, y+7, z-3, wool, 4)
    mc.setBlock(x, y+7, z-2, wool, 4)
    mc.setBlock(x, y+7, z-1, wool, 4)
    mc.setBlock(x, y+7, z, wool, 4)

    sleep(0.5)

    #layer 9
    mc.setBlock(x, y+8, z-5, wool, 4)
    mc.setBlock(x, y+8, z-4, wool, 4)
    mc.setBlock(x, y+8, z-3, wool, 4)
    mc.setBlock(x, y+8, z-2, wool, 4)
    mc.setBlock(x, y+8, z-1, wool, 4)
    mc.setBlock(x, y+8, z, wool, 4)
    mc.setBlock(x, y+8, z+1, wool, 4)
    mc.setBlock(x, y+8, z+2, wool, 4)
    mc.setBlock(x, y+8, z+3, wool, 4)
    sleep(0.5)

    #layer 10
    mc.setBlock(x, y+9, z-4, wool, 4)
    mc.setBlock(x, y+9, z-3, wool, 4)
    mc.setBlock(x, y+9, z-2, wool, 4)
    mc.setBlock(x, y+9, z-1, wool, 4)
    mc.setBlock(x, y+9, z, wool, 4)
    mc.setBlock(x, y+9, z+1, wool, 4)
    mc.setBlock(x, y+9, z+2, wool, 15)
    mc.setBlock(x, y+9, z+3, wool, 4)
    mc.setBlock(x, y+9, z+4, wool, 4)
    mc.setBlock(x, y+9, z+5, wool, 4)
    sleep(0.5)

    #layer 11
    mc.setBlock(x, y+10, z-4, wool, 4)
    mc.setBlock(x, y+10, z-3, wool, 4)
    mc.setBlock(x, y+10, z-2, wool, 4)
    mc.setBlock(x, y+10, z-1, wool, 4)
    mc.setBlock(x, y+10, z, wool, 4)
    mc.setBlock(x, y+10, z+1, wool, 4)
    mc.setBlock(x, y+10, z+2, wool, 4)
    mc.setBlock(x, y+10, z+3, wool, 4)
    mc.setBlock(x, y+10, z+4, wool, 4)
    mc.setBlock(x, y+10, z+5, wool, 4)
    sleep(0.5)

    #layer 12
    mc.setBlock(x, y+11, z-3, wool, 4)
    mc.setBlock(x, y+11, z-2, wool, 4)
    mc.setBlock(x, y+11, z-1, wool, 4)
    mc.setBlock(x, y+11, z, wool, 4)
    mc.setBlock(x, y+11, z+1, wool, 4)
    mc.setBlock(x, y+11, z+2, wool, 4)
    mc.setBlock(x, y+11, z+3, wool, 4)
    mc.setBlock(x, y+11, z+4, wool, 4)
    sleep(0.5)

    #layer 13
    mc.setBlock(x, y+12, z-1, wool, 4)
    mc.setBlock(x, y+12, z, wool, 4)
    mc.setBlock(x, y+12, z+1, wool, 4)
    mc.setBlock(x, y+12, z+2, wool, 4)
    sleep(0.5)



#move pacman
def move():
    i = 0

    while i < 150:
        global z
        z += 1
        i += 1

        #layer 1
        mc.setBlock(x, y, z-1, wool, 4)
        mc.setBlock(x, y, z, wool, 4)
        mc.setBlock(x, y, z+1, wool, 4)
        mc.setBlock(x, y, z+2, wool, 4)

        #layer 2
        mc.setBlock(x, y+1, z-3, wool, 4)
        mc.setBlock(x, y+1, z-2, wool, 4)
        mc.setBlock(x, y+1, z-1, wool, 4)
        mc.setBlock(x, y+1, z, wool, 4)
        mc.setBlock(x, y+1, z+1, wool, 4)
        mc.setBlock(x, y+1, z+2, wool, 4)
        mc.setBlock(x, y+1, z+3, wool, 4)
        mc.setBlock(x, y+1, z+4, wool, 4)

        #layer 3
        mc.setBlock(x, y+2, z-4, wool, 4)
        mc.setBlock(x, y+2, z-3, wool, 4)
        mc.setBlock(x, y+2, z-2, wool, 4)
        mc.setBlock(x, y+2, z-1, wool, 4)
        mc.setBlock(x, y+2, z, wool, 4)
        mc.setBlock(x, y+2, z+1, wool, 4)
        mc.setBlock(x, y+2, z+2, wool, 4)
        mc.setBlock(x, y+2, z+3, wool, 4)
        mc.setBlock(x, y+2, z+4, wool, 4)
        mc.setBlock(x, y+2, z+5, wool, 4)

        #layer 4
        mc.setBlock(x, y+3, z-4, wool, 4)
        mc.setBlock(x, y+3, z-3, wool, 4)
        mc.setBlock(x, y+3, z-2, wool, 4)
        mc.setBlock(x, y+3, z-1, wool, 4)
        mc.setBlock(x, y+3, z, wool, 4)
        mc.setBlock(x, y+3, z+1, wool, 4)
        mc.setBlock(x, y+3, z+2, wool, 4)
        mc.setBlock(x, y+3, z+3, wool, 4)
        mc.setBlock(x, y+3, z+4, wool, 4)
        mc.setBlock(x, y+3, z+5, wool, 4)

        #layer 5
        mc.setBlock(x, y+4, z-5, wool, 4)
        mc.setBlock(x, y+4, z-4, wool, 4)
        mc.setBlock(x, y+4, z-3, wool, 4)
        mc.setBlock(x, y+4, z-2, wool, 4)
        mc.setBlock(x, y+4, z-1, wool, 4)
        mc.setBlock(x, y+4, z, wool, 4)
        mc.setBlock(x, y+4, z+1, wool, 4)
        mc.setBlock(x, y+4, z+2, wool, 4)
        mc.setBlock(x, y+4, z+3, wool, 4)

        #layer 6
        mc.setBlock(x, y+5, z-6, wool, 4)
        mc.setBlock(x, y+5, z-5, wool, 4)
        mc.setBlock(x, y+5, z-4, wool, 4)
        mc.setBlock(x, y+5, z-3, wool, 4)
        mc.setBlock(x, y+5, z-2, wool, 4)
        mc.setBlock(x, y+5, z-1, wool, 4)
        mc.setBlock(x, y+5, z, wool, 4)

        #layer 7
        mc.setBlock(x, y+6, z-6, wool, 4)
        mc.setBlock(x, y+6, z-5, wool, 4)
        mc.setBlock(x, y+6, z-4, wool, 4)
        mc.setBlock(x, y+6, z-3, wool, 4)
        mc.setBlock(x, y+6, z-2, wool, 4)

        #layer 8
        mc.setBlock(x, y+7, z-6, wool, 4)
        mc.setBlock(x, y+7, z-5, wool, 4)
        mc.setBlock(x, y+7, z-4, wool, 4)
        mc.setBlock(x, y+7, z-3, wool, 4)
        mc.setBlock(x, y+7, z-2, wool, 4)
        mc.setBlock(x, y+7, z-1, wool, 4)
        mc.setBlock(x, y+7, z, wool, 4)

        #layer 9
        mc.setBlock(x, y+8, z-5, wool, 4)
        mc.setBlock(x, y+8, z-4, wool, 4)
        mc.setBlock(x, y+8, z-3, wool, 4)
        mc.setBlock(x, y+8, z-2, wool, 4)
        mc.setBlock(x, y+8, z-1, wool, 4)
        mc.setBlock(x, y+8, z, wool, 4)
        mc.setBlock(x, y+8, z+1, wool, 4)
        mc.setBlock(x, y+8, z+2, wool, 4)
        mc.setBlock(x, y+8, z+3, wool, 4)

        #layer 10
        mc.setBlock(x, y+9, z-4, wool, 4)
        mc.setBlock(x, y+9, z-3, wool, 4)
        mc.setBlock(x, y+9, z-2, wool, 4)
        mc.setBlock(x, y+9, z-1, wool, 4)
        mc.setBlock(x, y+9, z, wool, 4)
        mc.setBlock(x, y+9, z+1, wool, 4)
        mc.setBlock(x, y+9, z+2, wool, 15)
        mc.setBlock(x, y+9, z+3, wool, 4)
        mc.setBlock(x, y+9, z+4, wool, 4)
        mc.setBlock(x, y+9, z+5, wool, 4)

        #layer 11
        mc.setBlock(x, y+10, z-4, wool, 4)
        mc.setBlock(x, y+10, z-3, wool, 4)
        mc.setBlock(x, y+10, z-2, wool, 4)
        mc.setBlock(x, y+10, z-1, wool, 4)
        mc.setBlock(x, y+10, z, wool, 4)
        mc.setBlock(x, y+10, z+1, wool, 4)
        mc.setBlock(x, y+10, z+2, wool, 4)
        mc.setBlock(x, y+10, z+3, wool, 4)
        mc.setBlock(x, y+10, z+4, wool, 4)
        mc.setBlock(x, y+10, z+5, wool, 4)

        #layer 12
        mc.setBlock(x, y+11, z-3, wool, 4)
        mc.setBlock(x, y+11, z-2, wool, 4)
        mc.setBlock(x, y+11, z-1, wool, 4)
        mc.setBlock(x, y+11, z, wool, 4)
        mc.setBlock(x, y+11, z+1, wool, 4)
        mc.setBlock(x, y+11, z+2, wool, 4)
        mc.setBlock(x, y+11, z+3, wool, 4)
        mc.setBlock(x, y+11, z+4, wool, 4)

        #layer 13
        mc.setBlock(x, y+12, z-1, wool, 4)
        mc.setBlock(x, y+12, z, wool, 4)
        mc.setBlock(x, y+12, z+1, wool, 4)
        mc.setBlock(x, y+12, z+2, wool, 4)


        #remove old blocks
        mc.setBlock(x, y, z-2, air)
        mc.setBlock(x, y+1, z-4, air)
        mc.setBlock(x, y+2, z-5, air)
        mc.setBlock(x, y+3, z-5, air)
        mc.setBlock(x, y+4, z-6, air)
        mc.setBlock(x, y+5, z-7, air)
        mc.setBlock(x, y+6, z-7, air)
        mc.setBlock(x, y+7, z-7, air)
        mc.setBlock(x, y+8, z-6, air)
        mc.setBlock(x, y+9, z-5, air)
        mc.setBlock(x, y+10, z-5, air)
        mc.setBlock(x, y+11, z-4, air)
        mc.setBlock(x, y+12, z-2, air)


        #wait after move
        sleep(0.1)




sensor = 23
gpio.setup(sensor, gpio.IN)

inputcount = 0

while True:
    sleep(0.2)
    if gpio.input(sensor) == 0:
        if inputcount == 0:
            buildPacman()
            inputcount += 1
            sleep(1)

        elif inputcount == 1:
            placeFood()
            inputcount += 1
            sleep(1)

        elif inputcount == 2:
            move()
            inputcount = 0
            sleep(1)



##reset the status of all gpio pins
gpio.cleanup()
