import turtle

turt = turtle.Turtle()
turt.shape("turtle")

k = 0
length = 200
color = ["red","green","yellow","pink","black"]
for sides in range(3,8):
  angle = 360/sides;
  turtle.color(color[k])
  k += 1
  while sides>0:
    turtle.forward(length)
    turtle.right(angle)
    sides -= 1
