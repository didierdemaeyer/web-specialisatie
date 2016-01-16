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

mc.postToChat("Hello World")

```

## 4. Advanced scripts

## 5. Multiplayer
