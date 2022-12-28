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

class Card:
    """
    This class have two methods used to populate a deck of 52 cards without "Joker".

    Attributes:
        suits (str): The symbol of a card.
        cards (str): The value of a card.
    """

    def __init__(self, suits, cards):
        """
        The constructor for Card class.

        Parameters:
            suits (str): The symbol of a card.
            cards (str): The value of a card.
        """

        self.suits = suits
        self.cards = cards

    def suits(self):
        """
        This method returns a dictionary of suits.

        Returns:
            suits: A dictionary of suits.
        """

        suits = {
            "spade": "♠️",
            "heart": "♥️",
            "diamond": "♦️",
            "club": "♣️"
        }

        return suits

    def cards(self):
        """
        This method returns a list of values for cards.

        Return:
            cards: A list of values for cards.
        """

        cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

        return cards


class Deck:
    """
    This class have methods to generate a deck, shuffle the deck, and dispense cards.

    Attributes:
        deck (str): A list of cards
    """

    def __init__(self, deck):
        """
        The constructor for Deck class.

        Parameters:
            deck (str): A list of cards
        """

        self.deck = deck

    def generate_deck(self):
        """
        This method generates a deck in a list using suits and cards methods from the Card class.
        """
        ...


def main():
    # Initialise the deck



if __name__ == "__main__":
    main()