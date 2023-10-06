# Exercise 1 : Geometry
# Instructions
# Write a class called Circle that receives a radius as an argument (default is 1.0).
# Write two instance methods to compute perimeter and area.
# Write a method that prints the geometrical definition of a circle.

class Circle :
    def __init__(self, radius = 1.0) :
        self.radius = radius

    def perimeter(self) :
        import math
        self.perimeter = 2 * math.pi * self.radius
        print(f"Perimeter of the circle with this radius = {round(self.perimeter, 2)}")

    def area(self) :
        import math
        self.area = math.pi * (self.radius ** 2)
        print(f"Area of the circle with this radius = {round(self.area, 2)}")

    def definition(self) :
        print('''
              A circle is a closed two-dimensional figure in which the set of all the points in the plane
              is equidistant from a given point called “centre”. Every line that passes through the circle 
              forms the line of reflection symmetry. Also, it has rotational symmetry around the centre 
              for every angle.
              ''')

circle = Circle(3)
circle.perimeter()
circle.area()
circle.definition()
circle_01 = Circle(5)
circle_01.perimeter()


# Exercise 2 : Custom List Class
# Instructions
# Create a class called MyList, the class should receive a list of letters.
# Add a method that returns the reversed list.
# Add a method that returns the sorted list.
# Bonus : Create a method that generates a second list with the same length as mylist. 
# The list should be constructed with random numbers. (use list comprehension).

class MyList :
    def __init__(self, list) :
        self.list = list

    def reversed(self) :
        self.reversed_list = self.list[::-1]
        print(f"Reversed list: {self.reversed_list}")

    def sorted(self) :
        self.sorted_list = sorted(self.list)
        print(f"Sorted list: {self.sorted_list}")

    def rand_num(self) :
        import random
        self.rand_num_list = [random.randint(0, 100) for item in self.list]
        print(f"A list of random numbers: {self.rand_num_list}")

new_list = MyList(["Mary", "has", "9", "a", "156", "True", "little", "lamb."])
new_list.reversed()
new_list.sorted()
new_list.rand_num()


# Exercise 3 : Restaurant Menu Manager
# Instructions
# The purpose of this exercise is to create a restaurant menu. The code will allow a manager to add and delete dishes.

# Create a python file called menu_manager.py.

class MenuManager :
    def __init__(self, menu) :
        self.menu = menu
    
    def add_item(self, **kwargs) :
        item_dict = kwargs
        self.menu.append(item_dict)
        print(self.menu)

    def update_item(self, **kwargs) :
        item_dict = kwargs
        for element in self.menu :
            if element['name'] == item_dict['name'] :
                list_index = self.menu.index(element)
                self.menu[list_index] = item_dict
                print(self.menu)
 
    def remove_item(self, name) :
        self.name = name
        for element in self.menu :
            if element['name'] == self.name :
                list_index = self.menu.index(element)
                self.menu.pop(list_index)
                print(self.menu)
              


# Create a class called MenuManager.

# Create a method __init__ that instantiates an attribute called menu. 
# The menu attributes value will be all the current dishes (list of dictionaries). 
# Each dish will be stored in a dictionary where the keys are name, price, spice level and gluten index (which value is a boolean).

menu = [
    {"name" : "Soup", "price" : 10, "spice_level" : "B", "gluten_index" : False}, 
    {"name" : "Hamburger", "price" : 15, "spice_level" : "A", "gluten_index" : True}, 
    {"name" : "Salad", "price" : 18, "spice_level" : "A", "gluten_index" : False}, 
    {"name" : "French Fries", "price" : 5, "spice_level" : "C", "gluten_index" : False}, 
    {"name" : "Beef bourguignon", "price" : 25, "spice_level" : "B", "gluten_index" : True}
    ]

menu_current = MenuManager(menu)
menu_current.add_item(name = "Gaspacho", price = 22, spice_level = "C", gluten_index = False)
menu_current.update_item(name = "Salad", price = 13, spice_level = "B", gluten_index = False)
menu_current.remove_item("Beef bourguignon")


#     Meaning: For the spice level:
#        • A = not spicy,
#        • B = a little spicy,
#        • C = very spicy


# Create a method called add_item(name, price, spice, gluten). This method will add new dishes to the menu.
# Create a method called update_item(name, price, spice, gluten). This method checks whether a dish is in the menu, if the dish exists then update it. If not notify the manager that the dish is not in the menu.
# Create a method called remove_item(name). This method should check if the dish is in the menu, if the dish exists then delete it and print the updated dictionary. If not notify the manager that the dish is not in the menu.

