import random

print("""
 _____                       _____ _            _   _                 _               
|  __ \                     |_   _| |          | \ | |               | |              
| |  \/_   _  ___  ___ ___    | | | |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
| | __| | | |/ _ \/ __/ __|   | | | '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
| |_\ \ |_| |  __/\__ \__ \   | | | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
 \____/\__,_|\___||___/___/   \_/ |_| |_|\___| \_| \_/\__,_|_| |_| |_|_.__/ \___|_|
 """);

EASY_LEVEL_ATTEMPTS = 15
MEDIUM_LEVEL_ATTEMPTS = 10
HIGH_LEVEL_ATTEMPTS = 5

MaxNum = int(input("Choose the maximum number for the game: "))
RandomNumber = random.randint(1,MaxNum)

def ChooseDifficulty():
    print("Difficulty Levels are High, Medium, Low")
    Diff = input("Choose the Difficulty leel: ")
    if Diff == "High":
        NumberOfChances = HIGH_LEVEL_ATTEMPTS
    elif Diff == "Medium":
        NumberOfChances = MEDIUM_LEVEL_ATTEMPTS
    elif Diff == "Low":
        NumberOfChances = EASY_LEVEL_ATTEMPTS
    return NumberOfChances

def Validate():
  difference = guess - RandomNumber 
  if difference == 0:
    print("Congratulations!. You Guessed it right")
    return 0
  elif difference >= 10:
    print("Too High")
  elif difference <= -10:
    print("Too Low")
  elif difference > 5 and difference < 10:
    print("High")
  elif difference < -5 and difference > -10:
    print("Low")
  elif difference <= 5 and difference >= -5:
    print("Near")
  return 1

Lives = ChooseDifficulty()

while Lives > 0:
  guess = int(input("Guess the Number : "))
  res = Validate()
  if res ==  0:
    break
  else:
    Lives = Lives -1

if Lives == 0:
  print("Sorry!! Try again.")
  print(f"The correct number is {RandomNumber}")
