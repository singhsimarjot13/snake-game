import random
from turtle import Turtle
class food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("blue")
        self.speed("fastest")
        self.refreash()

    def refreash(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x,y)
