from mcpi.minecraft import Minecraft
mc=Minecraft.create()
list2d=[[5,15,24],[16,103,48]]
myID=mc.getPlayerEntityId('kevinhuang971104')
x,y,z=mc.entity.getTilePos(myID)
startx=x
for list1d in list2d:
    for i in list1d:
        mc.setBlock(x,y,z,i)
        x=x+1
    x=startx
    z=z+1