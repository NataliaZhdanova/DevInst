# Exercise 1: Cats
# Instructions
# Using this class

#Solution EX 1:

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
# Instantiate three Cat objects using the code provided above.
# Outside of the class, create a function that finds the oldest cat and returns the cat.
# Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.

cat_1 = Cat("Tusik", 12)
cat_2 = Cat("Pusik", 3)
cat_3 = Cat("Barsik", 7)

def oldest_cat() :
    if cat_1.age > cat_2.age and cat_1.age > cat_3.age :
        print(f"The oldest cat is {cat_1.name}, and it is {cat_1.age} years old.”")
    elif cat_2.age > cat_1.age and cat_2.age > cat_3.age :
        print(f"The oldest cat is {cat_2.name}, and it is {cat_2.age} years old.”")
    elif cat_3.age > cat_1.age and cat_3.age > cat_2.age :
        print(f"The oldest cat is {cat_3.name}, and it is {cat_3.age} years old.”")

oldest_cat()

# Exercise 2 : Dogs
# Instructions
# Create a class called Dog.
# In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
# Create a method called bark that prints the following string “<dog_name> goes woof!”.
# Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
# Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
# Print the details of his dog (ie. name and height) and call the methods bark and jump.
# Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# Print the details of her dog (ie. name and height) and call the methods bark and jump.
# Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.

#Solution EX 2:
class Dog:
    def __init__(self, dog_name, dog_height):
        self.name = dog_name
        self.height = dog_height
    
    def bark(self) :
       print(f"{self.name} goes woof!")

    def jump(self) :
       print(f"{self.name} jumps {self.height * 2} cm high!!")

davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Teacup", 20)

def present_dog_1() :
    print(f"Dog 1: This is {davids_dog.name}! It is {davids_dog.height} cm heigh!")
    print(davids_dog.bark())
    print(davids_dog.jump())

def present_dog_2() :
    print(f"Dog 2: This is {sarahs_dog.name}! It is {sarahs_dog.height} cm heigh!")
    print(sarahs_dog.bark())
    print(sarahs_dog.jump())

def compare_dogs() :
    if davids_dog.height > sarahs_dog.height :
        print(f"{davids_dog.name} is bigger than {sarahs_dog.name}.")
    else :
        print(f"{sarahs_dog.name} is bigger than {davids_dog.name}.")

present_dog_1()
present_dog_2()
compare_dogs()

# Exercise 3 : Who’s The Song Producer?
# Instructions
# Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics (a list).
# Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
# Create an object, for example:
# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
# Then, call the sing_me_a_song method. The output should be:
# There’s a lady who's sure
# all that glitters is gold
# and she’s buying a stairway to heaven

#Solution EX 3:
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self) :
        for index in range(0, len(self.lyrics)):
            print(self.lyrics[index])

stairway = Song(["There's a lady who's sure","all that glitters is gold", "and she's buying a stairway to heaven"])

stairway.sing_me_a_song()


# Exercise 4 : Afternoon At The Zoo
# Instructions
# Create a class called Zoo.
# In this class create a method __init__ that takes one parameter: zoo_name.
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
# Create a method called get_animals that prints all the animals of the zoo.
# Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
# Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
# Example

# { 
#     1: "Ape",
#     2: ["Baboon", "Bear"],
#     3: ['Cat', 'Cougar'],
#     4: ['Eel', 'Emu']
# }






#Solution EX 4:

class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animal = [ ]
        self.dic = { }
        self.new_dict = { }
        self.num_dic = { }
            
    def add_animal(self) :
        new_animal = str()
        while new_animal != "quit" :
            new_animal = input(("Which animal should we add to our zoo? (Type 'quit' to exit) "))
            if new_animal not in self.animal :
                self.animal.append(new_animal)
            else :
                print(f"{new_animal} is already in the Zoo!")
        else :
            self.animal.remove("quit")
    
    #Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.

    def sort_animals(self) :
        self.animal = sorted(self.animal)        
        
#for each animal name in the list
        for index in range (0,len(self.animal)) : 
#if the first letter of this animal name is NOT in the list of keys of the self.new_dict
            if self.animal[index][0] not in self.new_dict.keys() : 
#add the new element to the self.new_dict, where key is the first letter of the animal name, and the value is the animal name
                self.new_dict[self.animal[index][0]] = self.animal[index]
#if the first letter of this animal name is in the list of keys of the self.new_dict
            else : 
#find the element by this key and change its value to: 
                self.new_dict[self.animal[index][0]] = self.new_dict[self.animal[index][0]] + ", " + self.animal[index]
        
        for key in self.new_dict.keys() :
            self.dic[key] = list(self.new_dict[key].split(","))
        

# Create a method called get_groups that prints the animal/animals inside each group.        
    def get_groups(self) :
        
        for index, (key, value) in enumerate(self.dic.items()):
           self.num_dic[index +1] = value
        
    
    def get_animals(self) :
        print(f"The following animals are currently in the zoo: {self.num_dic}")

    def sell_animal(self) :
        animal_sold = str()
        while animal_sold != "quit" :
            animal_sold = input(("Which animal should we sell? (Type 'quit' to exit) "))
            if animal_sold in self.animal :
                self.animal.remove(animal_sold)
                print(f"The {animal_sold} was sold! The following animals are currently in the zoo: {self.animal}")
            else :
                print(f"This animal is not in the zoo!")
        else :
            print(f"The following animals are currently in the zoo: {self.animal}")



# Create an object called ramat_gan_safari and call all the methods.
# Tip: The zookeeper is the one who will use this class.
# Example
# Which animal should we add to the zoo --> Giraffe
# x.add_animal(Giraffe)
 
ramat_gan_safari = Zoo("Ramat Gan Safari")
ramat_gan_safari.add_animal()
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal()