#imports
import pygame
import random
import math
import screeninfo
import datetime
import Snake as sn
if __name__ =="__main__":
    #setup
    pygame.init()
    #get primary Monitor shape
    for monitor in screeninfo.get_monitors():
        if monitor.is_primary:
            height=monitor.height
            width=monitor.width
    screen=pygame.display.set_mode(size=(height,width))#,flags=pygame.FULLSCREEN)
    #screen=pygame.display.set_mode(flags=pygame.FULLSCREEN)
    length,width=pygame.display.get_window_size()
    #pos_0=(random.randint(0,int(math.floor(length/2))),random.randint(0,int(math.floor(width/2))))
    clock=pygame.time.Clock()
    running=True
    #snake=sn.Snake(3,(random.randint(0,int(math.floor(min(width,length)/2*100))),random.randint(0,int(math.floor(min(width,length)/2*100)))))
    #setup logging
    log_action=open("action.log","w") 
    log_debug=open("debug.log","w")
    #mainloop
    while running:
        act_event=None
        for event in pygame.event.get():#
            act_event=event
            if act_event.type==event.type:
                act=False
            if event.type==pygame.QUIT:
                running=False
            elif event.type==pygame.K_UP and act:
                #screen.unlock()
                screen.set_at((10,10),(255,255,255))
            elif event.type==pygame.K_DOWN and act:
                pass
            elif event.type==pygame.K_LEFT and act:
                pass
            elif event.type==pygame.K_RIGHT and act:
                pass
            else:
                #if event.type is 
                log_action.write("Event: %s at time: %s not recognized\n"%(pygame.event.event_name(event.type),str(datetime.datetime.now())))
            log_debug.write("Event: %s at time: %s recognized\n"%(str(event),str(datetime.datetime.now())))
        clock.tick(60)
    #quit
    log_action.close()
    log_debug.close()
    pygame.quit()