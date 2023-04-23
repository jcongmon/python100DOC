def print_report(db):
    print(f"Water: {db['water']} mL\nMilk: {db['milk']} mL\nCoffee: {db['coffee']} g\nMoney: ${db['money']}")


def check_resources(water, milk, coffee):
    sentinel = True
    if water < 0:
        print("Add more water.")
        sentinel = False
    if milk < 0:
        print("Add more milk.")
        sentinel = False
    if coffee < 0:
        print("Add more coffee.")
        sentinel = False
    return sentinel


def is_enough_change(cost):
    print(f"The price is {cost}. Please insert coins.")
    coins = [0.25, 0.1, 0.05, 0.01]
    input_coins = [int(input("How many quarters?: ")), int(input("How many dimes?: ")), int(input("How many nickles?: ")), int(input("How many pennies?: "))]
    sum = 0
    for i in range(0, len(coins)):
        sum += coins[i]*input_coins[i]
    return cost - sum


def print_give_drink(item, change):
    print(f"Here is your ${change} in change.")
    print(f"Here is your {item}. Enjoy!")


reserve = {"water": 300, "milk": 200, "coffee": 100, "money": 0.0}
menu = {"espresso": [50, 10, 0, 1.25], "latte": [200, 24, 150, 2.50], "cappucino": [250, 24, 200, 2.0]}

while True:
    inpt = input("What would you like? (espresso/latte/cappucino): ").lower()
    if inpt == 'off':
        break
    elif inpt == 'report':
        print_report(reserve)
        continue
    elif inpt != "espresso" and inpt != "latte" and inpt != "cappucino":
        print("Enter a valid option.")
        continue

    new_water = reserve["water"] - menu[inpt][0]
    new_coffee = reserve["coffee"] - menu[inpt][1]
    new_milk = reserve["milk"] - menu[inpt][2]
    price = menu[inpt][3]

    check = check_resources(new_water, new_milk, new_coffee)
    if not check:
        continue

    change = is_enough_change(price)
    if change > 0:
        print("Insufficient coins entered. Refunding change now.")
        continue

    reserve["water"] = new_water
    reserve["milk"] = new_milk
    reserve["coffee"] = new_coffee
    reserve["money"] += price
    change = abs(change)

    print_give_drink(inpt, change)

print("Coffee machine powering down.")