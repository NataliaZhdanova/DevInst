# Challenge 1
# Ask the user for a number and a length.
# Create a program that prints a list of multiples of the number until the list length reaches length.
# Examples

# number: 7 - length 5 ➞ [7, 14, 21, 28, 35]

# number: 12 - length 10 ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

# number: 17 - length 6 ➞ [17, 34, 51, 68, 85, 102]

number = int(input("Provide a number: \n"))
length = int(input("Provide length: \n"))

number_list = [int(number * x) for x in range (1,length+1)]
print(number_list)


# Challenge 2
# Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
# Examples

# user's word : "ppoeemm" ➞ "poem"

# user's word : "wiiiinnnnd" ➞ "wind"

# user's word : "ttiiitllleeee" ➞ "title"

# user's word : "cccccaaarrrbbonnnnn" ➞ "carbon"

word = set(input("Provide a string of characters: \n"))
no_dup = list()
word_list = list()
new_word = str()
word = input("Provide a string of characters: \n")

for x in word :
    word_list.append(x)

no_dup = list(dict.fromkeys(word_list))

new_word = ("").join(no_dup)
print(new_word)


