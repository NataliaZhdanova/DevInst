# Count Occurence
# Write a program which takes a string and a character as an input, and finds out the number of occurrences the character has in the string.

# String: Programming is cool!
# Character: o
# 3


# String: This is a great example
# Character: y
# 0

def char_in_string(char, string) :
    number = string.count(char)
    print(number)

string = input("Provide a string: ")
char = input("Enter a character to count in this string: ")
char_in_string(string, char)