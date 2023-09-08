# Challenge 1: 
# Ask a user for a word
# Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.

# Make sure the letters are the keys.
# Make sure the letters are strings.
# Make sure the indexes are stored in a list and those lists are values.

# Examples:

# "dodo" ➞ { "d": [0, 2], "o": [1, 3] }

# "froggy" ➞ { "f":  [0], "r": [1], "o": [2], "g": [3, 4], "y": [5] }

# "grapes" ➞ { "g": [0], "r": [1], "a": [2], "p": [3]}

word = input("Enter a word: \n")
list_char = list(enumerate(word))
word_dict = dict()

for value, key in list_char:
    if key not in word_dict :
        word_dict[key] = value
    else :
        word_dict[key] = [word_dict[key], value]


print(word_dict)

# Challenge 2: 
# Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.
# Sort the list in alphabetical order.
# Return “Nothing” if you can’t afford anything from the store.

store_inventory = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20",
  "Apple": "$4",
  "Honey": "$3",
  "Fan": "$14",
  "Bananas": "$4",
  "Pan": "$100",
  "Spoon": "$2",
  "Phone": "$999",
  "Speakers": "$300",
  "Laptop": "$5,000",
  "PC": "$1200"
}

allow_list = []

wallet_sum = input("How much money you have in your wallet? \n")

for key, value in store_inventory.items() :
    str_num = value[1:]
    int_num = int(str_num.replace(",", ""))
    
    if wallet_sum >= int_num :
        allow_list.append(key)

allow_list.sort()
if len(allow_list) > 0 :
    print(f"You can afford the following items: {allow_list}!")
else :
    print(f"You can afford nothing in the shop!")



