# Exercise 1 : Cars
# Instructions
# Copy the following string into your code: "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet".

cars = 'Volkswagen, Toyota, Ford Motor, Honda, Chevrolet'

# Convert it into a list using Python (don’t do it by hand!).

cars_list = cars.split(", ")
print(cars_list)

# Print out a message saying how many manufacturers/companies are in the list.

print(f"There are {len(cars_list)} manufacturers in the list.")

# Print the list of manufacturers in reverse/descending order (Z-A).

print(f"There are {cars_list[::-1]} manufacturers in the list.")

# Using loops or list comprehension:
# Find out how many manufacturers’ names have the letter ‘o’ in them.

man_o = len([man for man in cars_list if 'o' in man])
print(man_o)

# Find out how many manufacturers’ names do not have the letter ‘i’ in them.

man_no_i = len([man for man in cars_list if 'i' not in man])
print(man_no_i)

# Bonus: There are a few duplicates in this list:["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]

dup_list = ["Honda", "Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]

# Remove these programmatically. (Hint: you can use set to help you).

new_set = {item for item in dup_list}
print(new_set)

# Print out the companies without duplicates, in a comma-separated string with no line-breaks (eg. “Acura, Alfa Romeo, Aston Martin, …”) 
# also print out a message saying how many companies are now in the list.

man_string = ", ".join(new_set)
print(man_string)
print(f"there are {len(new_set)} companies in the list.")

# Bonus: Print out the list of manufacturers in ascending order (A-Z), but reverse the letters of each manufacturer’s name.

man_list = [item for item in new_set]
man_list.sort()
reverse_word_list = [item[::-1] for item in man_list]
print(reverse_word_list)
