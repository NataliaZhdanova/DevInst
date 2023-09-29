# In the file menu_item.py, create a new class called MenuItem, the attributes should be the name and price of each item.

class MenuItem :
    def __init__(self, item_name, item_price) :
        self.name = item_name
        self.price = item_price

    def save(self) :
        pass

    def delete(self) :
        pass

    def update(self, item_name, item_price) :
        pass


# Create several methods (save, delete, update) these methods will allow a user to save, delete and update items from the Menu_Items table. 
# The update method can update the name as well as the price of an item.    

class MenuManager :
    def __init__(self, item_name) :
        self.name = item_name

    def get_by_name(self, item_name) :
        pass

    def all_items(self) :
        pass

# Create a Class Method called get_by_name that will return a single item from the Menu_Items table depending on it’s name, 
# if an object is not found (there is no item matching the name in the get_by_name method) return None.

# Create a Class Method called all_items which will return a list of all the items from the Menu_Items table.

# -- Codebox:

# -- item = MenuItem('Burger', 35)
# -- item.save()
# -- item.delete()
# -- item.update('Veggie Burger', 37)
# -- item2 = MenuManager.get_by_name('Beef Stew')
# -- items = MenuManager.all()


