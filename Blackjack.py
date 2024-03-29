
############### Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

#######################################################
#Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt


import random
from replit import clear
print("WELCOME TO THE GAME OF BLACKJACK\n")
restart_counter = True
while restart_counter:
  #deal_card() function that uses the List below to *return* a random card. 11 is the Ace.
  def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
  
  #Create a function called calculate_score() that takes a List of cards as input 
  #and returns the score. 
  #Look up the sum() function to help you do this.
  def calculate_score(cards):
    """Take a list of cards and return a score calculated from the cards"""
  #Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if sum(cards) == 21 and len(cards) == 2:
      return 0
    #Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    if 11 in cards and sum(cards) > 21:
          cards.remove(11)
          cards.append(1)
    return sum(cards)
    
  #Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
  def compare(user_score, computer_score):
    if user_score == computer_score:
      return "It is a draw!"
    elif computer_score == 0:
      return "You lose, computer wins!"
    elif user_score == 0:
      return "Computer loses, you win!"
    elif user_score > 21:
      return "You lose, computer wins!"
    elif computer_score > 21:
      return "Computer loses, you win!"
    elif user_score > computer_score:
      return "You win, computer loses."
    else:
      return "Computer wins, you lose." 
  
  #Deal the user and computer 2 cards each using deal_card() and append().
  user_cards = []
  computer_cards = []
  is_game_over = False
  
  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  #The score will need to be rechecked with every new card drawn and needs to be repeated until the game ends.
  
  while not is_game_over:
    #Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    
    print(f"Your cards are {user_cards} and your score is {user_score}")
    print(f"\nComputer's first card is {computer_cards[0]}")
    
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      #If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
      user_should_deal = input("\nDo you want to draw another card? Type 'y' for yes or 'n' for no: ").lower()
    if user_should_deal == 'y':
      user_cards.append(deal_card())
    else:
      is_game_over = True
  
  #Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  print(f"\nYour final cards are {user_cards} and your final score is {user_score}")
  print(f"\nComputer's final cards are {computer_cards} and computer's final score is {computer_score}\n")
  print(compare(user_score, computer_score))
  
  #Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
  ask_restart = input("\nWould you like to restart the game? Type 'y' or 'n': ").lower()
  if ask_restart == 'y':
    clear()
  else:
    restart_counter = False
    clear()
    print("Thank you for playing! Bye-Bye.")

