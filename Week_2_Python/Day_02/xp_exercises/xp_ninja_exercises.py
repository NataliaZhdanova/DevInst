# Exercise 1: Formula
# Instructions
# Write a program that calculates and prints a value according to this given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50.
# H is 30.
# Ask the user for a comma-separated string of numbers, use each number from the user as D in the formula and return all the results
# For example, if the user inputs: 100,150,180
# The output should be:
# 18,22,24

import math
c = 50
h = 30
result = str()
result_list = []
user_nums = input("Enter a comma-separated string of numbers: ")
num_list = user_nums.split(",")
for item in num_list :
    d = int(item)
    q = round(math.sqrt((2 * c * d) / h))
    result_list.append(str(q))
result = (", ").join(result_list)
print(result)

# Exercise 2 : List Of Integers
# Instructions
# Given a list of 10 integers to analyze. For example:

#     [3, 47, 99, -80, 22, 97, 54, -23, 5, 7] 
#     [44, 91, 8, 24, -6, 0, 56, 8, 100, 2] 
#     [3, 21, 76, 53, 9, -82, -3, 49, 1, 76] 
#     [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]
# Store the list of numbers in a variable.

int_list = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7, 99, 0, 47] 
single_line = ', '.join(str(element) for element in int_list)
sorted_list_desc = sorted(int_list, reverse = True)
sum_num = sum(int_list)
fl_list = [int_list[0], int_list[-1]]
greater_50 = []
for item in int_list :
    if item > 50 :
        greater_50.append(item)
smaller_10 = []
for item in int_list :
    if item < 10 :
        smaller_10.append(item)
squared_list = []
for item in int_list :
    squared_list.append(item ** 2)
no_duplicates = set()
for item in int_list :
    no_duplicates.add(item)
largest_num = max(int_list)
smallest_num = min(int_list)
average_num = sum(int_list) // len(int_list)

print(f'''
- The list of numbers in a single line: {single_line}
- The list of numbers sorted in descending order: {sorted_list_desc}
- The sum of all the numbers: {sum_num}
- A list containing the first and the last numbers: {fl_list}
- A list of all the numbers greater than 50: {greater_50}
- A list of all the numbers smaller than 10: {smaller_10}
- A list of all the numbers squared: {squared_list}
- The numbers without any duplicates: {no_duplicates}. There are {len(no_duplicates)} numbers in this list.
- The average of all the numbers: {average_num}
- The largest number: {largest_num}
- The smallest number: {smallest_num}     
      ''')

# Bonus: Find the sum, average, largest and smallest number without using built in functions.

int_list = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7, 99, 0, 47] 
sorted_list_desc = sorted(int_list, reverse = True)

sum_raw = 0
for item in int_list :
    sum_raw += item
avg_raw = sum_raw // len(int_list)
largest_raw = sorted_list_desc[0]
smallest_raw = sorted_list_desc[-1]

print(f'''
      - sum = {sum_raw}
      - average = {avg_raw}  
      - largest = {largest_raw}
      - smallest = {smallest_raw}
      
      ''')


# Bonus: Instead of using pre-defined lists of numbers, ask the user for 10 numbers between -100 and 100. 
# Ask the user for an integer between -100 and 100 – repeat this question 10 times. 
# Each number should be added into a variable that you created earlier.

trying = 1
int_list = list()
while trying <=10 :
    int_input = int(input("Enter an integer between -100 and 100: "))
    int_list.append(int_input)
    trying += 1

print(int_list)


# Bonus: Instead of asking the user for 10 integers, generate 10 random integers yourself. 
# Make sure that these random integers are between -100 and 100.

import random
trying = 1
int_list = list()
while trying <=10 :
    int_rand = random.randint(-100, 100)
    int_list.append(int_rand)
    trying += 1

print(int_list)

# Bonus: Instead of always generating 10 integers, let the amount of integers also be random! 
# Generate a random positive integer no smaller than 50.

import random
trying = 1
int_list = list()
attempts = random.randint(50, 100)
while trying <= attempts :
    int_rand = random.randint(-100, 100)
    int_list.append(int_rand)
    trying += 1

print(int_list)

# Exercise 3: Working On A Paragraph
# Find an interesting paragraph of text online. (Please keep it appropriate to the social context of our class.)
# Paste it to your code, and store it in a variable.
# Let’s analyze the paragraph. Print out a nicely formatted message saying:
# How many characters it contains (this one is easy…).
# How many sentences it contains.
# How many words it contains.
# How many unique words it contains.
# Bonus: How many non-whitespace characters it contains.
# Bonus: The average amount of words per sentence in the paragraph.
# Bonus: the amount of non-unique words in the paragraph.

text = input("Paste here a paragraph of text: \n")
chars = len(text)
sentences = text.count('.')
word_list = text.split(' ')
words = len(word_list)
word_set = set(word_list)
unique = len(word_set)
no_whitespaces = ('').join(word_list)
non_white_char = len(no_whitespaces)
average_words = words // sentences
non_unique_set = set()
for word in word_list :
    quantity = word_list.count(word)
    if quantity > 1 :
        non_unique_set.add(word)

print(f'''
      This paragraph contains:
      - {chars} characters
      - {sentences} sentences
      - {words} words
      - {unique} unique words: {word_set}
      - {non_white_char} non-whitespace characters
      - {average_words} words per sentence on average
      - {len(non_unique_set)} non-unique words: {non_unique_set}  
      
      ''')


# Exercise 4
# Instructions
# Write a program that prints the frequency of the words from the input.

# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.

# Then, the output should be:

#     2:2
#     3.:1
#     3?:1
#     New:1
#     Python:5
#     Read:1
#     and:1
#     between:1
#     choosing:1
#     or:2
#     to:1

phrase = input("Enter a long phrase: ")
new_dict = { }
word_list = phrase.split(" ")
for word in word_list :
    frequency = word_list.count(word)
    new_dict[word] = frequency
list_dict = sorted(new_dict.items())
for index in range(len(list_dict)) :
    print(f"{list_dict[index][0]} : {list_dict[index][-1]}")