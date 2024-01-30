import random

print("""
Welcome to a game of Higher or Lower!
Can you clear the deck?
Please note Ace is high!
Type in 'Cheat' to see the cards already cleared""")

def create_deck():
    #Creates and returns a deck of playing cards.
    suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def card_value(card):
    #Returns the numerical value of a card.
    rank = card[0]
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
    return values[rank]

def play_game():
    deck = create_deck()
    cheat_list = []
    current_card = deck.pop()
    print(f"The current card is: {current_card[0]} of {current_card[1]}")

    while deck:
        guess = input("Will the next card be high or low? (h/l): ").lower()

        if guess == 'cheat':
            print("\nCheat List:")
            for card in cheat_list:
                print(f"{card[0]} of {card[1]}")
            continue

        next_card = deck.pop()
        print(f"The next card is: {next_card[0]} of {next_card[1]}")

        if card_value(next_card) > card_value(current_card) and guess == 'h':
            print("Correct!")
        elif card_value(next_card) < card_value(current_card) and guess == 'l':
            print("Correct!")
        elif card_value(next_card) == card_value(current_card):
            print("Same value, please continue.")
        else:
            print("Incorrect guess. Game over.")
            print(f"You managed to guess {len(cheat_list)} cards correctly")
            break

        current_card = next_card
        cheat_list.append(next_card)

    else:
        print("Congratulations! You've guessed all the cards correctly.")

if __name__ == "__main__":
    play_game()
