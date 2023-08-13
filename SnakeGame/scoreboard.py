from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
FILENAME = "highest_score.txt"


class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.score = 0
    self.highest_score = self.read_highest_score()
    self.color("white")
    self.penup()
    self.goto(0, 270)
    self.hideturtle()
    self.update_scoreboard()

  def read_highest_score(self):
    with open(FILENAME, mode="r") as hscore:
      return int(hscore.read())

  def update_highest_score(self):
    with open(FILENAME, mode="w") as hscore:
      return hscore.write(str(self.highest_score))

  def update_scoreboard(self):
    self.write(f"Score: {self.score} Highest Score: {self.highest_score}",
               align=ALIGNMENT,
               font=FONT)

  def game_over(self):
    self.update_highest_score()
    self.goto(0, 0)
    self.write("GAME OVER", align=ALIGNMENT, font=FONT)

  def increase_score(self):
    self.score += 1
    if self.score > self.highest_score:
      self.highest_score = self.score
    self.clear()
    self.update_scoreboard()
