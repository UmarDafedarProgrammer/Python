# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# TRUE LOVE
name1lower = name1.lower()
name2lower = name2.lower()

arr1 = ['t','r','u','e']
arr2 = ['l','o','v','e']
num1 = num2= 0

for a in arr1:
    num1 += name1lower.count(a)
    num1 += name2lower.count(a)
print(num1)

for a in arr2:
    num2 += name2lower.count(a)
    num2 += name1lower.count(a)
print(num2)

Score = int(str(num1)+str(num2))

if Score <10 or Score>90:
    print(f"Your score is {Score}, you go together like coke and mentos.")
elif Score>40 and Score<50:
    print(f"Your score is {Score}, you are alright together.")
else:
    print(f"Your score is {Score}.")
