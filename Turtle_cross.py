from turtle import Screen
import time
from player import Player
from cars import Cars
import random as r
from turtlecrosswriter import TurtleCrossWriter

screen = Screen()
screen.bgcolor("white")
screen.setup(600,600)
screen.tracer(0)

game_is_on=True

player = Player()
screen.listen()
dis = 10
li=[]
m=10
#while car.xcor() > -300:
n=1
level = 1
tcw = TurtleCrossWriter()
tcw.writer(level)
acc=22
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    screen.onkey(player.move,"Up")
    if n<2:
        car = Cars()
        li.append(car)
        n=n+1
    elif n>=2:
        n=1
    
    for car in li:
        if car.xcor() > -320:
            car.go(m)
        if player.distance(car) < acc:
            game_is_on = False
            tws = TurtleCrossWriter()
            tws.gameover()
            time.sleep(1)
            #screen.exitonclick()
            screen.bye()
            

            
            

    if player.ycor()>300:
        player.goto(0,-280)
        m=m+5
        level = level+1
        if acc > 0:
            acc=acc-2
        else:
            acc=10
        tcw.clear()
        tcw = TurtleCrossWriter()
        tcw.writer(level)
        
    
    #game_is_on = False
    #    i=i-1

