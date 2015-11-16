from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()

x, y, z = mc.player.getPos()

# setBlock(x, y, z, block.BLOCK_SORT.id, BLOCK_COLOUR)
# BLOCK_COLOUR only works with certain blocks

mc.setBlock(x+1, y, z, 1)

# replaces  existing block
mc.setBlock(x+1, y, z, block.NETHER_REACTOR_CORE.id)


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

#place a row of blocks
mc.setBlock(x+1, y, z, stone)
mc.setBlock(x+2, y, z, grass)
mc.setBlock(x+3, y, z, dirt)
mc.setBlock(x+4, y, z, wood_planks)
mc.setBlock(x+5, y, z, water)
mc.setBlock(x+6, y, z, gold_ore)
mc.setBlock(x+7, y, z, gold_block)
mc.setBlock(x+8, y, z, diamond_block)
mc.setBlock(x+9, y, z, neather_reactor_core)
mc.setBlock(x+10, y, z, wool)
mc.setBlock(x+11, y, z, wool, 2) # BLOCK_COLOUR
mc.setBlock(x+12, y, z, wool, 3)
mc.setBlock(x+13, y, z, wool, 4)



