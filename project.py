# This program is a game of BlackJack where the player is able to versus the computer

# Class to represent a deck of cards, including methods to shuffle the deck and deal a card to a player.

# Create a class to represent a player, including methods to receive a card and calculate the value of their hand.

# Write a main game loop that allows the player to play multiple rounds of Blackjack.

# Implement the rules of the game, including when the dealer must hit or stand and when the player wins, loses, or pushes (ties with the dealer).

# Add additional features as desired, such as the ability to bet and keep track of the player's bankroll, or the option to play against multiple computer-controlled dealers.

"""
# RULES:
if hand > 21 = bust

dealer deals one card face up to each person, and one card faced down

if A+10 = x1.5 amount

if accept more card from dealer say hit

if reject more cards say stay

if <16 need take more cards
"""

import random

# Class to represent a single playing card
class Card:
    """
    This class represent a single playing card.

    Attributes:
        value (str): The value of a card.
        suit (str): The symbol of a card.
    """
    def __init__(self, value, suit):
        """
        The constructor for Card class.

        Parameters:
            value (str): The value of a card.
            suit (str): The symbol of a card.
        """
        self.value = value
        self.suit = suit

    def __str__(self):
        """
        This method prints the value and suit of the card.

        Returns:
            self.suit: suit of the card.
            self.value: Value of the card.
        """
        return "{} {}".format(self.suit, self.value)


# Class to represent a full deck of cards
class Deck:
    """
    This class represent a deck of card.
    """
    def __init__(self):
        """
        The constructor for Deck class.

        Parameters:
            cards_in_deck (list): A list of total cards in the deck.
            populate() (method): Call method to populate the deck.
            shuffle_deck() (method): Call method to randomly shuffle the deck.
        """
        self.cards_in_deck = []
        self.populate()
        self.shuffle_deck()
    
    def populate(self):
        """
        This method populate the empty deck of cards.
        """
        suits = {
            "spade": "♠️",
            "heart": "♥️",
            "diamond": "♦️",
            "club": "♣️"
        }

        cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

        for count, suit in enumerate(suits):
            for card in cards:
                self.cards_in_deck.append(Card(suits[suit], card))

    def return_cards(self):
        """
        This method prints the list of cards in the deck.

        returns:
            cards: A list of cards in the deck
        """
        cards = []
        for card in self.cards_in_deck:
            cards.append(card)

        return cards

    def shuffle_deck(self):
        """
        This method shuffles the deck randomly.
        """
        random.shuffle(self.cards_in_deck)

    def deal_card(self):
        """
        This method deals a card to the player and remove it from the overall list.

        returns:
            card: A card from the top of the deck
        """
        card = self.cards_in_deck.pop(0)

        return card
        
    def count_cards(self):
        """
        This method prints the number of cards in the deck.

        Returns:
            len(self.cards_in_deck)
        """
        return "{}".format(len(self.cards_in_deck))


def main():
    # Initialise the deck
    deck = Deck()
    print(deck.deal_card())
    # Return the list of cards by calling the deck.return_cards() method
    card_deck = deck.return_cards()

    print(deck.count_cards())
    # # Iter over the list and print out the cards, as just printing the whole list will return the object memory location as python calls "__repr__" method instead of "__str__"
    # for card in card_deck:
    #     print(card)
 

if __name__ == "__main__":
    main()