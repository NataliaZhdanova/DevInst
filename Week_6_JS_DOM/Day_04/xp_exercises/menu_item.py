# In the file menu_item.py, create a new class called MenuItem, the attributes should be the name and price of each item.

import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'postgres'
DATABASE = 'devinst'

connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
cursor = connection.cursor()

# Create several methods (save, delete, update) these methods will allow a user to save, delete and update items from the Menu_Items table. 
# The update method can update the name as well as the price of an item.  

class MenuItem :
    def __init__(self, name, price, table_name = "menu_items") :
        self.name = name
        self.price = price
        self.table_name = table_name

    def save(self) :
        query = f"INSERT INTO {self.table_name} (item_name, item_price) VALUES ('{self.name}', {self.price});"
        cursor.execute(query)
        connection.commit()
        connection.close()        
        
    def delete(self) :
        query = f"DELETE FROM {self.table_name} WHERE item_name = '{self.name}';"
        cursor.execute(query)
        connection.commit()
        connection.close()

    def delete_by_name(name, table_name = "menu_items") :
        query = f"DELETE FROM {table_name} WHERE item_name = '{name}';"
        cursor.execute(query)
        connection.commit()
        connection.close()
        
    def update(self, name, price) :
        self.new_name = name
        self.new_price = price
        query = f"UPDATE {self.table_name} SET item_price = {self.new_price}, item_name = '{self.new_name}' WHERE item_name = '{self.name}';"
        cursor.execute(query)
        connection.commit()
        connection.close()
    
    def update_by_name(old_name, name, price, table_name = "menu_items") :
        query = f"UPDATE {table_name} SET item_price = {price}, item_name = '{name}' WHERE item_name = '{old_name}';"
        cursor.execute(query)
        connection.commit()
        connection.close()

# -- Codebox:

# item = MenuItem('Burger', 35)
# item.save()
# item_01 = MenuItem('Cola', 18)
# item_01.save()
# item_02 = MenuItem('Pepsi', 10)
# item_02.save()
# item.delete()
# item_02.update('Pepsi-cola', 20)



