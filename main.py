from turtle import Screen
from snake import Snake
import time
from food import food
from scoreboard import scoreboard
from scoreboard import ALIGN,FONT
screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.tracer(0)
cobra=Snake()
food=food()
score=scoreboard()
cobra.snake()
screen.listen()
screen.onkey(cobra.up,"Up")
screen.onkey(cobra.down,"Down")
screen.onkey(cobra.left,"Left")
screen.onkey(cobra.right,"Right")

game=True
while game:
 time.sleep(0.1)

 cobra.movesnake()
 if cobra.segment[0].distance(food) <15:
  food.refreash()
  score.clear()
  score.score+=1
  score.again()
  cobra.extend()
 if cobra.segment[0].xcor() >280 or cobra.segment[0].xcor()<-280 or cobra.segment[0].ycor()>280 or cobra.segment[0].ycor()<-280:
    score.reset()
    cobra.reset()
    score.record()
  # cobra.segment[0].goto(1000,1000)
  # cobra.snake()
  # detect collision with tail

 for segment in cobra.segment[1:]:
  # if segment==cobra.segment[0]:
  #  continue
  if cobra.segment[0].distance(segment)<15:
    score.reset()
    cobra.reset()
    score.record()
   # cobra.segment[0].goto(1000,1000)
   # cobra.snake()

 screen.update()


screen.exitonclick()