from mcpi.minecraft import Minecraft

mc = Minecraft.create()

#pos = mc.player.getPos()
x,y,z = mc.player.getPos()

#mc.postToChat(pos)

mc.player.setPos(x, y+50, z)
