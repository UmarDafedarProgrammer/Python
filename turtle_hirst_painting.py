import colorgram as c
import turtle  as t
import random
t.colormode(255)

rgb_colors = []
colors = c.extract("hirst_painting.jpg",20)
for color in colors:
  r = color.rgb.r
  g = color.rgb.g
  b = color.rgb.b
  rgb_colors.append((r,g,b))
  
print(rgb_colors)

turt = t.Turtle()
t.penup()
t.setheading(225)
t.forward(250)
t.setheading(0)
numberofdots = 100

for dot_count in range(1,numberofdots+1):
  t.pendown()
  t.dot(20, random.choice(rgb_colors) )
  t.penup()
  t.forward(50)

  if dot_count%10 == 0:
    t.setheading(90)
    t.forward(50)
    t.setheading(180)
    t.forward(500)
    t.setheading(0)
