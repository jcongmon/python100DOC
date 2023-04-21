import random

word_bank = ["aardvark", "baboon", "camel"]
rand_num = random.randint(0, len(word_bank) - 1)
word = word_bank[rand_num]

guessed_word = []
guessed_letters = []
for c in word:
    guessed_word.append("_")
lives = 6

print("Welcome to hangman.")


def check_bank(guessed_letters, guess):
    for n in guessed_letters:
        if n == guess:
            print(f"You guessed {guess} already.")
            return True


def check_guessed(word, guessed_word, guess, letters):
    for n in range(0, len(word)):
        if word[n] == guess:
            letters += 1
            guessed_word[n] = guess
    return letters


def check_done(word, guessed_word):
    for n in range(0, len(word)):
        if word[n] is not guessed_word[n]:
            return False
    return True


def print_lives(lives, word):
    print(f"Current lives: {lives}")
    if lives == 0:
        print(f"Sorry, you lose. The word was {word}.")


while lives > 0:
    guess = input("Guess a letter: ")
    if check_bank(guessed_letters, guess):
        continue
    guessed_letters.append(guess)

    letters = 0

    letters = check_guessed(word, guessed_word, guess, 0)
    for n in guessed_word:
        print(n + " ", end="")
    print()

    if letters > 0:
        print(f"You guessed {guess}, there are {letters} {guess}(s)")
    else:
        lives -= 1
        print(f"You guessed {guess}, which is not in the word. You lose a life.")

    if check_done(word, guessed_word):
        print(f"The word was {word}! Congratulations!")
        break
    print_lives(lives, word)