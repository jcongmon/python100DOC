
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
first = input("You are at a cross road. Where do you want to go? Left or right?")
if first.lower() == "right":
    print("Game over. You died to a giant.")
else:
    second = input("You are at a lake. Do you swim or wait?")
    if second.lower() == "swim":
        print("Game over. You died to the Loch Ness Monster.")
    else:
        third = input("You come to three doors, a red, yellow, and blue door. Which do you go through?")
        if third.lower() == "yellow":
            print("You win! You found the treasure!")
        else:
            print("Game over. You died to a fire.")
