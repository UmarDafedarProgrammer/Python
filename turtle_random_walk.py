import turtle as t
import random

trt = t.Turtle()
trt.speed("fastest")
NumberOfSteps = int(input("Please, enter the number of steps: "))

colors = ["red","green","yellow","blue"]
direction = ["up","forward","down","back"]
t.pensize(5)
for i in range(0,NumberOfSteps):
  distance = random.randint(50,100)
  col_index = random.randint(0,3)
  dir_index = random.randint(0,3)
  t.color(colors[col_index])
  if dir_index == 0:
    pass
  elif dir_index == 1:
    t.right(180)
  elif dir_index == 2:
    t.right(90)
  elif dir_index == 3:
    t.right(270)

  t.forward(distance)
  
