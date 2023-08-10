from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")

starting_pos = [(0,0),(-20,0),(-40,0)]

snake_list = []

for position in starting_pos:
  t = Turtle(shape="square")
  t.color("white")
  t.penup()
  t.goto(position)
  snake_list.append(t)

game_is_on = True

while game_is_on:
  screen.update()
  for seg in snake_list:
    if seg.xcor() > 290:
      seg.setheading(180)
    if seg.xcor() < -290:
      seg.setheading(0)
    seg.forward(10)
    
