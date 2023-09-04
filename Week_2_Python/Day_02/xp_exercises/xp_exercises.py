# Exercise 1 : Set
# Instructions
# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

#Solution EX 1:

#Create a set of my favorite numbers
my_fav_numbers = set()
print("Provide your ten favorite numbers.\n")
while len(my_fav_numbers) < 10 :
    my_fav_numbers.add(input("The number is: \n"))
else :
    print("My ten favorite numbers:", my_fav_numbers)

#Add two new numbers to this set
print("Add two more numbers to this set.")

while len(my_fav_numbers) < 12 :
    my_fav_numbers.add(input("The number is: \n"))
else :
    print("My twelve favorite numbers:", my_fav_numbers)

#Remove the last number

my_fav_numbers.discard(list(my_fav_numbers)[-1])
print("My eleven favorite numbers:", my_fav_numbers)

#Create a set called friend_fav_numbers with your friend’s favorites numbers

friend_fav_numbers = set()
print("Provide your friend's five favorite numbers.\n")
while len(friend_fav_numbers) < 5 :
    friend_fav_numbers.add(input("The number is: \n"))
else :
    print("My friend's five favorite numbers:", friend_fav_numbers)


#Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

our_fav_numbers = set()

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print("Our favorite numbers are:", our_fav_numbers)


# Exercise 2: Tuple
# Instructions
# Given a tuple which value is integers, is it possible to add more integers to the tuple?

#Solution EX 2:
#No, it is not possible because tauples are immutable.

# Exercise 3: List
# Instructions
# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];
# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)

#Solution EX 3:

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
print("A basket without a banana:", basket)

basket.remove("Blueberries")
print("A basket without a banana and blueberries:", basket)

basket.append("Kiwi")
print("A basket with a kiwi:", basket)

basket.insert(0, "Apples")
print("A basket with double apples:", basket)

count = basket.count("Apples")
print("There are", count, "apples in the basket.")

basket.clear()
print("The empty basket:", basket)

# Exercise 4: Floats
# Instructions
# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).

#Solution EX 4:

floats = [float(i) / 2 for i in range (3,11)]
print(floats)

# Exercise 5: For Loop
# Instructions
# Use a for loop to print all numbers from 1 to 20, inclusive.
# Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.

#Solution EX 5:

for x in range(1, 21) :
    print(x)

list_of_values = list()
even_values = list()
for x in range(1, 21) :
    list_of_values.append(x)
    if (list_of_values.index(x) % 2) == 0 :
        print(x)


# Exercise 6 : While Loop
# Instructions
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.

#Solution EX 6:

name = "Natalia"
your_name = input("What is your name? \n")
while your_name != "Natalia" :
    your_name = input("What is your name? \n")
else :
    print("Hi, Natalia!")

# Exercise 7: Favorite Fruits
# Instructions
# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

#Solution EX 7:

fruits_input = input("Provide a list of three fruits separated by a single whitespace: \n")
fruits_list = list(fruits_input.split(" "))
print(fruits_list)

fav_fruit = input("Provide a name of any fruit: \n")
if fav_fruit in fruits_list :
    print("You chose one of your favorite fruits! Enjoy!")
else :
    print("You chose a new fruit. I hope you enjoy it!")

# Exercise 8: Who Ordered A Pizza ?
# Instructions
# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

#Solution EX 8:

toppings_list = list()
pizza_price = 10
topping = 0
while topping != "quit" :
    topping = input("Choose a topping... To stop choosing, type 'quit': \n")
    toppings_list.append(topping)
    print("I added this topping to your pizza!")
    pizza_price = pizza_price + 2.5
else :
    toppings_list.remove("quit")
    pizza_price = pizza_price - 2.5
    your_toppings = ','.join(toppings_list)
    print("Your selected toppings are:", your_toppings)
    print("The total price is:", pizza_price)


# Exercise 9: Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
# Ask a family the age of each person who wants a ticket.
# Store the total cost of all the family’s tickets and print it out.

# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.

#Solution EX 9:

total_cost = 0
members = int(input("How many family members want to buy a ticket? \n"))
for x in range(1, members + 1) :
    age = int(input("Please provide your age: \n"))
    if age < 3 :
        print("Your ticket is free")
    elif 3 <= age < 12 :
        print("Your ticket costs $10")
        total_cost = total_cost + 10
    elif age >= 12 :
        print("Your ticket costs $15")
        total_cost = total_cost + 15
print("The total cost of tickets is: $", total_cost)

tn_name = 0
tn_age = 0
init_tn_list = ['Masha', 'Sasha', 'John', 'Vlad']
final_list = list()
for x in init_tn_list :
    tn_name = input("What is your name? \n")
    if tn_name in init_tn_list :
        tn_age = int(input("How old are you? \n"))
        if tn_age < 16 :
            print("You are not permitted to watch the movie!\n")
        elif tn_age >=21 :
            print("You are not permitted to watch the movie!\n")
        else :
            print("You're allowed to watch the movie!\n")
            final_list.append(tn_name)
    else :
        print("You're not in the list!")
        break
print("The final list of teenagers:", final_list)



# Exercise 10 : Sandwich Orders
# Instructions
# Using the list below :

# sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

# The deli has run out of pastrami, use a while loop to remove all occurrences of “Pastrami sandwich” from sandwich_orders.
# We need to prepare the orders of the clients:
# Create an empty list called finished_sandwiches.
# One by one, remove each sandwich from the sandwich_orders while adding them to the finished_sandwiches list.
# After all the sandwiches have been made, print a message listing each sandwich that was made, such as:
# I made your tuna sandwich
# I made your avocado sandwich
# I made your egg sandwich
# I made your chicken sandwich

#Solution EX 10:
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]


while "Pastrami sandwich" in sandwich_orders :
    sandwich_orders.remove("Pastrami sandwich")
print(sandwich_orders)

sandwich_orders_1 = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
finished_sandwiches = list()
for x in range(1, len(sandwich_orders_1)+1) :
    finished_sandwiches.append(sandwich_orders[0])
    sandwich_orders.remove(sandwich_orders[0])
print(finished_sandwiches)
for x in range(1, len(finished_sandwiches)+1) :
    print("I made your", finished_sandwiches[x-1])
