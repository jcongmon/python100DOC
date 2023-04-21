print("Welcome to the secret auction program.")
auction = {}

def check_winner(auction):
    max_val = 0
    winner = ""
    for key in auction:
        if auction[key] > max_val:
            max_val = auction[key]
            winner = key
    print(f"The winner is {winner} with a bid of ${max_val}!")


def cls():
    print("\n" * 50)


while True:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: $"))
    auction[name] = bid
    sentinel = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if sentinel == 'no':
        break
    cls()

check_winner(auction)