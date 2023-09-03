# Instructions
# Using the input function, ask the user for a string. The string must be 10 characters long.
# If it’s less than 10 characters, print a message which states “string not long enough”.
# If it’s more than 10 characters, print a message which states “string too long”.
# If it’s 10 characters, print a message which states “perfect string” and continue the exercise.

# Then, print the first and last characters of the given text.

# Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example:
# The user enters "HelloWorld"
# Then, you have to construct the string character by character
# H
# He
# Hel
# ... etc
# HelloWorld


# 4. Bonus: Swap some characters around then print the newly jumbled string (hint: look into the shuffle method). For example:

# Hlrolelwod

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