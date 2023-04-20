import random

compScore = 0
userScore = 0
while True:
    choice = input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors, or q to quit.")
    if choice == 'q':
        break
    randNum = random.randint(0, 2)
    if choice == "0":
        print("You chose rock.")
        if randNum == 0:
            print("The computer chose rock.")
            print("It's a tie!")
        elif randNum == 1:
            print("The computer chose paper.")
            print("You lost!")
            compScore += 1
        else:
            print("The computer chose scissors.")
            print("You won!")
            userScore += 1
    if choice == "1":
        print("You chose paper.")
        if randNum == 0:
            print("The computer chose rock.")
            print("You won!")
            userScore += 1
        elif randNum == 1:
            print("The computer chose paper.")
            print("It's a tie!")
        else:
            print("The computer chose scissors.")
            print("You lost!")
            compScore += 1
    if choice == "2":
        print("You chose scissors.")
        if randNum == 0:
            print("The computer chose rock.")
            print("You lost!")
            compScore += 1
        elif randNum == 1:
            print("The computer chose paper.")
            print("You won!")
            userScore += 1
        else:
            print("The computer chose scissors.")
            print("It's a tie!")
    print(f"The current score is {userScore} (you) : {compScore} (computer).")