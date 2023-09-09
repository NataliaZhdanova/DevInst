# Challenge 1 : Sorting
# Instructions
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Use List Comprehension
# Example:
# Suppose the following input is supplied to the program: without,hello,bag,world
# Then, the output should be: bag,hello,without,world

def sorting() :
    sequence = input("Provide a comma-separated sequence of words: \n")
    sorting_list = sequence.split(",")
    sorting_list = [str(element).replace(' ','') for element in sorting_list]
    sorting_list.sort()
    sorted_sequence = (',').join(sorting_list)
    print(f"the sorted sequense is: {sorted_sequence}")

sorting()

# Challenge 2 : Longest Word
# Instructions
# Write a function that finds the longest word in a sentence. If two or more words are found, return the first longest word.
# Characters such as apostrophe, comma, period count as part of the word (e.g. O’Connor is 8 characters long).
# Examples

# longest_word("Margaret's toy is a pretty doll.") ➞ "Margaret's"

# longest_word("A thing of beauty is a joy forever.") ➞ "forever."

# longest_word("Forgetfulness is by all means powerless!") ➞ "Forgetfulness"


def longest_word() :
    sentence = input("Provide a sentence to find the longest word in it: \n")
    sentence_to_list = sentence.split(" ")
    longest_word = max(sentence_to_list, key = len)
    print(f"The longest word is: '{longest_word}'")

longest_word()

