class Snake():
    __pixels=[]
    def __init__(self,length_0:int,pos_0:tuple):
        self.__length=length_0
        self.__head_pos=pos_0
        self.__direct=(1,0)
        for pixel in range(self.__length):
            self.__pixels.append(SnakePixel(self.__head_pos[0]+pixel*self.__direct[0],self.__head_pos[1]+pixel*self.__direct[1]))
    def move(self,x_direction:int,y_direction:int):
        if x_direction>0 and y_direction>0: #nort east
            self.__head_pos[0]+=1
            self.__head_pos[1]+=1
        elif x_direction>0 and y_direction==0:#east
            self.__head_pos[0]+=1
        elif x_direction>0 and y_direction<0:#south east
            self.__head_pos[0]+=1
            self.__head_pos[1]-=1
        elif x_direction==0 and y_direction<0:#south
            self.__head_pos[1]-=1
        elif x_direction<0 and y_direction<0:#south west
            self.__head_pos[0]-=1
            self.__head_pos[1]-=1
        elif x_direction<0 and y_direction==0:#west
            self.__head_pos[1]-=1
        elif x_direction<0 and y_direction>0:#north west
            self.__head_pos[0]-=1
            self.__head_pos[1]+=1
        else:#north
            self.__head_pos[1]+=1
        del(self.__pixels[-1])
        
class SnakePixel():
    def __init__(self,p:tuple):
        self.__position=p