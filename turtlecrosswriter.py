from turtle import Turtle

class TurtleCrossWriter(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        
    def writer(self,num):
        self.goto(-260,270)
        self.write(f"Level: {num}",font=("Arial", 15, "normal"),align="center")
    def gameover(self):
        self.goto(0,0)
        self.write("Game Over!",font=("Arial", 15, "normal"),align="center")
        
