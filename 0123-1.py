from mcpi.minecraft import Minecraft
mc=Minecraft.create()

from random import choice

a=[3,9,12,15,29,300,75]

r=choice(a)
print(r)


myID=mc.getPlayerEntityId("kevinhuang971104")
x,y,z=mc.entity.getTilePos(myID)
mc.setBlock(x,y,z,r)