from turtle import Turtle, Screen
import time

############ CONSTANTS
STARTING_POS = [(0,0),(-20,0),(-40,0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

######## Screen Setup
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) # Turn Off the animation

############  Snake Classs
class Snake:
  def __init__(self):
    self.segments = []
    self.create_snake()
    self.head = self.segments[0]

  def create_snake(self):
    for position in STARTING_POS:
      new_segment = Turtle("square")
      new_segment.color("white")
      new_segment.penup()
      new_segment.goto(position)
      self.segments.append(new_segment)

  def move(self):
    for seg_index in range(len(self.segments)-1,0,-1):      
      self.segments[seg_index].goto(self.segments[seg_index-1].xcor(),self.segments[seg_index-1].ycor())
    self.segments[0].forward(MOVE_DIST)

  def up(self):
    if self.head.heading() != DOWN:
      self.segments[0].setheading(UP)

  def down(self):
    if self.head.heading() != UP:
      self.segments[0].setheading(DOWN)

  def right(self):
    if self.head.heading() != LEFT:
      self.segments[0].setheading(RIGHT)

  def left(self):
    if self.head.heading() != RIGHT:
      self.segments[0].setheading(LEFT)

##############Create Snake Object
snake = Snake()

##############Event Listeners
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")


############## Movement
game_is_on = True

while game_is_on:
  screen.update()
  time.sleep(0.1)
  snake.move()
