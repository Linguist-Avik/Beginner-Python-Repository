#rock paper scissors game
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
  print(rock)
elif select == 2:
  print(paper)
elif select == 3:
  print(scissors)
else:
  print("Enter numbers 1, 2 or 3")

#logic for computer input
random_selection = random.randint(1,3)
print(f'Computer selects {random_selection}')
if random_selection == 1:
  print(rock)
elif random_selection == 2:
  print(paper)
else:
  print(scissors)
  
#logic for winner selection
if select == random_selection:
  print("It is a tie")
elif select == 1 and random_selection == 2:
  print("Computer wins")
elif select == 1 and random_selection == 3:
  print("You win")
elif select == 2 and random_selection == 1:
  print("You win")
elif select == 2 and random_selection == 3:
  print("Computer wins")
elif select == 3 and random_selection == 1:
  print("Computer wins")
elif select == 3 and random_selection == 2:
  print("You win")
else:
  print('wrong input')
