#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

logo = """
 _____                     _               _____                      
|  __ \                   (_)             |  __ \                     
| |  \/_   _  ___  ___ ___ _ _ __   __ _  | |  \/ __ _ _ __ ___   ___ 
| | __| | | |/ _ \/ __/ __| | '_ \ / _` | | | __ / _` | '_ ` _ \ / _ \
| |_\ \ |_| |  __/\__ \__ \ | | | | (_| | | |_\ \ (_| | | | | | |  __/
 \____/\__,_|\___||___/___/_|_| |_|\__, |  \____/\__,_|_| |_| |_|\___|
                                    __/ |                             
                                   |___/                              
"""

import random
from replit import clear

def guess_game():
  print(logo)
  print("I am thinking of a number between 1 to 100")
  computer_guess = random.choice(range(101))
  
  ask_level = input("Choose mode - 'Easy' or 'Hard': ").lower()
  if ask_level == "easy":
    turns = 10
    print(f"You have {turns} turns left to guess the number")
  else:
    turns = 5
    print(f"You have {turns} turns left to guess the number")
    
  while turns != 0:
    user_guess = int(input("Make a guess: "))
    if user_guess == computer_guess:
      print(f"\nComputer's guess is {computer_guess}\nYou have correctly guessed {user_guess}\nCongratulations! You won!!\n")
      break
    elif user_guess > computer_guess:
      print("Too High")
      turns -= 1
      print(f"You have {turns} turns left")
    elif user_guess < computer_guess:
      print("Too Low")
      turns -= 1
      print(f"You have {turns} turns left")
    if turns == 0:
      print("\nYou've run out of guesses, you lose.")

def final_game():
  guess_game()
  counter = True
  while counter:
    another_game = input("Do you want to play again? 'Y' or 'N'? ").lower()
    if another_game =='y':
      clear()
      guess_game()
    else:
      counter = False
      print("\nThank You for playing the guessing game! Bye-Bye.")

final_game()
  
  

