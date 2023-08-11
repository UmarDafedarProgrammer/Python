from turtle import Turtle, Screen
import time
import random

############ CONSTANTS
STARTING_POS = [(0,0),(-20,0),(-40,0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

######## Screen Setup
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) # Turn Off the animation

############  Snake Classs
class Snake:
  def __init__(self):
    self.segments = []
    self.create_snake()
    self.head = self.segments[0]

  def create_snake(self):
    for position in STARTING_POS:
      self.add_segment(position)

  def add_segment(self, position):
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    self.segments.append(new_segment)

  def extend(self):
    self.add_segment(self.segments[-1].position())
    
  def move(self):
    for seg_index in range(len(self.segments)-1,0,-1):      
      self.segments[seg_index].goto(self.segments[seg_index-1].xcor(),self.segments[seg_index-1].ycor())
    self.segments[0].forward(MOVE_DIST)

  def up(self):
    if self.head.heading() != DOWN:
      self.segments[0].setheading(UP)

  def down(self):
    if self.head.heading() != UP:
      self.segments[0].setheading(DOWN)

  def right(self):
    if self.head.heading() != LEFT:
      self.segments[0].setheading(RIGHT)

  def left(self):
    if self.head.heading() != RIGHT:
      self.segments[0].setheading(LEFT)

############## Food class
class Food(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.penup()
    self.shapesize(stretch_len=0.5,stretch_wid=0.5)
    self.color("blue")
    self.speed("fastest")
    # random_x = random.randint(-280,280)
    # random_y = random.randint(-280,280)
    # self.goto(random_x,random_y)
    self.refresh()

  def refresh(self):
    random_x = random.randint(-280,280)
    random_y = random.randint(-280,280)
    self.goto(random_x,random_y)

############ ScoreBoard Class
class ScoreBoard(Turtle):
  def __init__(self):
    super().__init__()
    self.score = 0
    ##self.shape("dot")
    self.color("white")
    self.penup()
    self.goto(0,280)
    self.hideturtle()
    self.update_scoreboard()
    
  def update_scoreboard(self):
    self.write(f"Score: {self.score}",align="center")

  def increasescore(self):
    self.score += 1
    self.clear()
    self.update_scoreboard()

  def gameover(self):
    self.goto(0,0)
    self.write(" Game Over! ")
    
##############Create Snake Object
snake = Snake()
food = Food()
score = ScoreBoard()

##############Event Listeners
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")


############## Movement
game_is_on = True

while game_is_on:
  screen.update()
  time.sleep(0.1)
  snake.move()

  #Detect the collision between food and snake head
  if snake.head.distance(food) < 15:
    food.refresh()
    snake.extend()
    score.increasescore()
    ## update the score
    ## Add the turtle

  #Detect Colliso with Wall
  if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    game_is_on = False
    score.gameover()
