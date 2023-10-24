# In the file menu_manager.py, create a new class called MenuManager
import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'postgres'
DATABASE = 'devinst'

connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
cursor = connection.cursor()

class MenuManager :
    
    def get_by_name(name, table_name = "menu_items") :
        query = f"SELECT item_name, item_price FROM {table_name} WHERE item_name = '{name}';"
        cursor.execute(query)
        results = cursor.fetchall()
        if results == [] :
            print("There is no such item in the current menu.")
        else:
            print(results)
        connection.close()

    def all_items(table_name = "menu_items") :
        query = f"SELECT item_name, item_price FROM {table_name};"
        cursor.execute(query)
        results = cursor.fetchall()
        print(results)
        connection.close()

# Create a Class Method called get_by_name that will return a single item from the Menu_Items table depending on it’s name, 
# if an object is not found (there is no item matching the name in the get_by_name method) return None.

# Create a Class Method called all_items which will return a list of all the items from the Menu_Items table.

# item3 = MenuManager.get_by_name('Beef Stew')
# items = MenuManager.all_items()
# item2 = MenuManager.get_by_name('Cola')