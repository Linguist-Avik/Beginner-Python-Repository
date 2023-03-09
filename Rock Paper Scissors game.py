import random
select = int(input('Enter numbers 1 for rock or 2 for paper or 3 for scissors: '))
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#logic for user input
if select == 1:
  print(f'\nYou have selected Rock {rock}')
elif select == 2:
  print(f'\nYou have selected Paper {paper}')
elif select == 3:
  print(f'\nYou have selected Scissors {scissors}')
else:
  print("Enter numbers 1, 2 or 3")
  
#logic for computer input
random_selection = random.randint(1,3)
if random_selection == 1:
  print(f'Computer selects Rock {rock}')
elif random_selection == 2:
  print(f'Computer selects Paper {paper}')
else:
  print(f'Computer selects Scissors {scissors}')
  
#check the logic
if select == random_selection:
  print("\n~ It is a tie ~")
elif select == 1 and random_selection == 2:
  print("\n~ Computer wins ~")
elif select == 1 and random_selection == 3:
  print("\n~ You win ~")
elif select == 2 and random_selection == 1:
  print("\n~You win~")
elif select == 2 and random_selection == 3:
  print("\n~ Computer wins ~")
elif select == 3 and random_selection == 1:
  print("\n~ Computer wins ~")
elif select == 3 and random_selection == 2:
  print("\n~ You win ~")
