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
