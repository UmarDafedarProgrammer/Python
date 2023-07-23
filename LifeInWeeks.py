# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
ExpectedAge = 90
ageinfloat = float(age)
NumOfDaysPerYear = 365
NumOfWeeksPerYear = 52
NumOfMonthPerYear = 12

DaysLeft = int((ExpectedAge -ageinfloat) * NumOfDaysPerYear)
MonthsLeft = int((ExpectedAge -ageinfloat) * NumOfMonthPerYear)
WeeksLeft = int((ExpectedAge -ageinfloat) * NumOfWeeksPerYear)

print(f"You have {DaysLeft} days, {WeeksLeft} weeks, and {MonthsLeft} months left.")



