from turtle import Turtle
import random

COLOR_LIST = ["red","green","blue","pink","violet","indigo","yellow","orange"]
STARTING_CAR_DISTANCE = 250
MOVE_INCREMENT = 1
STARTING_SPEED = 5

class Car(Turtle):
  def __init__(self):
    super().__init__()
    self.car_list = []
    self.car_speed = STARTING_SPEED

  def create_car(self):
    random_chance = random.randint(1,6)
    if random_chance == 1:
      new_car = Turtle("square")
      new_car.shapesize(0.5,2)
      new_car.color(random.choice(COLOR_LIST))
      new_car.penup()
      random_y = random.randint(-220,220)
      new_car.goto(STARTING_CAR_DISTANCE,random_y)
      self.car_list.append(new_car)

  def move_cars(self):
    for car in self.car_list:
      car.backward(self.car_speed)

  def level_up(self):
    self.car_speed += MOVE_INCREMENT  
