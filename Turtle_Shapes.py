import turtle

turt = turtle.Turtle()
turt.shape("turtle")

k = 0
length = 200
color = ["red","green","yellow","pink","black"]
for i in range(3,8):
  angle = 360/i;
  turtle.color(color[k])
  k += 1
  for i in range(0,i):
    turtle.forward(length)
    turtle.right(angle)
