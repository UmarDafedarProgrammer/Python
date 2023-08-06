print("""
  ___                                   _   _      _       _     _   
 / _ \                                 | | | |    (_)     | |   | |  
/ /_\ \_   _____ _ __ __ _  __ _  ___  | |_| | ___ _  __ _| |__ | |_ 
|  _  \ \ / / _ \ '__/ _` |/ _` |/ _ \ |  _  |/ _ \ |/ _` | '_ \| __|
| | | |\ V /  __/ | | (_| | (_| |  __/ | | | |  __/ | (_| | | | | |_ 
\_| |_/ \_/ \___|_|  \__,_|\__, |\___| \_| |_/\___|_|\__, |_| |_|\__|
                            __/ |                     __/ |          
                           |___/                     |___/           
""")
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

TotalHeight = 0
#Write your code below this row 👇
for height in student_heights:
    TotalHeight += height

AvgHeight = round(TotalHeight / len(student_heights))
print(AvgHeight)

AvgHeight = round(sum(student_heights)/len(student_heights))
print(AvgHeight)
