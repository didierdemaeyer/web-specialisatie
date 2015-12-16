from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

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


# uncomment to place flowers where you walk every 100ms
while True:
    x, y, z = mc.player.getPos()
    mc.setBlock(x, y, z, flower)
    sleep(0.1)



# uncomment to place blocks below you serving as ground
##while True:
##    x, y, z = mc.player.getPos()
##    mc.setBlock(x, y-1, z, stone)
##    sleep(0.1)



# uncomment to place flowers on grass blocks you walk on
##while True:
##    x, y, z = mc.player.getPos()
##    block_beneath = mc.getBlock(x, y-1, z)  # block ID
##
##    if block_beneath == grass:
##        mc.setBlock(x, y, z, flower)
##    sleep(0.1)



#uncomment to place grass blocks where you walk and place flowers on them
##while True:
##    x, y, z = mc.player.getPos()
##    block_beneath = mc.getBlock(x, y-1, z)  # block ID
##
##    if block_beneath == grass:
##        mc.setBlock(x, y, z, flower)
##    else:
##        mc.setBlock(x, y-1, z, grass)
##        mc.setBlock(x, y, z, flower)
##    sleep(0.1)
    


