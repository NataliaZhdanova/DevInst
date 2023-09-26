# Exercise 1: Concatenate Lists
# Instructions
# Write code that concatenates two lists together without using the + sign.

list_01 = [ "Mary", "has", "a", "little", "lamb"]
list_02 = [1, 2, 3, 4, 5, 6]

list_01.extend(list_02)
print(list_01)

# Exercise 2: Range Of Numbers
# Instructions
# Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.

for number in range(1500, 2501) :
    multiple_5 = number % 35
    if multiple_5 == 0 :
        print(number)


# Exercise 3: Check The Index
# Instructions
# Using this variable

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user_name = input("What is your name? \n")
guessed = False
while guessed == False :
    if user_name in names :
        guessed = True
        name_index = names.index(user_name)
        print(f"the index of your name is: {name_index}")
    else :
        user_name = input("What is your name? \n")

# Ask a user for their name, if their name is in the names list print out the index of the first occurence of the name.
# Example: if input is 'Cortana' we should be printing the index 1


# Exercise 4: Greatest Number
# Instructions
# Ask the user for 3 numbers and print the greatest number.
#     Test Data
#     Input the 1st number: 25
#     Input the 2nd number: 78
#     Input the 3rd number: 87

#     The greatest number is: 87
comparison_list = []

for attempt in range(1, 4):
    number = input(f"Please provide {attempt} number: ")
    comparison_list.append(number)
print(f"The greatest number is: {max(comparison_list)}")



# Exercise 5: The Alphabet
# Instructions
# Create a string of all the letters in the alphabet
# Loop over each letter and print a message that contains the letter and whether its a vowel or a consonant.
letters = input("Enter all letters of the alphabet at once: ")
vowels = ["a", "e", "i", "o", "u"]
for char in letters :
    if char in vowels :
        print(f"{char} - is a vowel!")
    else :
        print(f"{char} - is a consonant!")


# Exercise 6: Words And Letters
# Instructions
# Ask a user for 7 words, store them in a list named words.
# Ask the user for a single character, store it in a variable called letter.
# Loop through the words list and print the index of the first appearence of the letter variable in each word of the list.
# If the letter doesn’t exist in one of the words, print a friendly message with the word and the letter.

words_list = []
for words in range(1, 8) :
    word = input(f"Tell me a word #{words}: ")
    words_list.append(word)
letter = input("Give me any character: ")
for word in words_list :
    if letter in word :
        print(f"The index of letter '{letter}' in the word '{word}' is '{word.index(letter)}'")
    else :
        print(f"there is no letter '{letter}' in the word '{word}'.")

# Exercise 7:
# Instructions
# Create a list of numbers from one to one million and then use min() and max() to make sure your list actually starts at one and ends at one million. Use the sum() function to see how quickly Python can add a million numbers.
my_list = list(range(1, 1000001))
print(min(my_list))
print(max(my_list))
print(sum(my_list))

# Exercise 8 : List And Tuple
# Instructions
# Write a program which accepts a sequence of comma-separated numbers. Generate a list and a tuple which contain every number.
# Suppose the following input is supplied to the program: 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

numbers = input("Provide several numbers separated by the comma: ")
new_list = numbers.split(', ')
new_tuple = tuple(new_list)
print(new_list)
print(new_tuple)


# Exercise 9 : Random Number
# Instructions
# Ask the user to input a number from 1 to 9 (including).
# Get a random number between 1 and 9. Hint: random module.
# If the user guesses the correct number print a message that says Winner.
# If the user guesses the wrong number print a message that says better luck next time.
# Bonus: use a loop that allows the user to keep guessing until they want to quit.
# Bonus 2: on exiting the loop tally up and display total games won and lost.

import random
won_games = 0
lost_games = 0
while True: 
    rand_num = random.randint(1,10)
    user_num = input("Enter a number from 1 to 9. Type 0 to exit: ")
    if user_num == '0' :
        print(f"You won {won_games} times and lost {lost_games} times!")
        print("Bye-bye!")
        break
    else :
        if int(user_num) == rand_num :
            won_games += 1
            print("Congrats, you won!")
        else :
            lost_games += 1
            print("Ooops, you lost! Good luck next time!")