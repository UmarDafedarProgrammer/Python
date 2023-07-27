import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line👇
options = [rock,paper,scissors]
user = int(input("Choose your option \n0. Rock\n1. Paper\n3.Scissors\n"))
comp = random.randint(0,2)

if user == comp:
  print(f"You Chose: \n {options[user]}")
  print(f"Computer Chose: \n {options[comp]}")
  print("Try Again!!")
else:
  if (user == 0 and comp == 1) or (user == 1 and comp == 2) or (user == 2 and comp == 0):
    print(f"You Chose: \n {options[user]}")
    print(f"Computer Chose: \n {options[comp]}")
    print("You Lose !!")
  else:
    print(f"You Chose: \n {options[user]}")
    print(f"Computer Chose: \n {options[comp]}")
    print("You Win !!!")
