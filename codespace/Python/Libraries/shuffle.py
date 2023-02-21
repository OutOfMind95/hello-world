import random

def main():
    cards = ["jack", "queen", "king", "ace"]
    random.shuffle(cards)
    for card in cards:
        print(card)

main()