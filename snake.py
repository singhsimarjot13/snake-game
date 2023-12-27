from turtle import Turtle
co=[(10,0),(-10,0),(-30,0)]
FORWARDING=20
class Snake:
 def __init__(self):
    self.score=0
    self.segment=[]

 def snake(self):
        for position in co:
            self.create(position)

 def create(self,position):
     square = Turtle()
     square.color("white")
     square.penup()
     square.shape("square")
     square.goto(position)
     self.segment.append(square)

 def extend(self):
         self.create(self.segment[-1].position())
 def movesnake(self):
        for seg_num in range(len(self.segment)-1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.segment[0].forward(FORWARDING)
 def up(self):
     if self.segment[0].heading()!=270:
      self.segment[0].setheading(90)
 def down(self):
     if self.segment[0].heading() != 90:
      self.segment[0].setheading(270)
 def left(self):
     if self.segment[0].heading() != 0:
      self.segment[0].setheading(180)
 def right(self):
     if self.segment[0].heading() != 180:
      self.segment[0].setheading(0)
 def reset(self):
     for seg in self.segment:
      seg.goto(1000,1000)
     self.segment.clear()
     self.snake()





