# Create A Deck Of Cards Class.
# The Deck of cards class should NOT inherit from a Card class.

# The requirements are as follows:

# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# The Deck class :
# should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.


import random

class Card :
    def __init__(self, suit, value) :
        self.suit = suit
        self.value = value

    def __str__(self) :
        return f"{self.value} of {self.suit}"


class Deck :
    def __init__(self) :
        self.cards = []
        self.generate_deck()
        self.shuffle()

    def generate_deck(self) :
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def shuffle(self) :
        random.shuffle(self.cards)

    def deal(self) :
        if not self.is_empty() :
            return self.cards.pop()
        else:
            return None

    def is_empty(self) :
        return len(self.cards) == 0


deck = Deck()

for number in range(0, 5):
    card = deck.deal()
    if card:
        print(card)
    else:
        print("The deck is empty.")


deck.shuffle()

for number in range(0, 5):
    card = deck.deal()
    if card:
        print(card)
    else:
        print("The deck is empty.")
