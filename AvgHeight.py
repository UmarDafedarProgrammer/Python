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
