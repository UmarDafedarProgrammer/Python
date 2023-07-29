import random
from replit import clear

print("Welcome to Silent/Blind Auction 🔨 🔨 🔨 ")
StartingBid = int(input("Starting Bid is: $"))
BiddingList = {}

name = input("Please Enter your name : ")
Amount = input("Please, place your bid: $")
BiddingList[name] = Amount

StopBidding = False

while not StopBidding:
  clear()
  Cont = input("Others want to Participate Y/N?: ")
  if Cont == "N":
    StopBidding = True
    break
  name = input("Please Enter your name : ")
  Amount = random.randint(StartingBid, 5*StartingBid)
  BiddingList[name] = Amount

WinnerAmount = 0
Winner = ""

for key in BiddingList:
  if int(BiddingList[key]) > WinnerAmount:
    WinnerAmount = int(BiddingList[key])
    Winner = key

print(BiddingList)

print(f"Congratulations !! {Winner}. You Bid ${WinnerAmount} and have won.")
