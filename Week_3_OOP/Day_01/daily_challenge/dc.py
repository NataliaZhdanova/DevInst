# Instructions : Old MacDonald’s Farm
# Take a look at the following code and output:
# File: market.py

# macdonald = Farm("McDonald")
# macdonald.add_animal('cow',5)
# macdonald.add_animal('sheep')
# macdonald.add_animal('sheep')
# macdonald.add_animal('goat', 12)
# print(macdonald.get_info())
# Output

# McDonald's farm

# cow : 5
# sheep : 2
# goat : 12

#     E-I-E-I-0!


# Create the code that is needed to receive the result provided above. Below are a few questions to assist you with your code:

# Create a class called Farm. How should it be implemented?
# Does the Farm class need an __init__ method? If so, what parameters should it take?
# How many methods does the Farm class need?
# Do you notice anything interesting about the way we are calling the add_animal method? What parameters should this function have? How many…?
# Test your code and make sure you get the same results as the example above.
# Bonus: nicely line the text in columns as seen in the example above. Use string formatting.

class Farm :
    def __init__(self, farm_name):
        self.name = farm_name
        self.animal = [ ]

    def add_animal(self) :
        new_animal = str()
        while new_animal != "quit" :
            new_animal = input(("Which animal should we add to the farm and in what quantity (use comma as a delimiter)? (Type 'quit' to exit) "))
            self.animal.append(new_animal)
        else :
            self.animal.remove("quit")
    
    def update_quantity(self) :
        list_of_lists = list()
        for index in range(0, len(self.animal)) :
            if "," in self.animal[index]:
                list_of_lists.append(self.animal[index].split(","))
            elif ", " in self.animal[index]:
                list_of_lists.append(self.animal[index].split(", "))
            elif " " in self.animal[index]:
                list_of_lists.append(self.animal[index].split(" "))
            else :
                list_of_lists.append([self.animal[index],1])

        global quantity_dict
        quantity_dict = { }
        for index in range(0, len(list_of_lists)) :
            item_list = list_of_lists[index]
            if item_list[0] not in quantity_dict.keys() :
                quantity_dict[item_list[0]] = int(item_list[-1])
            else :
                quantity_dict[item_list[0]] = quantity_dict[item_list[0]] + int(item_list[-1])

    
    def get_animal_types(self) :
        self.sorted_list = sorted(quantity_dict.keys())
        print(self.sorted_list)


    def get_short_info(self) :
        print(f"McDonald's farm has {self.sorted_list[0]}, {self.sorted_list[1]} and {self.sorted_list[2]} \n")
    
    def get_info(self) :
        print ("\n" + self.name + "\n")
        for key, value in quantity_dict.items():
            print(f"{key} : {value} \n")
        print ("\n E-I-E-I-O \n")


mcdonald = Farm("Old McDonald's Farm")
mcdonald.add_animal()
mcdonald.update_quantity()
mcdonald.get_info()
mcdonald.get_animal_types()
mcdonald.get_short_info()


# Expand The Farm
# Add a method called get_animal_types to the Farm class. This method should return a sorted list of all the animal types (names) in the farm. With the example above, the list should be: ['cow', 'goat', 'sheep'].

# Add another method to the Farm class called get_short_info. This method should return the following string: “McDonald’s farm has cows, goats and sheep.”. The method should call the get_animal_types function to get a list of the animals.