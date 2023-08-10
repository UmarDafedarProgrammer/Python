import turtle as t
import random

race_on = False
screen = t.Screen()
screen.setup(width=500,height=400)

user_choice = screen.textinput(title="Choose your champion",prompt="Your choice")

color_list = ["red","green","yellow","blue","black","purple","pink"]
turtle_list = []

y_coordinate = 0

if user_choice:
  race_on = True
  
for i in range(0,7):
  turt = t.Turtle(shape = "turtle")
  turt.penup()
  turt.goto(-250,y_coordinate)
  turt.color(color_list[i])
  y_coordinate = y_coordinate + 30
  turtle_list.append(turt)

while race_on:
  #distance = [random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10)]
  for turtle in turtle_list:
    if turtle.xcor() > 240:
      race_on = False
      winning_color  = turtle.pencolor()
      if winning_color == user_choice:
        print("You Won")
      else:
        print(f"You lose, {winning_color} turtle won")
    else:
      turtle.forward(random.randint(0,10))
