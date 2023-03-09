#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
rock = '''  ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''  PAPER
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''  SCISSORS
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

select = int(input('Enter numbers 0 for rock or 1 for paper or 2 for scissors: '))
print('\nYou have selected:\n')
print(game_images[select])


random_selection = random.randint(0,2)
print("\nComputer selects: \n")
print(game_images[random_selection])


if select > 2 and select < 0:
  print("Enter valid input")
elif select == random_selection:
  print("\n~ It is a tie ~")
elif select == 0 and random_selection == 1:
  print("\n~ Computer wins ~")
elif select == 0 and random_selection == 2:
  print("\n~ You win ~")
elif select == 1 and random_selection == 1:
  print("\n~You win~")
elif select == 1 and random_selection == 2:
  print("\n~ Computer wins ~")
elif select == 2 and random_selection == 0:
  print("\n~ Computer wins ~")
elif select == 2 and random_selection == 1:
  print("\n~ You win ~")


# In[ ]:





# In[ ]:





# In[ ]:




