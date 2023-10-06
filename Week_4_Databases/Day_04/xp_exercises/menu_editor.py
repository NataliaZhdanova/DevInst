# Create a file called menu_editor.py , which will have the following functions:
# show_user_menu() - this function should display the program menu (not the restaurant menu!), and ask the user to :
# View an Item (V)
# Add an Item (A)
# Delete an Item (D)
# Update an Item (U)
# Show the Menu (S)
# Call the appropriate function that matches the user’s input.
import menu_item
import menu_manager

def show_user_menu() :
    print("Please, select one of the options below: \n")
    option = input('''
                   - View an Item (V)
                   - Add an Item (A)
                   - Delete an Item (D)
                   - Update an Item (U)
                   - Show the Menu (S)
                   - Exit the Menu (E)
                   ''')
    if option == "V" :
        name = input("What item are you interested in?")
        item = menu_manager.MenuManager.get_by_name(name)
        print(item)
    elif option == "A" :
        add_item_to_menu()
    elif option == "D" :
        remove_item_from_menu()
    elif option == "U" :
        update_item_from_menu()
    elif option == "S" :
        show_restaurant_menu()
    elif option == "E" :
        show_restaurant_menu()
        exit

# add_item_to_menu() - this function should ask the user to input the item’s name and price. 
# This function will not interact with the menu itself, but simply create a MenuItem object and call the appropriate function from 
# the MenuItem object.
# If the item was added successfully print a message which states: item was added successfully.

def add_item_to_menu() :
    name = input("Please enter a name of the dish: ")
    price = int(input("Please enter a price of the dish: "))
    item = menu_item.MenuItem(name, price)
    try:
        item.save()
        print(f"The {name} was added successfully!")
    except Exception as e:
        print(f"Error: {e}")
    

# remove_item_from_menu()- this function should ask the user to input the name of the item they want to remove from the restaurant’s menu. This function will not interact with the menu itself, but simply create a MenuItem object and call the appropriate function from the MenuItem object.
# If the item was deleted successfully – print a message to let the user know this was completed.
# If not – print a message which states that there was an error.

def remove_item_from_menu() :
    name = input("Please enter a name of the dish to delete: ")
    
    try:
        menu_item.MenuItem.delete_by_name(name)
        print(f"The {name} was deleted successfully!")
    except Exception as e:
        print(f"Error: {e}")
    

# update_item_from_menu()- this function should ask the user to input the name and price of the item they want to update from the restaurant’s menu, as well as to input the name and price they want to change them with. This function will not interact with the menu itself, but simply create a MenuItem object and call the appropriate function from the MenuItem object.
# If the item was updated successfully – print a message to let the user know this was completed.
# If not – print a message which states that there was an error.

def update_item_from_menu() :
    old_name = input("Please enter a name of the dish you want to update: ")
    name = input("Please enter a new name of the dish: ")
    price = int(input("Please enter a new price of the dish: "))    
    try:
        menu_item.MenuItem.update_by_name(old_name, name, price)
        print(f"The {name} was updated successfully!")
    except Exception as e:
        print(f"Error: {e}")

# show_restaurant_menu() - print the restaurant’s menu.
def show_restaurant_menu() :
    items = menu_manager.MenuManager.all_items()
    print(items)
    

# When the user chooses to exit the program, display the restaurant menu and exit the program.


if __name__ == "__main__" :
    show_user_menu()