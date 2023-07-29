dict = {1:"one",2:"two",3:"three"}

print(dict)
print(f"{dict[1]}, {dict[2]}, {dict[3]}")

for key in dict:
  print(f"{key}:{dict[key]}")

dict = {} # Wipes out the data
