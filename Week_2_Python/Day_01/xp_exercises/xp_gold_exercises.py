# Exercise 1 : Hello World-I Love Python
# Instructions
# Print the following output in one line of code:
# Hello world
# Hello world
# Hello world
# Hello world
# I love python
# I love python
# I love python
# I love python

print("Hello world \n" * 4 + "I love python \n" * 4)

# Exercise 2 : What Is The Season ?
# Instructions
# Ask the user to input a month (1 to 12).
# Display the season of the month received :
# Spring runs from March (3) to May (5)
# Summer runs from June (6) to August (8)
# Autumn runs from September (9) to November (11)
# Winter runs from December (12) to February (2)

month = input("Please enter the number of the month (from 1 to 12): \n")
month_num = int(month)
if month_num in range (3, 6) :
     print("It's spring outside!")
elif month_num in range (6, 9) :
     print("It's summer outside!")
elif month_num in range (9, 12) :
     print("It's autumn outside!")
elif month_num in range (1, 3) :
     print("It's winter outside!")
elif month_num == 12 :
     print("It's winter outside!")

    
