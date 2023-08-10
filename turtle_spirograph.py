import random as rm
import turtle as t

t.colormode(255)

def random_color():
  r = rm.randint(0,255)
  g = rm.randint(0,255)
  b = rm.randint(0,255)
  return (r,g,b)

t.speed("fastest")

radius = int(input("Enter, the size of the circle : "))
cobj = t.Turtle()
i = int(input("Please, enter the number of circles: "))
while i > 0:
  cobj.color(random_color())
  cobj.circle(radius)
  current_heading = cobj.heading()
  cobj.setheading(current_heading + 10)
  i -= 1
