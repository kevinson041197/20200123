from mcpi.minecraft import Minecraft
mc=Minecraft.create()

while True:
    chat =mc.events.pollChatPosts()
    #ChatEvent(chatEvent.POST,57,"嗨嗨憨兒)
    if len (chat)>0:    
        strchat=str(chat[0])
        length=len(strchat)

        comma1=strchat.find(",",0)  
        comma2=strchat.find(",",comma1+1)
    
        myID=strchat[comma1+1:comma2]
        myID=int(myID)
        message=strchat[comma2:length-1]
        name=mc.entity.getName(myID)
        x,y,z=mc.entity.getTilePos(myID)
        mc.setSign(x,y,z,63,0,name,"",message)