############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

import random
import art
from copy import copy
from replit import clear

# for key in art.ASCII:
#   print(art.ASCII[key])
  
# deck = {
#   "a": 1,
#   "b": 2,
#   "c": 3,
# }

# keys = []

# for key in deck:
#   keys.append(key)

# print(keys)
# print(random.choice(keys))

print(art.logo)
deck = {
  "A": {
    "value": [1,11],
    "ASCII": art.ASCII["A"],
    "on_deck": 32,
  },
  "C2": {
    "value": 2,
    "ASCII": art.ASCII["C2"],
    "on_deck": 32,
  },
  "C3": {
    "value": 3,
    "ASCII": art.ASCII["C3"],
    "on_deck": 32,
  },
  "C4": {
    "value": 4,
    "ASCII": art.ASCII["C4"],
    "on_deck": 32,
  },
  "C5": {
    "value": 5,
    "ASCII": art.ASCII["C5"],
    "on_deck": 32,
  },
  "C6": {
    "value": 6,
    "ASCII": art.ASCII["C6"],
    "on_deck": 32,
  },
  "C7": {
    "value": 7,
    "ASCII": art.ASCII["C7"],
    "on_deck": 32,
  },
  "C8": {
    "value": 8,
    "ASCII": art.ASCII["C8"],
    "on_deck": 32,
  },
  "C9": {
    "value": 9,
    "ASCII": art.ASCII["C9"],
    "on_deck": 32,
  },
  "C10": {
    "value": 10,
    "ASCII": art.ASCII["C10"],
    "on_deck": 32,
  },
  "J": {
    "value": 10,
    "ASCII": art.ASCII["J"],
    "on_deck": 32,
  },
  "Q": {
    "value": 10,
    "ASCII": art.ASCII["Q"],
    "on_deck": 32,
  },
  "K": {
    "value": 10,
    "ASCII": art.ASCII["K"],
    "on_deck": 32,
  },
  
}

keys = ["A", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "J", "Q", "K"]
player = {}
player_sum = 0
CPU = {}
CPU_sum = 0
CPU_keys = []
drawing_cards = True
lost_game = False
game_on = True
waiting_for_valid_input = True
user_input = ""
aces_on_deck_to_change = 0

def give_card(receiver):

  global player_sum
  global CPU_sum
  global aces_on_deck_to_change
  
  key = random.choice(keys)
  
  while deck[key]["on_deck"] == 0:
    key = random.choice(keys)
  
  if receiver == "p":
    if key in player:
      player[key]["on_deck"] += 1
      deck[key]["on_deck"] -= 1
    else:
      player[key] = copy(deck[key])
      deck[key]["on_deck"] -= 1
      player[key]["on_deck"] = 1
      
    if key == "A":
      player_sum += 11
      aces_on_deck_to_change += 1
    else:
      player_sum += deck[key]["value"]
      
  elif receiver == "c":
    if key in CPU:
      CPU[key]["on_deck"] += 1
      deck[key]["on_deck"] -= 1
    else:
      CPU[key] = copy(deck[key])
      deck[key]["on_deck"] -= 1
      CPU[key]["on_deck"] = 1
      CPU_keys.append(key)

    if key == "A":
      CPU_sum += 11
    else:
      CPU_sum += deck[key]["value"]

def number_of_cards(player_or_cpu):
  number = 0
  for key in player_or_cpu:
    number += player_or_cpu[key]["on_deck"]
  return number

def print_hand():
  print("Ihre Karten sind: ")
  for key in player:
    for number in range (player[key]["on_deck"]):
       print(player[key]["ASCII"])
  print(f"Ihre Summe ist {player_sum}.\n")
  print("Die Karten des Computers sind: ")
  if drawing_cards:
    print(CPU[CPU_keys[0]]["ASCII"])
    cards = number_of_cards(CPU)
    for number in range(cards-1):
      print(art.turned_card)
  else:
    for key in CPU:
      for number in range (CPU[key]["on_deck"]):
        print(CPU[key]["ASCII"])
# Testing code

# print(deck["A"])
# print(deck["A"]["value"])
# print(deck["A"]["ASCII"])
# print(deck["A"]["on_deck"])

# for key in deck:
#   print(deck[key]["value"])
#   print(deck[key]["ASCII"])
#   print(deck[key]["value"])

# for key in keys:
#   print(key)

# End of testing code
  
print("Willkommen!")
while waiting_for_valid_input:
  user_input = input("Möchten Sie spielen? Schreiben Sie 'J' (Ja) oder 'N' (Nein).\n")
  if user_input == 'J':
    game_on = True
    waiting_for_valid_input = False
  elif user_input == 'N':
    game_on = False
    waiting_for_valid_input = False
  else:
    waiting_for_valid_input = True
    print("Bitte schreiben Sie eine richtige Option.\n")

while game_on:
  print("Sie bekommen einige Karte...")
  give_card("p")
  give_card("p")
  print("Und jetzt bekommt der Computer einige Karte...")
  give_card("c")
  give_card("c")
  print_hand()
  while drawing_cards:
    if player_sum > 21:
      if "A" in player:
        if aces_on_deck_to_change > 0:
          waiting_for_valid_input = True
          while waiting_for_valid_input:
            user_input = input("Möchten Sie den Wert einer von Ihren A-Karten auf 1 verändern? Schreiben Sie 'J' (Ja) oder 'N' (Nein).\n")
            if user_input == 'J':
              player_sum -= 10
              aces_on_deck_to_change -= 1
              waiting_for_valid_input = False
            elif user_input == 'N':
              print("Sie haben das Spiel verloren. Ihre Summe ist grosser als 21.")
              waiting_for_valid_input = False
              drawing_cards = False
              lost_game = True
            else:
              waiting_for_valid_input = True
              print("Bitte schreiben Sie eine richtige Option.\n")
        else:
          print("Sie haben das Spiel verloren. Ihre Summe ist grosser als 21.")
          waiting_for_valid_input = False
          drawing_cards = False
          lost_game = True
      else:
        print("Sie haben das Spiel verloren. Ihre Summe ist grosser als 21.")
        waiting_for_valid_input = False
        drawing_cards = False
        lost_game = True
    else:
      waiting_for_valid_input = True
      while waiting_for_valid_input:
        user_input = input("Möchten Sie noch eine Karte? Schreiben Sie 'J' (Ja) oder 'N' (Nein).\n")
        if user_input == "J":
          give_card("p")
          waiting_for_valid_input = False
        elif user_input == "N":
          drawing_cards = False
          waiting_for_valid_input = False
        else:
          waiting_for_valid_input = True
          print("Bitte schreiben Sie eine richtige Option.\n")
         
    print_hand()
    
  while CPU_sum < 17:
    print(f"Die Summe des Computers ist {CPU_sum}, und das ist kleiner als 17. Der Computer bekommt eine neue Karte.")
    give_card("c")
    print_hand()

  print(f"Ihre Summe ist {player_sum} und die Summe des Computers ist {CPU_sum}.")

  if player_sum > 21:
    print("Sie haben verloren. Ihre Summe ist grosser als 21.")
  elif player_sum > CPU_sum :
    print("Sie haben gewonnen!")
  elif player_sum == CPU_sum:
    print("Gleichstand!")
  else:
    print("Sie haben verloren weil der Computer gewonnen hat. Schade.")

  waiting_for_valid_input = True
  while waiting_for_valid_input:
    user_input = input("Möchten Sie noch einmal spielen? Schreiben Sie 'J' (Ja) oder 'N' (Nein).\n")
    if user_input == "J":
      waiting_for_valid_input = False
      player = {}
      player_sum = 0
      CPU = {}
      CPU_sum = 0
      CPU_keys = []
      drawing_cards = True
      lost_game = False
      game_on = True
      user_input = ""
      aces_on_deck_to_change = 0
    elif user_input == "N":
      game_on = False
      waiting_for_valid_input = False
    else:
      waiting_for_valid_input = True
      print("Bitte schreiben Sie eine richtige Option.\n")

print("Bitte beehren Sie uns bald mit Ihrem Besuch. Auf Wiedersehen.")