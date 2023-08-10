import turtle as t

tur = t.Turtle()
screen = t.Screen()

def move_left():
  t.setheading(180)
  t.forward(10)

def move_up():
  t.setheading(90)
  t.forward(10)

def move_right():
  t.setheading(0)
  t.forward(10)

def move_down():
  t.setheading(270)
  t.forward(10)


screen.listen()
screen.onkey(key="w",fun=move_left)
screen.onkey(key="e",fun=move_up)
screen.onkey(key="r",fun=move_right)
screen.onkey(key="d",fun=move_down)
