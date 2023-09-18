# Exercise 1 : Pets
# Instructions
# Using this code:

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# Create another cat breed named Siamese which inherits from the Cat class.

class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# Create a list called all_cats, which holds three cat instances : one Bengal, one Chartreux and one Siamese.

patty_cat = Bengal("Patty", 5)
tusik_cat = Chartreux("Tusik", 3)
pisik_cat = Chartreux("Pisik", 1)
all_cats = [patty_cat, tusik_cat, pisik_cat]
print(all_cats)

# Those three cats are Sara’s pets. Create a variable called sara_pets which value is an instance of the Pet class, and pass the variable all_cats to the new instance.

sara_pets = Pets(all_cats)

# Take all the cats for a walk, use the walk method.

sara_pets.walk()


# Exercise 2 : Dogs
# Instructions
# Create a class called Dog with the following attributes name, age, weight.
# Implement the following methods in the Dog class:
# bark: returns a string which states: “<dog_name> is barking”.
# run_speed: returns the dogs running speed (weight/age*10).
# fight : takes a parameter which value is another Dog instance, called other_dog. This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.

class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking'

    def run_speed(self):
        return f"The {self.name}'s running speeed is {self.weight/self.age*10} km/h"
    
    def fight(self, other_dog):
        self.state = self.run_speed() * self.weight
        other_dog.state = other_dog.run_speed() * other_dog.weight
        if self.state > other_dog.state :
            return f"{self.name} won!"
        else :
            return f'{other_dog.name} won!'

tuzik_dog = Dog("Tuzik", 8, 45)
murzik_dog = Dog("Murzik", 4, 60)
pusik_dog = Dog("Pusik", 2, 34)


tuzik_dog.bark()
murzik_dog.run_speed()
tuzik_dog.fight(murzik_dog)


# Create 3 dogs and run them through your class.


# Exercise 3 : Dogs Domesticated
# Instructions
# Create a new python file and import your Dog class from the previous exercise.
# In the new python file, create a class named PetDog that inherits from Dog.
# Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
# Add the following methods:
# train: prints the output of bark and switches the trained boolean to True

# play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string: “dog_names all play together”.

# do_a_trick: If the dog is trained the method should print one of the following sentences at random:
# “dog_name does a barrel roll”.
# “dog_name stands on his back legs”.
# “dog_name shakes your hand”.
# “dog_name plays dead”.

from xp_exercises import Dog

class PetDog(Dog) :
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight) # calling a method from a parent class
        self.trained = False
        self.name = name

    def train(self) :
        if not self.trained :
            print(self.bark())
            self.trained = True
            print(f"{self.name} is trained!")
           

    def play(self, *dog_names) :
        print(f"{self.name}, {', '.join(dog_names)} play together!")


    def do_a_trick(self) :
        import random
        r_num = random.randint(1,5)
        sentences_dict = {1 : "does a barrel roll", 2 : "stands on his back legs", 3 : "shakes your hand", 4 : "plays dead"}
        if self.trained :
            print(f"{self.name} {sentences_dict[r_num]}")
        else :
            print(f"{self.name} is not trained!")

if __name__ == "__main__": # this code module runs as main 
    tuzik_dog = PetDog("Tuzik", 8, 45)
    tuzik_dog.train()
    tuzik_dog.play("Murzik", "Puzik")
    tuzik_dog.do_a_trick()

