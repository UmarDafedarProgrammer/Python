import turtle as t

tur = t.Turtle()

def move_forward():
  tur.forward(10)

screen = t.Screen()

screen.listen()
screen.onkey(key="space",fun=move_forward)
