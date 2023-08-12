from turtle import Screen
from player import Player
import time
from cars import Car
from score import Score

p = Player()
c = Car()
s = Score()

FINISH_LINE = 230
COLLISON_DISTANCE = 20 

screen = Screen()
screen.bgcolor("black")
screen.screensize(canvwidth=700, canvheight=500)
screen.title("Turtle Crossing")
screen.tracer(0)

screen.listen()
screen.onkey(fun=p.move,key="Up")

GameIsOn = True

while GameIsOn:
  time.sleep(0.1)
  screen.update()
  c.create_car()
  c.move_cars()
  
  if p.ycor() > FINISH_LINE:
    p.reset_pos()
    c.level_up()
    s.increase_level()
  
  for car in c.car_list:
    if car.distance(p) < COLLISON_DISTANCE:
      GameIsOn = False
      s.game_over()
