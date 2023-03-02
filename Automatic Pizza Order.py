# Automatic pizza order program
#Small Pizza: $15; Medium Pizza: $20; Large Pizza: $25; Pepperoni for Small Pizza: +$2; Pepperoni for Medium or Large Pizza: +$3; Extra cheese for any size pizza: + $1

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

#Category Small
if size == "s" or size == "S":
    if add_pepperoni == "Y" or add_pepperoni == "y":
        if extra_cheese == "Y" or extra_cheese == "y":
            print('$', 15 + 2 + 1)
        else:
            print('$', 15 + 2)
    else:
        print('$', 15)
#Category Medium
elif size == "M" or size == "m":
    if add_pepperoni == "Y" or add_pepperoni == "y":
        if extra_cheese == "Y" or extra_cheese == "y":
            print('$', 20 + 3 + 1)
        else:
            print('$', 20 + 3)
    else:
        print('$', 20)
#Category Large
elif size == "L" or size == "l":
    if add_pepperoni == "Y" or add_pepperoni == "y":
        if extra_cheese == "Y" or extra_cheese == "y":
            print('$', 25 + 3 + 1)
        else:
            print('$', 25 + 3)
    else:
        print('$', 25)
else:
    print('product unavailable')
