import random

# Define the suits and cards per suit
suits = ['♠', '♥', '♦', '♣']
cards_per_suit = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

class CardGame:
    def __init__(self, name):
        self.name = name
        self.final_deck = []

    def create_deck(self):
        # Create the deck of cards
        deck = ''
        for i in range(len(cards_per_suit)):
            # Build cards for each suit
            for suit in suits:
                card = suit + cards_per_suit[i]
                deck += card
        # Convert the string deck to a list
        self.final_deck = list(deck)
        
        # Ask if a Joker should be included
        joker = int(input('Should this deck contain a joker? 1 - YES | 2 - NO\nAnswer: '))
        if joker == 1:
            self.final_deck.append('Joker')
            random.shuffle(self.final_deck)
            print('Added Joker')
        
        # Shuffle the deck and display the total number of cards
        random.shuffle(self.final_deck)
        print(f'Total cards in the deck: {len(self.final_deck)}')

    def display_card_types(self):
        # Display the types of cards in each suit
        for suit in suits:
            print(f'=== {suit} ===')
            for card in cards_per_suit:
                print(suit + card, end=', ')
            print()

    def receive_cards(self):
        # Receive a hand of 9 random cards from the deck
        my_cards = random.choices(self.final_deck, k=9)
        print('Your hand:', my_cards)

# Create a player and start the game
player_1 = CardGame('Cleyton')

# Display the types of cards in each suit
player_1.display_card_types()

# Create the deck of cards
player_1.create_deck()

# Receive a hand of cards
player_1.receive_cards()
