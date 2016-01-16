import mcpi.minecraft as minecraft
import mcpi.block as block
import random
import time
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)

mc = minecraft.Minecraft.create()
mc.postToChat("Minecraft Whac-a-Block!")


#vars
stone = block.STONE.id
glowstone = block.GLOWSTONE_BLOCK.id


def playGame():
    #build the board
    pos = mc.player.getTilePos()

    mc.setBlocks(pos.x - 1, pos.y, pos.z + 3, pos.x + 1, pos.y +2, pos.z +3, stone)

    #countdown
    mc.postToChat("Get ready ...")
    time.sleep(1)
    mc.postToChat("3...")
    time.sleep(1)
    mc.postToChat("2...")
    time.sleep(1)
    mc.postToChat("1...")
    time.sleep(1)
    mc.postToChat("GO!")

    #light up blocks
    blocksLit = 0
    points = 0

    while blocksLit < 9:
        time.sleep(0.3)

        blocksLit += 1
        lightCreated = False
        while not lightCreated:
            xPos = pos.x + random.randint(-1, 1)
            yPos = pos.y + random.randint(0, 2)
            zPos = pos.z + 3

            if mc.getBlock(xPos, yPos, zPos) == stone:
                mc.setBlock(xPos, yPos, zPos, glowstone)
                lightCreated = True

        #register hits
        for hitBlock in mc.events.pollBlockHits():
            if mc.getBlock(hitBlock.pos.x, hitBlock.pos.y, hitBlock.pos.z) == glowstone:
                mc.setBlock(hitBlock.pos.x, hitBlock.pos.y, hitBlock.pos.z, stone)
                blocksLit -= 1
                points += 1


    #show message game over 
    mc.postToChat("Game Over. You scored " + str(points) + " points.")


#check button press
sensor = 23
gpio.setup(sensor, gpio.IN)

while True:
    sleep(0.2)
    if gpio.input(sensor) == 0:
        playGame()



##reset the status of all gpio pins
gpio.cleanup()
