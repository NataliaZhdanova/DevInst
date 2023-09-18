# Exercise 1 : Family
# Instructions
# Create a class called Family and implement the following attributes:

# members: list of dictionaries with the following keys : name, age, gender and is_child (boolean).
# last_name : (string)
# Initial members data:

# [
#     {'name':'Michael','age':35,'gender':'Male','is_child':False},
#     {'name':'Sarah','age':32,'gender':'Female','is_child':False}
# ]

class Family() :
    def __init__(self, last_name):
        self.members = []
        self.last_name = last_name


    def add_member(self, **kwargs) :
        self.member = {'name': kwargs.get('name', ''), 'age': kwargs.get('age', 0), 'gender': kwargs.get('gender', ''), 'is_child': kwargs.get('is_child', False)}
        self.members.append(self.member)
        print(self.members)

    def born(self, **kwargs) :
        self.member = {'name': kwargs.get('name', ''), 'age': kwargs.get('age', 0), 'gender': kwargs.get('gender', ''), 'is_child': kwargs.get('is_child', False)}
        self.members.append(self.member)
        print(f"Congrats! {kwargs.get('name', '')} was born!")
        print(self.members)

    def is_18(self, name) :
        self.name = name
        
        for index in range(0, len(self.members)) :
            if self.members[index]['name'] == self.name :
                self.age = self.members[index]['age']
                if self.age >= 18 :
                    return True
                else :
                    return False
        

    def family_presentation(self) :
        members_names = list()
        for index in range(0, len(self.members)) :
            members_names.append(self.members[index]['name'])
        print(f"{', '.join(members_names)} are from {self.last_name} family!")


family = Family("Fitzpatrick")
family.add_member(name='Michael', age=35, gender='Male', is_child=False)
family.add_member(name='Sarah', age=32, gender='Female', is_child=False)

family.born(name='Mary', age=0, gender='Female', is_child=True)
family.is_18('Sarah')
family.family_presentation()


# Exercise 2 : TheIncredibles Family
# Instructions
# Create a class called TheIncredibles. This class should inherit from the Family class:
# This is no random family they are an incredible family, therefore we need to add the following keys to our dictionaries: power and incredible_name.

# Initial members data:

# [
#     {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
#     {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
# ]

class TheIncredibles(Family) :
    def __init__(self, last_name):
        super().__init__(last_name) # calling a method from a parent class
        self.members = []
        self.last_name = last_name

    def add_member(self, **kwargs) :
        self.member = {'name': kwargs.get('name', ''), 'age': kwargs.get('age', 0), 'gender': kwargs.get('gender', ''), 'is_child': kwargs.get('is_child', False), 'power': kwargs.get('power', ''), 'incredible_name': kwargs.get('incredible_name', '') }
        self.members.append(self.member)
        print(self.members)

# Add a method called use_power, this method should print the power of a member only if they are over 18 years old. If not raise an exception (look up exceptions) which stated they are not over 18 years old.

    def use_power(self):
    user_age = input("How old are you?\n>>> ")
    #######
    try:
        user_age = int(user_age)
        print("I AM AFTER USER_AGE")
    except:
        print("Your age is not a real age")
        user_age = 0
    #######
    print("Next year, you will be {} years old".format(user_age+1))

age()



# Add a method called incredible_presentation which :

# Prints the family’s last name and all the members’ first name (ie. use the super() function, to call the family_presentation method)
# Prints all the members’ incredible name and power.

# Call the incredible_presentation method.


# Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.


# Call the incredible_presentation method again.
