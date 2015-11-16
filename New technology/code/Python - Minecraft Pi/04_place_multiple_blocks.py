from mcpi.minecraft import Minecraft
from mcpi import block
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

# setBlock(x, y, z, block.BLOCK_SORT.id, BLOCK_COLOUR)
# BLOCK_COLOUR only works with certain blocks


x, y, z = mc.player.getPos()

#place a row of blocks
mc.setBlocks(x+1, y, z, x+1, y, z+10, stone)
mc.setBlocks(x+2, y, z, x+2, y, z+10, grass)
mc.setBlocks(x+3, y, z, x+3, y, z+10, dirt)
mc.setBlocks(x+4, y, z, x+4, y, z+10, wood_planks)
mc.setBlocks(x+5, y, z, x+5, y, z+10, water)
mc.setBlocks(x+6, y, z, x+6, y, z+10, gold_ore)
mc.setBlocks(x+7, y, z, x+7, y, z+10, gold_block)
mc.setBlocks(x+8, y, z, x+8, y, z+10, diamond_block)
mc.setBlocks(x+9, y, z, x+9, y, z+10, neather_reactor_core)
mc.setBlocks(x+10, y, z, x+10, y, z+10, wool)
mc.setBlocks(x+11, y, z, x+11, y, z+10, wool, 2)
mc.setBlocks(x+12, y, z, x+12, y, z+10, wool, 3)
mc.setBlocks(x+13, y, z, x+13, y, z+10, wool, 4)

