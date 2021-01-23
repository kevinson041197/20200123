from mcpi.minecraft import Minecraft
mc=Minecraft.create()

myID=mc.getPlayerEntityId('kevinhuang971104')
x,y,z=mc.entity.getTilePos(myID)
try:
    block=int(input("請輸入方塊ID"))
    mc.setBlock(x,y,z,block)
except:
    print("only number")