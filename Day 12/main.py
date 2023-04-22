import random


def welcome():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    return input("Choose a difficulty. Type 'easy' or 'hard': ").lower()


def print_attempts(lives):
    print(f"You have {lives} attempts to guess the number.")


def query_guess(num, k):
    if num < k:
        print("Too low.")
        return False
    elif num > k:
        print("Too high.")
        return False
    return True


difficulty = welcome()
lives = 10 if difficulty == "easy" else 5
rand_num = random.randint(0, 100)

while lives > 0:
    print_attempts(lives)
    guess = int(input("Make a guess: "))
    found_num = query_guess(guess, rand_num)
    if found_num:
        break
    else:
        lives -= 1

print(f"You got it! The answer was {rand_num}.") if found_num else print("You've run out of guesses. You lose.")

