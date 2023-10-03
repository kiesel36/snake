import random
#from matplotlib import animation
def move_snake(snake,direction:tuple):
    if len(direction)==2 and type(direction[0]) is int and type(direction[1]) is int:
        return snake[0]+direction[0],snake[1]+direction[1]
snake=(0,0)
print(snake)
#move snake by velocity ->(1,0) east or (-1,0) west or (0,1) north or (0,-1) south
directions=[(0,1),(1,0),(-1,0),(0,-1)]
#directs={"north":(0,1),"south":(0,-1),"east":(1,0),"west":(0,-1)}

for _ in range(10):
    direction=directions[random.randint(0,len(directions)-1)]
    snake=move_snake(snake,direction)
    print(snake)
#end snake=(2,2)