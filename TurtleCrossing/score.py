from turtle import Turtle

class Score(Turtle):
  def __init__(self):
    super().__init__()
    self.level = 1
    self.hideturtle()
    self.penup()
    self.color("white")
    self.goto(-350,250)
    self.update_score()

  def update_score(self):
    self.clear()
    self.write(f"Level: {self.level}",align="left",font=("Courier",24,"normal"))

  def increase_level(self):
    self.level += 1
    self.update_score()

  def game_over(self):
    self.goto(0,0)
    self.write(f"Game Over!",align="left",font=("Courier",24,"normal"))
