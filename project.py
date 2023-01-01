# This program is a game of BlackJack where the player is able to versus the computer

# Add additional features as desired, such as the ability to bet and keep track of the player's bankroll, or the option to play against multiple computer-controlled dealers.

import random, sys

# Main function
def main():
    # Get users choice
    menu_selection()


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

        returns:
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

        suits = ["♠️", "♥️", "♦️", "♣️"]
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

        for suit in suits:
            for card in values:
                self.cards_in_deck.append(Card(suit, card))

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

        return "{}".format(card)
        
    def count_cards(self):
        """
        This method prints the number of cards in the deck.

        returns:
            len(self.cards_in_deck)
        """
        return "{}".format(len(self.cards_in_deck))


# Class to represent a player
class Player:
    """
    This class represent a player

    Attributes:
            card_in_hand (list): A list of total cards on hand.    
    """
    def __init__(self):
        """
        The constructor for Player class.

        Parameters:
            card_in_hand (list): A list of total cards on hand.
        """
        self.card_in_hand = []

    def receive_card(self, card):
        """
        This method receive a card given by deal_card in Deck class.
        """
        self.card_in_hand.append(card)

    def calculate_hand(self):
        """
        This method calculates the total value in the player's hand.
        """
        face_value_list = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]
        picture_list = ["J", "Q", "K"]
        total_value = 0
        ace_count = 0        

        # Check if ACE is in the hand
        for card in self.card_in_hand:
            # Remove all symbol of J, Q, K, A, and space
            card = card.rstrip("♠️♥️♦️♣️ ")
            
            if card == "A":
                ace_count += 1

        # Loop through the whole hand and check if card is any value other than ACE
        for card in self.card_in_hand:
            # Remove all symbol of J, Q, K, A, and space
            card = card.rstrip("♠️♥️♦️♣️ ")

            # Check if card is in face value list
            if card in face_value_list:
                total_value += int(card)

            # Check if card is in picture value list
            elif card in picture_list:
                total_value += 10

            # Check if card is ACE
            else:
                if total_value > 21 and ace_count > 1:
                    total_value += 1
                    ace_count -= 1
                else:
                    total_value += 11

        return total_value

    def auto_win(self):
        """
        This method checks for auto win criteria - E.g. AA, Ak, AQ, AJ, A10
        """
        value_list = ["10", "J", "Q", "K"]
        auto_win = False
        ace_count = 0
        total_value = 0

        # Check if ACE is in the hand
        for card in self.card_in_hand:
            # Remove all symbol of J, Q, K, A, and space
            card = card.rstrip("♠️♥️♦️♣️ ")
            
            if card == "A":
                ace_count += 1

        # Return auto_win and ace_count if player get AA
        if ace_count == 2:
            auto_win = True
            return auto_win, ace_count

        # Loop through the whole hand and check if card is any value other than ACE
        for card in self.card_in_hand:
            # Remove all symbol of J, Q, K, A, and space
            card = card.rstrip("♠️♥️♦️♣️ ")

            if ace_count == 1 and card in value_list:
                auto_win = True
                return auto_win, ace_count
        
        return auto_win, ace_count

    def show__hand(self):
        """
        This method shows all the card in the player's hand.

        returns:
            self.card_in_hand = A list of cards that is given to the player.
        """
        return self.card_in_hand


# Function to check if user input is value
def menu_selection():
    """
    Takes in the user input and check if value is in int

    returns:
        choice (int): The string value given by the user, converted to int
    """
    while True:
        try:
            # Show menu options
            print("Choose 1 to start the BlackJack game")
            print("Choose 2 to show the rules of BlackJack")
            print("Choose 3 to exit")
            choice = input("Enter the choice in integer: ")
            choice = int(choice)

            # Data validation
            if choice == 1:
                start_game()
            elif choice == 2:
                show_rules()
            else:
                sys.exit("You have exited the program!")

        except ValueError:
            print("Choice must be an integer and between value of 1-3!")
            pass

# Function to run the main game loop
def start_game():
    """
    Function to start game loop
    """
    # Set the classes as global variable 
    global deck, player, dealer

    # Initialise the deck object
    deck = Deck()

    # Initialise the player an dealer object
    player = Player()
    dealer = Player()

    # First the dealer deals two card to each other
    deal_starting_cards()

    # Check for auto win criteria - E.g. AA, AJ, AQ, AK, A10
    check_auto_win_criteria()

    # Start the actual game if there are no auto win criteria
    game_loop()


def deal_starting_cards():
    """
    This method deals the starting card to the player and dealer
    """
    card = deck.deal_card()
    player.receive_card(card)

    card = deck.deal_card()
    dealer.receive_card(card)

    card = deck.deal_card()
    player.receive_card(card)

    card = deck.deal_card()
    dealer.receive_card(card)

    player_hand = player.show__hand()
    dealer_hand = dealer.show__hand()

    # Print new line
    print("\n")

    # Show player's hand to the player
    print("Your cards are {}, {}".format(player_hand[0], player_hand[1]))

    # Show dealer's first card to the player
    print("Dealer's cards are {}, XX".format(dealer_hand[0]))
    
    # Print new line
    print("\n")


def check_auto_win_criteria():
    """
    Function to check if player or dealer auto win.
    """
    player_auto_win_criteria, player_ace_count = False, 0
    dealer_auto_win_criteria, dealer_ace_count = False, 0

    player_auto_win_criteria, player_ace_count = player.auto_win()
    dealer_auto_win_criteria, dealer_ace_count = dealer.auto_win()

    player_hand = player.show__hand()
    dealer_hand = dealer.show__hand()

    # Check if game is a draw
    if player_auto_win_criteria == True and dealer_auto_win_criteria == True:

        if player_ace_count == 1 and dealer_auto_win_criteria == 1:
            print("Your cards are {}, {}".format(player_hand[0], player_hand[1]))
            print("Dealer's cards are {}, {}".format(dealer_hand[0], dealer_hand[1]))
            sys.exit("Game is a draw!")

        elif player_ace_count == 1 and dealer_ace_count == 0:
            print("Your cards are {}, {}".format(player_hand[0], player_hand[1]))
            print("Dealer's cards are {}, {}".format(dealer_hand[0], dealer_hand[1]))
            sys.exit("Player wins!")

        else:
            print("Your cards are {}, {}".format(player_hand[0], player_hand[1]))
            print("Dealer's cards are {}, {}".format(dealer_hand[0], dealer_hand[1]))
            sys.exit("Dealer wins!")

    # Check if player wins
    if player_auto_win_criteria == True and dealer_auto_win_criteria == False:
            print("Your cards are {}, {}".format(player_hand[0], player_hand[1]))
            print("Dealer's cards are {}, {}".format(dealer_hand[0], dealer_hand[1]))
            sys.exit("Player wins!")

    # Check if dealer wins
    if player_auto_win_criteria == False and dealer_auto_win_criteria == True:
        print("Your cards are {}, {}".format(player_hand[0], player_hand[1]))
        print("Dealer's cards are {}, {}".format(dealer_hand[0], dealer_hand[1]))
        sys.exit("Dealer wins!")


def game_loop():
    """
    This function creates a while loop until the both player and dealer ends their turn.
    """
    player_stand, dealer_stand = False, False
    player_bust, dealer_bust = False, False

    while player_stand == False and dealer_stand == False:
        # Player starts turn
        while player_stand == False and player_bust == False:
            try:
                choice = int(input("Enter 1 for Hit and 2 for Stand: \n"))

                # If user hit draw a card till satisfied
                if choice == 1:
                    card = deck.deal_card()
                    player.receive_card(card)

                    # Show player's hand to player
                    print("Your cards are: ")

                    # Print the whole deck
                    print("{}".format(', '.join(player.show__hand())))
                    
                    player_hand_value = player.calculate_hand()

                    # Set player_stand and player_bust variable to True if player hand is above 21 to prevent player from drawing the whole deck
                    if player_hand_value > 21:
                        player_stand = True
                        player_bust = True

                # If user stands
                else:
                    player_stand = True

            except ValueError:
                print("Please only enter 1 or 2!")                

        # Dealers turn
        while dealer_stand == False and dealer_bust == False:
            dealer_hand_value = dealer.calculate_hand()

            # Dealer will hit if hand value < 16
            if dealer_hand_value <= 16:
                card = deck.deal_card()
                dealer.receive_card(card)

                dealer_hand_value = dealer.calculate_hand()
                if dealer_hand_value > 21:
                    dealer_bust = True

            # Dealer will stand if hand value > 17
            else:
                dealer_stand = True

    # If both stop calculate who won and show cards
    player_hand_value = player.calculate_hand()
    dealer_hand_value = dealer.calculate_hand()

    # If player or dealer bust
    if player_bust == True and dealer_bust == True:
        print("Game is a draw! Both player and dealer bust!")
        print("Your cards are {}".format(', '.join(player.show__hand())))
        print("Dealer's cards are {}".format(', '.join(dealer.show__hand())))

    elif player_bust == False and dealer_bust == True:
        print("Player won! Dealer bust!")
        print("Your cards are {}".format(', '.join(player.show__hand())))
        print("Dealer's cards are {}".format(', '.join(dealer.show__hand())))

    elif player_bust == True and dealer_bust == False:
        print("Dealer won! Player bust!")
        print("Your cards are {}".format(', '.join(player.show__hand())))
        print("Dealer's cards are {}".format(', '.join(dealer.show__hand())))

    # If nobody bust
    else:
        if player_hand_value > dealer_hand_value:
            print("Player won! Value of player's hand is higher than dealer!")
            print("Your cards are {}".format(', '.join(player.show__hand())))
            print("Dealer's cards are {}".format(', '.join(dealer.show__hand())))

        elif player_hand_value < dealer_hand_value:
            print("Dealer won! Value of dealer's hand is higher than player!")
            print("Your cards are {}".format(', '.join(player.show__hand())))
            print("Dealer's cards are {}".format(', '.join(dealer.show__hand())))
        
        else:
            print("Game is a draw! Value of player and dealer is equal!")
            print("Your cards are {}".format(', '.join(player.show__hand())))
            print("Dealer's cards are {}".format(', '.join(dealer.show__hand())))

    # Print a new line
    print("\n")

# Function to show the rules of BlackJack
def show_rules():
    """
    Function to print out the rules of BlackJack.
    """
    print("\n")
    print("Blackjack is a popular card game played with a deck of 52 cards. The goal of the game is to beat the dealer by having a hand value that is closer to 21 than the dealer's hand, without going over 21.")
    print("\n")
    print("Here are the basic rules of blackjack:")
    print("1. The game is played with one deck of 52 cards.")
    print("2. The value of each card is as follows:")
    print("    - 2 through 10 are worth their face value.")
    print("    - Jack, Queen, and King are worth 10 points.")
    print("    - Ace is worth 1 or 11 points, depending on which value would be more beneficial for the hand.")
    print("3. The dealer deals two cards to each player and two cards to themselves, with one of the dealer's cards being face up and the other face down (the 'hole' card).")
    print("4. Each player's turn begins with the player to the left of the dealer. During their turn, the player has the following options:")
    print("    - Hit: Take another card from the deck.")
    print("    - Stand: Keep their current hand and end their turn.")
    print("5. If a player's hand value goes over 21, they lose the game (this is called a 'bust').")
    print("6. Once all players have completed their turns, the dealer reveals their hole card and hits or stands based on the following rules:")
    print("    - If the dealer has a hand value of 17 or higher, they must stand.")
    print("    - If the dealer has a hand value of 16 or lower, they must hit.")
    print("7. If the dealer busts, all remaining players win the game. If the dealer does not bust, the player's hands are compared to the dealer's hand and the player with the hand closest to 21 without going over wins the game.")
    print("8. If a player and the dealer have the same hand value, the game is a tie (this is called a 'push').")
    print("\n")


if __name__ == "__main__":
    main()
