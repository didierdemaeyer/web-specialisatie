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

bedrock = block.BEDROCK.id
lava = block.LAVA.id


#get players in the server
entityIds = mc.getPlayerEntityIds()
i = 0
players = [10]
while  i < len(entityIds):
    players[i] = entityIds[i]
    i += 1


## x1, y1, z1 = mc.entity.getPos(players[0])   # pos first player connected
## x2, y2, z2 = mc.entity.getPos(players[1]) # pos of second player connected


# build a cage
def buildCage():
    #get my pos
    global x, y, z
    x, y, z = mc.player.getPos()
    x += 10
    y -= 1

    #floor
    mc.setBlocks(x, y, z-2, x+4, y, z+2, bedrock)
    sleep(0.5)

    layer = 0

    while layer < 3:
        y += 1
        layer += 1
        
        if layer != 2:
            mc.setBlock(x, y, z-2, bedrock)
            mc.setBlock(x, y, z-1, bedrock)
            mc.setBlock(x, y, z, bedrock)
            mc.setBlock(x, y, z+1, bedrock)
            mc.setBlock(x, y, z+2, bedrock)
            mc.setBlock(x+1, y, z-2, bedrock)
            mc.setBlock(x+1, y, z+2, bedrock)
            mc.setBlock(x+2, y, z-2, bedrock)
            mc.setBlock(x+2, y, z+2, bedrock)
            mc.setBlock(x+3, y, z-2, bedrock)
            mc.setBlock(x+3, y, z+2, bedrock)
            mc.setBlock(x+4, y, z-2, bedrock)
            mc.setBlock(x+4, y, z-1, bedrock)
            mc.setBlock(x+4, y, z, bedrock)
            mc.setBlock(x+4, y, z+1, bedrock)
            mc.setBlock(x+4, y, z+2, bedrock)
            sleep(0.5)

    #roof
    mc.setBlocks(x, y+1, z-2, x+4, y+1, z+2, bedrock)
    sleep(0.5)



# put player in cage
def cagePlayer():
    mc.entity.setPos(players[0], x+2, y-2, z)
    sleep(2)

#fill cage with lava
def fillCageWithLava():
    mc.setBlock(x+2, y+1, z, air) #open roof
    mc.setBlock(x+2, y+2, z, lava) #place lava
    sleep(2)


sensor = 23
gpio.setup(sensor, gpio.IN)
inputcount = 0

while True:
    sleep(0.2)
    if gpio.input(sensor) == 0:
        if inputcount == 0:
            buildCage()
            inputcount += 1
            
        elif inputcount == 1:
            cagePlayer()
            inputcount += 1
            
        elif inputcount == 2:
            fillCageWithLava()
            inputcount = 0
            

