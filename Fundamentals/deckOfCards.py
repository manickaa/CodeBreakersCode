import random

SUITS = ["DIAMONDS", "SPADES", "HEARTS", "CLUBS"]
VALUES = ["ACE", "TWO" , "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN", "JACK", "QUEEN", "KING"]

class Card:

    # Card constructor
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    # Returns the suit of the card.
    def suit(self):
        return self.suit
    
    # Returns the value of the card.
    def value(self):
        return self.value

class Deck(Card):
    
    # Creates a sorted deck of playing cards. 13 values, 4 suits.
    def __init__(self):
        deck = []
        for suit in SUITS:
            for value in VALUES:
                card = Card(suit, value)
                deck.append(card)
        self.deck = deck
    
    # Returns the number of Cards in the Deck
    def num_cards(self):
        return len(self.deck)
    
    # Shuffles the deck of cards.
    def shuffle(self):
        random.shuffle(self.deck)
    
    # Returns the top Card in the deck, then puts it back.
    def peek(self):
        return (self.deck[-1].value, self.deck[-1].suit)
    
    # Draws and returns the top card in the deck. The card should no longer be in the Deck.
    def draw(self):
        drawn_card = self.deck.pop()
        return drawn_card
    
    # Adds the input card to the deck. If the deck has more than 52 cards, do not add the card and raise an exception.
    def add_card(self, card):
        if(len(self.deck) < 52):
            self.deck.append(card)
        else:
            print("Cannot Add card. Deck Full")

    # Calling this function should print all the cards in the deck in their current order.
    def print_deck(self):
        for card in self.deck:
            print("Value: " + card.value + " SUIT: " + card.suit)

deck = Deck()
deck.print_deck()
print(deck.num_cards())
print(deck.peek())
print(deck.num_cards())
print(deck.draw())
print(deck.num_cards())
card = Card("CLUBS", "KING")
print(deck.add_card(card))
print(deck.num_cards())
deck.print_deck()
deck.shuffle()
deck.print_deck()