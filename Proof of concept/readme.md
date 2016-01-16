# Proof of concept - Minecraft Pi

## Table of contents

1. Getting started with Minecraft Pi
2. Setup
3. Basics
4. Advanced scripts
5. Multiplayer


## 1. Getting started with Minecraft Pi

After installing Raspbian on the Raspberry Pi, you can get started playing with Minecraft Pi. You can manipulate the Minecraft world by writing scripts in Python. You can find the basic information on how to do this in the official Raspberry Pi Learning Resource: [Getting Started With Minecraft Pi](https://www.raspberrypi.org/learning/getting-started-with-minecraft-pi/worksheet/).

After trying these fun examples in Minecraft you can start creating your own creative stuff by using the full [Minecraft Pi API Reference](http://www.stuffaboutcode.com/p/minecraft-api-reference.html).

## 2. Setup



## 3. Basics

Here are some of the basics on manipulating the Minecraft world.

### 3.1 Use the Python programming interface

You can create a connection between Python 3 and Minecraft by using the following code:

```Python
from mcpi.minecraft import Minecraft

mc = Minecraft.create()
```

Post messages in chat by using the `mc.postToChat()` function.

```Python
mc.postToChat("Hello World! How's Steve?")
```

### 3.2 Setting the position of your player

Find your location in the world:

```Python
pos = mc.player.getPos()
```

Now you have access to your coordinates via the `pos` variable => `pos.x`, `pos.y` and `pos.z`.

You can also save it directly to `x`, `y` and `z` by using the following code.

```Python
x, y, z = mc.player.getPos()
```

Now that you have your location you can define your new location in relation to your current location or the world.

```Python
# in relation to your current position
mc.player.setPos(x, y+20, z+20)

# in relation to the base coordinates of the world
mc.player.setPos(10, 10, 10)
```

### 3.3 Placing a block

To place a single block use `mc.setBlock(x, y, z, block_id)`.

```Python
x, y, z = mc.player.getPos()

mc.setBlock(x+5, y, z, 1)
```

Of course it's a bit hard to remember the block ids of all blocks in Minecraft, so you'll probably want to use block constants. You can do this by importing the block module.

```Python
from mcpi import block
```

Now you can access block ids by using the blocks name, like this:

```Python
stone = block.STONE.id
wood_planks = block.WOOD_PLANKS.id
gold_ore = block.GOLD_ORE.id
gold_block = block.GOLD_BLOCK.id
```

Pretty easy right!

### 3.4 Special blocks

Some blocks have extra properties. For example you can specify the color of wool. You can set this extra property by including an extra parameter in `setBlock()`.

```Python
wool = block.WOOL.id
wool_color_white = 0  #default
wool_color_orange = 1
wool_color_magenta = 2

mc.setBlock(x, y, z, wool, wool_color_magenta)
```

To have a full list of blocks which have extra properties, see the [API Reference](http://www.stuffaboutcode.com/p/minecraft-api-reference.html).

### 3.5 Placing multiple blocks

To place multiple blocks in one line of code you can use the `setBlocks()` function.

```Python
stone = block.STONE.id
x, y, z = mc.player.getPos()

mc.setBlocks(x, y, z, x+5, y+5, z+5, stone)
```

### 3.6 Placing blocks as you walk

You've just learned how to get your location and place blocks, so let's combine these and place a grass block below you with a flower on top.

```Python
from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

grass = block.GRASS.id
flower = block.FLOWER.id

while True:
  x, y, z = mc.player.getPos()  #get your location
  mc.setBlock(x, y-1, z, grass) #place a grass block below you
  mc.setBlock(x, y, z, flower)  #place a flower on the block you just placed
  sleep(0.1)
```

The wile loop will go on forever, so to stop the script hit `Ctrl + C` in the Python window or close the Python window. 


## 4. Advanced scripts

## 5. Multiplayer


## Scripts

- dropping_blocks_as_you_walk.py: Dropping blocks and flowers where you walk
- stairs.py: Build stairs a few blocks away from you
- pacman.py: PACMAN EATS ALL
- cage.py: LOL
- lightsensor_mc.py: placing blocks based in input from lightsensor
- whac-a-block.py: Whac-a-Block game 3x3 blocks hit them to whac
