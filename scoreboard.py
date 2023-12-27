from turtle import Turtle
ALIGN="center"
FONT=("courier",20,"normal")
class scoreboard(Turtle):
    def __init__(self):
     super().__init__()
     self.score=0
     with open("data.txt") as data:
         self.best=int(data.read())
     self.color("white")
     self.hideturtle()
     self.penup()
     self.again()


    def again(self):
        self.clear()
        self.goto(-100, 260)
        self.write(f"Score={self.score} ", align=ALIGN, font=FONT)
        self.goto(100,260)
        self.write(f"Best score={self.best} ", align=ALIGN, font=FONT)



    def reset(self):
        if self.best < self.score:
            self.best = self.score
        self.score = 0
        self.again()
    def record(self):
        with open("data.txt",mode='w') as data:
            data.write(str(self.best))
