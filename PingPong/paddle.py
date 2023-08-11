from turtle import Turtle

DIST = 10
Y_COR = 200


class Paddle(Turtle):

  def __init__(self, position):
    super().__init__()
    self.color("white")
    self.shape("square")
    self.penup()
    self.shapesize(stretch_wid=5, stretch_len=1)
    self.goto(position)

  def up(self):
    y_cor = self.ycor() + DIST
    if y_cor < Y_COR:
      self.goto(self.xcor(), y_cor + DIST)

  def down(self):
    y_cor = self.ycor() - DIST
    if y_cor >= -Y_COR:
      self.goto(self.xcor(), y_cor - DIST)
