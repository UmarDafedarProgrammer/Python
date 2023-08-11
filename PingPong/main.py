from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

## Screen Setup
screen = Screen()
ball = Ball()
screen.bgcolor("black")
screen.setup(width=500, height=500)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((250, 0))
l_paddle = Paddle((-250, 0))
############## Event Listeners
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
game_is_on = True

while game_is_on:
  time.sleep(0.1)
  screen.update()
  ball.move()

  if ball.ycor() > 230 or ball.ycor() < -230:
    ball.bounce_y()

  if ball.distance(r_paddle) < 50 and ball.xcor() > 220 or ball.distance(l_paddle) < 50 and ball.xcor() < -220:
    ball.bounce_x()

  if ball.xcor() > 230 or ball.xcor() < -230:
    ball.game_over()
    break

screen.exitonclick()
