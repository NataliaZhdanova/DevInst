# Instructions :
# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.

# Other abilities of a Circle instance:

# Compute the circle’s area
# Print the attributes of the circle - use a dunder method
# Be able to add two circles together, and return a new circle with the new radius - use a dunder method
# Be able to compare two circles to see which is bigger, and return a Boolean - use a dunder method
# Be able to compare two circles and see if there are equal, and return a Boolean- use a dunder method
# Be able to put them in a list and sort them

import math

class Circle :
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("Please specify either radius or diameter")

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return round(math.pi * (self.radius ** 2), 2)

    def __str__(self):
        return f"Circle with radius: {self.radius}"

    def __add__(self, other_cir):
        return Circle(self.radius + other_cir.radius)

    def __lt__(self, other_cir):
        return self.radius < other_cir.radius

    def __eq__(self, other_cir):
        return self.radius == other_cir.radius

    def __le__(self, other_cir):
        return self.radius <= other_cir.radius


cir_1 = Circle(radius=4)
cir_2 = Circle(diameter=10)
cir_3 = Circle(radius=7)

cir_1.area

circles = [cir_1, cir_2, cir_3]
circles.sort()
for element in circles :
    print(element)
