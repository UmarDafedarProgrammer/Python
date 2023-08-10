import turtle

turt = turtle.Turtle()
turt.shape("turtle")

for i in range(0,20):
  if i%2 == 0:
    turt.forward(10)
    turt.penup()
  else:
    turt.forward(10)
    turt.pendown()
