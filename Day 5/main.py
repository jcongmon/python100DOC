import random

print("Welcome to the PyPassword Generator!")
chars = int(input("How many characters would you like in your password?\n"))
symbols = int(input("How many symbols would you like?\n"))
nums = int(input("How many numbers would you like?\n"))

char_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbol_list = "!@#$%^&*()-_=+"
num_list = "1234567890"

result = ""

for n in range(0, chars):
    idx = random.randint(0, len(char_list) - 1)
    result += char_list[idx]

for n in range(0, symbols):
    idx = random.randint(0, len(symbol_list) - 1)
    result += symbol_list[idx]

for n in range(0, nums):
    idx = random.randint(0, len(num_list) - 1)
    result += num_list[idx]

used_idx = []
password = ""

for n in range(0, len(result)):
    while True:
        idx = random.randint(0, len(result) - 1)
        if idx not in used_idx:
            password += result[idx]
            used_idx.append(idx)
            break

print(f"Here is your password: {password}")