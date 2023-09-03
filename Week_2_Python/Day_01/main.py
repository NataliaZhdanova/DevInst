# Exercise 1

# ask a user for a number of miles, to convert kilometers and display it.

# Exercise 2
# Fill missing pieces (____) of the following code such that prints make sense.

# name = 'John Doe'
# if ____:
#     print(f"Name "{name}" is more than 20 chars long")
#     length_description = 'long'
# elif ____:
#      print(f"Name "{name}" is more than 15 chars long")
#     length_description = 'semi long'
# elif ____:
#      print(f"Name "{name}" is more than 10 chars long")
#     length_description = 'semi long'
# elif ____:
#      print(f"Name "{name}" is 8, 9 or 10 20 chars long")
#     length_description = 'semi short'
# else:
#      print(f"Name "{name}" is a short name")
#     length_description = 'short'

# Exercise 3
# Here is a table of prices for a wedding catering company:

# # of guests	price
# Up to 50 people	$4,000
# Up to 100 people	$10,000
# Up to 200 people	$15,000
# More than 200 people	$20,000

# Instructions:

# Please write an program that asks the user for the number of people attending their wedding and prints the corresponding price in the console.
# For example, if the user says that 20 people are attending to the wedding, it must cost $4,000 dollars.

a = str (input("Please provide a random string of characters...\n"))
b = len(a)
if b > 10 :
    print("The string is too long!")
elif b < 10 :
    print("The string is too short!")
else :
    print("That's a perfect string!")
    print("The first character is", a[0])
    print("The last character is", a[-1])

#printing from 1 sympol to 10 symbols

n = 1
for x in a :
    print(a[:n])
    n = n + 1
    if x == a[:9] :
        break

#Shuffling and printing shuffled

import random

z = list(a)
random.shuffle(z)

my_string = "".join(str(element) for element in z)
print(my_string)

