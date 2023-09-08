# Exercise 1 : Convert Lists Into Dictionaries
# Instructions
# Convert the two following lists, into dictionaries.
# Hint: Use the zip method
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

#Solution EX 1:

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

#merges two lists in one list
key_value = zip(keys,values)

#converts a mew merged list into a dictionary
new_dic = dict(key_value)

print(new_dic)

# Exercise 2 : Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# Given the following object:

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


# How much does each family member have to pay ?

# Print out the family’s total cost for the movies.
# Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).

#Solution EX 2:

payment = 0
total_cost = 0
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
new_family = {}
for name, age in family.items() :
    if age < 3 :
        payment = 0
        total_cost += 0
        print(f"{name} has to pay nothing!")
    elif 3 <= age < 12 :
        payment = 10
        total_cost = total_cost + 10
        print(f"{name} has to pay $10!")
    elif age >= 12 :
        payment = 15
        total_cost = total_cost + 15
        print(f"{name} has to pay $15!")

print("The total cost of tickets is: $", total_cost)

#Bonus
payment = 0
total_cost = 0
new_family = {}
member = str()
member = input("Enter names and ages of your family members separated by whitespace. To finish, type 'quit'. \n")
while member != "quit" :
    member_details = member.split(" ")
    new_family.update([member_details])
    member = input("Enter names and ages of your family members separated by whitespace. . To finish, type 'quit'. \n")
else :
    for name, age in new_family.items() :
        if int(age) < 3 :
            payment = 0
            total_cost += 0
            print(f"{name} has to pay nothing!")
        elif 3 <= int(age) < 12 :
            payment = 10
            total_cost = total_cost + 10
            print(f"{name} has to pay $10!")
        elif int(age) >= 12 :
            payment = 15
            total_cost = total_cost + 15
            print(f"{name} has to pay $15!")

print("The total cost of tickets is: $", total_cost)

# Exercise 3: Zara
# Instructions
# Here is some information about a brand.
# name: Zara 
# creation_date: 1975 
# creator_name: Amancio Ortega Gaona 
# type_of_clothes: men, women, children, home 
# international_competitors: Gap, H&M, Benetton 
# number_stores: 7000 
# major_color: 
#     France: blue, 
#     Spain: red, 
#     US: pink, green

#Solution EX 3:

# Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
# The values type_of_clothes and international_competitors should be a list. The value of major_color should be a dictionary.

brand = {
    "name" : "Zara", 
    "creation_date" : 1975, 
    "creator_name" : "Amancio Ortega Gaona", 
    "type_of_clothes" : ["men", "women", "children", "home"],
    "international_competitors" : ["Gap", "H&M", "Benetton"],
    "number_stores" : 7000,
    "major_color" : {"France" : "blue", "Spain" : "red", "US" : ["pink", "green"]}
    }

# Change the number of stores to 2.

brand["number_stores"] = 2

# Print a sentence that explains who Zaras clients are.

clients = brand["type_of_clothes"]
print("Zara's clients are:", (", ").join(clients))

# Add a key called country_creation with a value of Spain.

brand["country_creation"] = "Spain"

# Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.

if "international_competitors" in brand:  
    print("Yes, 'international_competitors' is one of the keys in the brand dictionary.")
    brand["international_competitors"].append("Desigual")

print(brand["international_competitors"])


# Delete the information about the date of creation.

brand.pop("creation_date")  

# Print the last international competitor.

competitors = brand["international_competitors"]
print("Zara's last international competitor is", competitors[-1])

# Print the major clothes colors in the US.

major_colors = brand["major_color"]["US"]
print("Major colors in the US are:", (", ").join(major_colors))

# Print the amount of key value pairs (ie. length of the dictionary).

print(len(brand))

# Print the keys of the dictionary.

print(brand.keys())

# Create another dictionary called more_on_zara with the following details:

more_on_zara = {
    "creation_date" : 1975, 
    "number_stores" : 10000 
}


# Use a method to add the information from the dictionary more_on_zara to the dictionary brand.

brand.update(more_on_zara)
print(brand)

# Print the value of the key number_stores. What just happened ?
# The old value was overwritten

print(brand["number_stores"])


# Exercise 4 : Disney Characters
# Instructions
# Use this list :
# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# Analyse these results :
# #1/
# >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
# #2/
# >>> print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
# #3/ 
# >>> print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}

#Solution EX 4:

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

# Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.

disney_users_A = dict()
for element in users :
    disney_users_A[element] = users.index(element)

print(disney_users_A)


# Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.

disney_users_B = dict()
for element in users :
    disney_users_B[users.index(element)] = element

print(disney_users_B)

# Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.

disney_users_C = dict()
users.sort()
for element in users :
    disney_users_C[element] = users.index(element)

print(disney_users_C)

# Only recreate the 1st result for:
# The characters, which names contain the letter “i”.

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

users[:] = [x for x in users if "i" in x]
disney_users_A = dict()
for element in users :
    disney_users_A[element] = users.index(element)

print(disney_users_A)

# or
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
disney_users_A = dict()
for element in users :
    disney_users_A[element] = users.index(element)

disney_users = disney_users_A.copy()

for element in disney_users :
    if "i" not in element :
     disney_users_A.pop(element)  

print(disney_users_A)

# The characters, which names start with the letter “m” or “p”.

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

users[:] = [x for x in users if x.startswith('M') or x.startswith('P')]
disney_users_A = dict()
for element in users :
    disney_users_A[element] = users.index(element)

print(disney_users_A)




