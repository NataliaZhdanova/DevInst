# Exercise 1: Birthday Look-Up
# Instructions
# Create a variable called birthdays. Its value should be a dictionary.
# Initialize this variable with birthdays of 5 people of your choice. 
# For each entry in the dictionary, the key should be the person’s name, and the value should be their birthday. Tip : Use the format “YYYY/MM/DD”.
# Print a welcome message for the user. Then tell them: “You can look up the birthdays of the people in the list!”“
# Ask the user to give you a person’s name and store the answer in a variable.
# Get the birthday of the name provided by the user.
# Print out the birthday with a nicely-formatted message.

birthdays = {"Nick":"1969/01/12", "Anna":"1972/11/17", "Max":"1950/06/23", "Mary":"1986/02/26", "Elisabeth":"2002/12/30"}
username = input("Hi, dear, what is your name? ")
print(f"Welcome, {username}! You can look up the birthdays of the people in the list!")
person = input("Give me a name of the person to get their birthday date: " )
print(f"The birthday date of {person} is {birthdays[person]}.")


# Exercise 2: Birthdays Advanced
# Instructions
# Before asking the user to input a person’s name print out all of the names in the dictionary.
# If the person that the user types is not found in the dictionary, print an error message (“Sorry, we don’t have the birthday information for <person’s name>”)

birthdays = {"Nick":"1969/01/12", "Anna":"1972/11/17", "Max":"1950/06/23", "Mary":"1986/02/26", "Elisabeth":"2002/12/30"}
username = input("Hi, dear, what is your name? ")
print(f"Welcome, {username}! You can look up the birthdays of the people in the list!")
print(f"Currently, the following people are in the list: {[item for item in birthdays.keys()]}")
person = input("Give me a name of the person to get their birthday date: " )
if person in birthdays.keys() :
    print(f"The birthday date of {person} is {birthdays[person]}.")
else :
    print(f"Sorry, we don't have the birthday information for {person}.")

# Exercise 3: Add Your Own Birthday
# Instructions
# Add this new code: before asking the user to input a person’s name to look up, ask the user to add a new birthday:
# Ask the user for a person’s name – store it in a variable.
# Ask the user for this person’s birthday (in the format “YYYY/MM/DD”) - store it in a variable.
# Now add this new data into your dictionary.
# Make sure that if the user types any name that exists in the dictionary – including the name that he entered himself – the corresponding birthday is found and displayed.

birthdays = {"Nick":"1969/01/12", "Anna":"1972/11/17", "Max":"1950/06/23", "Mary":"1986/02/26", "Elisabeth":"2002/12/30"}
username = input("Hi, dear, what is your name? ")
print(f"Welcome, {username}! You can look up the birthdays of the people in the list!")
print(f"Currently, the following people are in the list: {[item for item in birthdays.keys()]}")
new_user = input("Please add a name of another person to our list: ")
new_user_bd = input("Please add a birthday date of this person in the YYYY/MM/DD format: ")
birthdays[new_user] = new_user_bd
person = input("Now, give me a name of the person to get their birthday date: " )
if person in birthdays.keys() :
    print(f"The birthday date of {person} is {birthdays[person]}.")
else :
    print(f"Sorry, we don't have the birthday information for {person}.")


# Exercise 4: Fruit Shop
# Instructions
items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
# Using the dictionary above, each key-value pair represents an item and its price - print all the items and their prices in a sentence.

print(f'''In our shop, you can find the following goods:
      - {list(items.keys())[0]} - {items[list(items.keys())[0]]} dollars per kg
      - {list(items.keys())[1]} - {items[list(items.keys())[1]]} dollars per kg
      - {list(items.keys())[2]} - {items[list(items.keys())[2]]} dollars per kg
      - {list(items.keys())[3]} - {items[list(items.keys())[3]]} dollars per kg
            
      ''')

# Using the dictionary below, each value are dictionaries containing both the price and the amount of items in stock -
# write some code to calculate how much it would cost to buy everything in stock.
items = {
    "banana": {"price": 4 , "stock":10},
    "apple": {"price": 2, "stock":5},
    "orange": {"price": 1.5 , "stock":24},
    "pear": {"price": 3 , "stock":1}
}

stock_value = 0

for value in items.values() :
    stock_value += value["price"] * value["stock"]

print(f"It would cost {stock_value} dollars to buy everything in stock.")