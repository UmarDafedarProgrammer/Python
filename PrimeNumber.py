#Write your code below this line 👇
def prime_checker(number):
    prime_number = 0
    for i in range(2,number//2):
        if number % i == 0:
            prime_number = 1
    if prime_number == 1:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
