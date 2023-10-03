class Auto():
    def __init__(self,t:str,c="red",p=(0,0)):
        """constructor of the auto class

        Args:
            t (str): string that descript the type of the auto, ex. limo,combi,bobicar
            c (str): string that defines the color of the auto, of cource a bobicar must be red
        """
        if t=="bobicar":
            self.type=t
            self.color="red"
        else:
            self.type=t
            self.color=c
        if type(p[0]) is int and type(p[1]) is int:
            self.pos=p
    def drive(self,time:int,velocity:tuple):
        """change the position atribute to simul    ate driving 

        Args:
            time (int): represent the time
            velocity (list): represent 

        Returns:
            void
        """
        if type(velocity[0]) is int and type(velocity[1]) is int:
            for _ in range(1,time):
                self.locate((self.pos[0]+velocity[0],self.pos[1]+velocity[1]))
    def locate(self,p:list):
        if len(p)==2 and type(p[0]) is bool and type(p[1]) is bool and type(self.pos)is not None:
            self.pos=p 
class Person:
    pass
class Driver(Person):
    pass 
def carscolided(c1:Auto,c2:Auto):
    return c1.pos==c2.pos
if __name__=="__main__":
    car1=Auto("bobicar")
    car2=Auto("limo","blue")
    car1.locate((1,2))
    car2.locate((2,4))
    car1.drive(1,(2,3))
    car2.drive(1,(1,1))
    print(carscolided(car1,car2))
    car2.drive(2,(2,3))
    print(carscolided(car1,car2))
    