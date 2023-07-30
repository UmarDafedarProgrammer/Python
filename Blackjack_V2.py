############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
import random

cards = ['Ace',1,2,3,4,5,6,7,8,9,10,'King','Queen','Jack']

ComputerCards = []
MyCards = []
GameOver = ""
ComputerScore = 0
MyScore = 0
FirstDraw = True

def WelcomePage():
  print("BlackJack !!!")
  print("Options are:\n1.DrawTheCard \n2.ShowTheCards \n3.Show")
  
def DistributeCards():
  if len(ComputerCards) == 0:
    ComputerCards.append(random.choice(cards))
    MyCards.append(random.choice(cards))
    
  ComputerCards.append(random.choice(cards))
  MyCards.append(random.choice(cards))
  
def ShowTheCards():
  print(f"Your cards are : {MyCards}")
  print(f"Computers Card is : {ComputerCards[1]}")

def CalculateScore(inp):
  Score = 0
  for i in inp:
    if i == 'Ace' or i == "King" or i == "Queen" or i == "Jack":
      Score = Score + 10
    else:
      Score = Score + i

  return Score

def CheckTheScore():
  MyScore = CalculateScore(MyCards)
  ComputerScore = CalculateScore(ComputerCards)
  return MyScore,ComputerScore

def ShowTheScore(MyScore, ComputerScore):
  print(f"My score is :{MyScore}")
  print(f"Computer score is :{ComputerScore}")

def WhoisWinner(MyScore, ComputerScore):
  if MyScore > 21 and ComputerScore <=21:
    print("You are Busted!")
  elif MyScore <=21 and ComputerScore > 21:
    print("Computer is Busted")
  elif MyScore > 21 and ComputerScore > 21:
    print("Draw")
  elif MyScore > ComputerScore:
    print("You are winner")
  else:
    print("Computer is winner")
  
def Show():
  print(f"Your cards are : {MyCards}")
  print(f"Computers Card is : {ComputerCards}")

def Busted(MyScore, ComputerScore):
  if MyScore > 21 or ComputerScore > 21:
    if MyScore > 21:
      print("You are Busted!")
      return True
    if ComputerScore > 21:
      print("Computer is Busted")
      return True
    return False

def PlayTheGame():
  WelcomePage()
  DistributeCards()
  while True:
    option = int(input("Please Select an option.\n"))
    if option == 1:
      DistributeCards()
      MyScore, ComputerScore = CheckTheScore()
      if Busted(MyScore, ComputerScore):
        break
    elif option == 2:
      ShowTheCards()
    elif option == 3:
      Show()
      MyScore, ComputerScore = CheckTheScore()
      ShowTheScore(MyScore, ComputerScore)
      WhoisWinner(MyScore, ComputerScore)

    if option == 3:
      break

PlayTheGame()
