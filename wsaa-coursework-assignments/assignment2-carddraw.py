# This is an API that simulates dealing a deck of cards
# URL: https://deckofcardsapi.com/
# Author: Andre Machado

import requests
import json

shuffle_url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(shuffle_url)

deck_data = response.json()
# Extract the deck_id from the response
deck_id = deck_data['deck_id']
print(f"Shuffled sucessfully! Deck id: {deck_id}")

# Draw two cards (count=2)
draw_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=2"
response = requests.get(draw_url)

cards_data = response.json()
# Extract the list of cards from the response
cards = cards_data['cards']
print(f"Draw 2 cards! Cards: {cards}")

# Print the value and suit of each card
print("Drawn 2 Cards: ")
for card in cards:
    print(f"{card['value']} of {card['suit']}")

print("---------------")
# Draw 5 cards (count=5)
draw5_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
response = requests.get(draw5_url)

cards5_data = response.json()
# Extract the list of cards from the response
cards5 = cards5_data['cards']
print(f"Draw 5 cards! Cards: {cards5}")

# Print the value and suit of each card
print("\nDrawn 5 Cards: ")
for cards in cards5:
    print(f"{cards['value']} of {cards['suit']}")