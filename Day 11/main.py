import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card(cards):
    rand_idx = random.randint(0, len(cards) - 1)
    return cards[rand_idx]


def deal_cards(cards):
    hand = [deal_card(cards), deal_card(cards)]
    return hand


def check_for_11(hand):
    for i in range(0, len(hand)):
        if hand[i] == 11:
            hand[i] = 1
    return hand


def check_for_22(hand):
    if hand[0] == 11 and hand[1] == 11:
        hand[1] = 1
    return hand

def print_user_score(user_cards, user_score):
    print(f"Your cards: {user_cards}, current score: {user_score}.")


def print_dealer_score(dealer_cards, dealer_score):
    print(f"Dealer cards: {dealer_cards}, dealer score: {dealer_score}.")


def print_score(user_cards, user_score, dealer_cards, dealer_score):
    print_user_score(user_cards, user_score)
    print_dealer_score(dealer_cards, dealer_score)


print("Welcome to PyBlackJack!")


while input("Do you want to play a game? y/n\n").lower() == "y":
    user_cards = check_for_22(deal_cards(cards))
    dealer_cards = check_for_22(deal_cards(cards))
    user_score = sum(user_cards)
    dealer_score = sum(dealer_cards)
    sentinel = True

    print_user_score(user_cards, user_score)
    print(f"Dealer's first card: {dealer_cards[0]}\n")

    while input("Enter 'y' to get another card or 'n' to pass.\n") == 'y':
        user_cards.append(deal_card(cards))
        user_score = sum(user_cards)
        if user_score > 21 and 11 in user_cards:
            check_for_11(user_cards)
        elif user_score > 21:
            print_score(user_cards, user_score, dealer_cards, dealer_score)
            print("You lose!\n")
            sentinel = False
            break
        user_score = sum(user_cards)
        print_user_score(user_cards, user_score)

    if sentinel is False:
        continue

    if user_score < dealer_score:
        print_score(user_cards, user_score, dealer_cards, dealer_score)
        print("You lose!\n")
        continue

    while dealer_score < 17:
        dealer_cards.append(deal_card(cards))
        dealer_score = sum(dealer_cards)
        if dealer_score > 21 and 11 in dealer_cards:
            check_for_11(dealer_cards)
        elif dealer_score > 21:
            print_score(user_cards, user_score, dealer_cards, dealer_score)
            print("The dealer busted. You win!\n")
            sentinel = False
            break
        dealer_score = sum(dealer_cards)

    if sentinel is False:
        continue

    if user_score > dealer_score:
        print_score(user_cards, user_score, dealer_cards, dealer_score)
        print("You win!\n")
    elif dealer_score > user_score:
        print_score(user_cards, user_score, dealer_cards, dealer_score)
        print("You lose!\n")
    else:
        print_score(user_cards, user_score, dealer_cards, dealer_score)
        print("It's a tie!\n")

print("Thanks for playing!")
