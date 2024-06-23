import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"




class Deck:
    def __init__(self):
        self.cards = [Card(suit, value) for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]
                      for value in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]]
        self.shuffle()

    def shuffle(self):
        if len(self.cards) != 52:
            self.cards = [Card(suit, value) for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]
                          for value in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]]
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop() if self.cards else None


# Example usage:
deck = Deck()
print(deck.cards)  # Print the shuffled deck

card = deck.deal()
print(card)  # Print the dealt card

print(len(deck.cards))  # Check the number of remaining cards in the deck
