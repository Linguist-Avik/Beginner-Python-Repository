print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')
print('\n WELCOME TO AUCTION PROGRAM')

from replit import clear
#HINT: You can call clear() to clear the output in the console.

def highest_bid(bidding_record):
  highest_number = 0
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount >= highest_number:
      highest_number = bid_amount
  print(f'The winner is {bidder} with the ${highest_number}')

bid_dictionary = {}      
counter = True
while counter:
  name = input("\nEnter Name: ")
  bid = int(input("Enter Bid: $"))
  bid_dictionary[name] = bid
  want_cont = input('\nAnyone else wants to bid? Yes/No: ').lower()
  if want_cont == 'yes':
    clear()
  elif want_cont == 'no':
    counter = False
    highest_bid(bid_dictionary)



