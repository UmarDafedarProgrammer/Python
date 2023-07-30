# 🚨 Don't change the code below 👇
inp = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
def is_leap_year(year):
  if year%4 == 0:
    if year%100 == 0:
      if year%400 ==0:
        return True
      else:
        return False
    else:
        return True
  else:
    return False

def Days_in_Feb():
  if is_leap_year(inp):
    return 29
  else:
    return 28

print(f"{inp}-{Days_in_Feb()}")
