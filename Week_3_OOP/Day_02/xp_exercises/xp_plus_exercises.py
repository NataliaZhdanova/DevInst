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

    def is_18(self, name) :
        self.name = name
        
        for index in range(0, len(self.members)) :
            if self.members[index]['name'] == self.name :
                self.age = self.members[index]['age']
                if self.age >= 18 :
                    return True, self.name
                else :
                    return False, self.name
        

    def family_presentation(self) :
        members_names = list()
        for index in range(0, len(self.members)) :
            members_names.append(self.members[index]['name'])
        print(f"{', '.join(members_names)} are from {self.last_name} family!")


# family = Family("Fitzpatrick")
# family.add_member(name='Michael', age=35, gender='Male', is_child=False)
# family.add_member(name='Sarah', age=32, gender='Female', is_child=False)

# family.born(name='Mary', age=0, gender='Female', is_child=True)
# family.is_18('Sarah')
# family.family_presentation()


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

# Add a method called use_power, this method should print the power of a member only if they are over 18 years old. If not raise an exception (look up exceptions) which stated they are not over 18 years old.

    def use_power(self, name):
        age_check = super().is_18(name)
        self.name = name
        try:
            if age_check[0] == True :
                for index in range(0, len(self.members)) :
                    if self.members[index]['name'] == self.name :
                        self.power = self.members[index]['power']
                print(f"{self.name}'s superpower is {self.power}")
        except:
         print(f"{self.name} is not over 18 years old")

    def inc_presentation(self) :
        super().family_presentation()
        presentation_dict = { }
        for index in range(0, len(self.members)) :
            presentation_dict[self.members[index]['name']] = self.members[index]['power']
        for key, value in presentation_dict.items() :
            print(f"{key} can {value}.")

    def inc_born(self, **kwargs) :
        super().born(**kwargs)
        for index in range(0, len(self.members)) :
                    if self.members[index]['name'] == kwargs.get('name', '') :
                       self.members[index]['power'] = kwargs.get('power', '')
        
        print(self.members)

family_inc = TheIncredibles("Fitzpatrick")
family_inc.add_member(name='Michael', age=35, gender='Male', is_child=False, power='fly', incredible_name='MikeFly')
family_inc.add_member(name='Sarah', age=32, gender='Female', is_child=False, power='read minds', incredible_name='SuperWoman')
family_inc.use_power('Sarah')
family_inc.inc_presentation()
family_inc.inc_born(name='Baby Jack', age=0, gender='Male', is_child=True, power='Unknown Power')
family_inc.inc_presentation()

# Add a method called incredible_presentation which :
# Prints the family’s last name and all the members’ first name (ie. use the super() function, to call the family_presentation method)
# Prints all the members’ incredible name and power.
# Call the incredible_presentation method.
# Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.
# Call the incredible_presentation method again.
