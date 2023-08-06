# When, global and local variables and functions are having same name, then the precedence is given to local scope variable and function.
# Global member can be accessed within any of the function and segments
# Functions and variables defined within function definition can not be accessed outside the local scope

name = "Global"
City = "London"

def ResetName():
  name = "Local"
  Weather = "Cold"
  print(f"Local Name is : {name}")
  print(f"Local City is : {City}")
  print(f"City Weather is : {Weather}")
  
ResetName()
print(f"Global Name is : {name}")
print(f"Global City is : {City}")
#print(f"City Weather is : {Weather}") Can not be accessed outsie
