from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.color("red")
    self.shape("circle")
    self.penup()
    self.y_move = 10
    self.x_move = 10
    self.goto(0,0)

  def bounce_y(self):
    self.y_move *= -1

  def bounce_x(self):
    self.x_move *= -1
    
  def move(self):
    y_cor = self.ycor() + self.y_move
    x_cor = self.xcor() + self.x_move
    self.goto(x_cor,y_cor)

  def game_over(self):
    self.goto(0,0)
    self.color("white")
    self.write("Game Over!",align=ALIGNMENT,font=FONT)

  def reset_position(self):
    self.goto(0,0)
    
    
