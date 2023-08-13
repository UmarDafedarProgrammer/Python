from turtle import Turtle
FILENAME = "highest_level.txt"

class Score(Turtle):

  def __init__(self):
    super().__init__()
    self.level = 1
    self.highest_level = self.read_highest_score()
    self.hideturtle()
    self.penup()
    self.color("white")
    self.goto(-350, 250)
    self.update_score()

  def read_highest_score(self):
    file = open(FILENAME)
    high_score = int(file.read())
    file.close()
    return high_score

  def update_highest_score(self):
    file = open(FILENAME,mode="w")
    file.write(str(self.level))
    file.close()
    
  def update_score(self):
    self.clear()
    self.write(f"Level: {self.level}  Highest Level: {self.highest_level}",
               align="left",
               font=("Courier", 24, "normal"))

  def increase_level(self):
    self.level += 1
    self.update_score()
    self.update_highest_level()
    
  def update_highest_level(self):
    if self.level > self.highest_level:
      self.highest_level = self.level
    self.update_score()

  def game_over(self):
    if self.level > self.highest_level:
      self.update_highest_score()
    self.goto(0, 0)
    self.write("Game Over!", align="left", font=("Courier", 24, "normal"))
