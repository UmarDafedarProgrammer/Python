from resources import resources
from resources import recipe
import time
import os


# To Print the Inventory details
def report_resources():
    print("Resources Details")
    print(f'Milk    - {resources["milk"]}ml')
    print(f'Water   - {resources["water"]}ml')
    print(f'Coffee  - {resources["coffee"]}gm')
    print(f'Honey   - {resources["honey"]}ml')


# Check, if sufficient ingredients are available
def check_if_sufficient(i_coffee):
    recipe_required = recipe[i_coffee]
    if (recipe_required["water"] <= resources["water"] and recipe_required["milk"] <= resources["milk"] and
            recipe_required["coffee"] <= resources["coffee"] and recipe_required["honey"] <= resources["honey"]):
        print("Sufficient resources are available")
        return True
    else:
        print("Sufficient resources are not available")
        return False


def deduct_the_resources(i_coffee):
    recipe_required = recipe[i_coffee]
    resources["water"] = resources["water"] - recipe_required["water"]
    resources["milk"] = resources["milk"] - recipe_required["milk"]
    resources["coffee"] = resources["coffee"] - recipe_required["coffee"]
    resources["honey"] = resources["honey"] - recipe_required["honey"]


def receive_the_payment(i_coffee):
    amt = float(input(f'Its {recipe[i_coffee]["price"]}. '))
    resources["money"] = resources["money"] + recipe[i_coffee]["price"]
    if amt != recipe[i_coffee]["price"]:
        print(f'Here, your change {amt - recipe[i_coffee]["price"]}')


def preparing():
    print("Thank You, Your coffee is getting ready !")
    for i in range(1,5):
        print("*")
        time.sleep(2)


def make_coffee():
    preparing()
    deduct_the_resources("Espresso")
    receive_the_payment("Espresso")


def welcome_logo():
    print("""
 _____        __  __          
/  __ \      / _|/ _|         
| /  \/ ___ | |_| |_ ___  ___ 
| |    / _ \|  _|  _/ _ \/ _ \/
| \__/\ (_) | | | ||  __/  __/
 \____/\___/|_| |_| \___|\___|
                                                          
""")


def menu():
    welcome_logo()
    print("1. Check the Inventory")
    print("2. Take an order")
    print("3. Check, the total collection")
    print("4. is it sufficient")
    print("5. Exit.We are closing.")


while True:
    menu()
    option = int(input("Choose, your option Mate!."))
    if option == 1:
        os.system("cls")
        welcome_logo()
        report_resources()
        time.sleep(10)
    elif option == 2:

        welcome_logo()
        coffee = input("Which coffee, would you like to order ?")
        if check_if_sufficient(coffee):
            make_coffee()
        else:
            print(f"Sorry Mate! We can not make {coffee}")
    elif option == 3:
        print(f'The total collection is {resources["money"]}')
    elif option == 4:
        coffee = input("Which coffee, would you like to order ?")
        if check_if_sufficient(coffee):
            print()
        else:
            print(f"Sorry Mate! We can not make {coffee}")
    elif option == 5:
        break
