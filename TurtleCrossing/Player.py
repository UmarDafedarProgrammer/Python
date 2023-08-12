from turtle import Turtle

STARTING_POSITION = (0,-250)
DISTANCE = 10

class Player(Turtle):
  def __init__(self):
    super().__init__()
    self.color("white")
    self.shape("turtle")
    self.penup()
    self.setheading(90)
    self.reset_pos()

  def move(self):
    y_cor = self.ycor() + DISTANCE
    self.goto(0,y_cor)

  def reset_pos(self):
    self.clear()
    self.goto(STARTING_POSITION)
