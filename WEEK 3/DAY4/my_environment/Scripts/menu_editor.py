from menu_item import MenuItem
from menu_manager import MenuManager

def show_user_menu():
    print("Menu Manager")
    print("V: View an Item")
    print("A: Add an Item")
    print("D: Delete an Item")
    print("U: Update an Item")
    print("S: Show the Menu")
    print("E: Exit")

    choice = input("Choose an option: ").upper()
    if choice == 'V':
        view_item()
    elif choice == 'A':
        add_item_to_menu()
    elif choice == 'D':
        remove_item_from_menu()
    elif choice == 'U':
        update_item_from_menu()
    elif choice == 'S':
        show_restaurant_menu()
    elif choice == 'E':
        exit_program()
    else:
        print("Invalid choice, please try again.")
        show_user_menu()

def view_item():
    name = input("Enter the name of the item you want to view: ")
    item = MenuManager.get_by_name(name)
    if item:
        print(f"Item: {item[1]}, Price: {item[2]}")
    else:
        print("Item not found.")
    show_user_menu()

def add_item_to_menu():
    name = input("Enter the name of the item: ")
    price = int(input("Enter the price of the item: "))
    item = MenuItem(name, price)
    item.save()
    print(f"{name} was added successfully.")
    show_user_menu()

def remove_item_from_menu():
    name = input("Enter the name of the item you want to remove: ")
    item = MenuItem(name, 0)
    item.delete()
    print(f"{name} was deleted successfully.")
    show_user_menu()

def update_item_from_menu():
    name = input("Enter the name of the item you want to update: ")
    new_name = input("Enter the new name of the item: ")
    new_price = int(input("Enter the new price of the item: "))
    item = MenuItem(name, 0)
    item.update(new_name, new_price)
    print(f"{name} was updated successfully.")
    show_user_menu()

def show_restaurant_menu():
    items = MenuManager.all_items()
    for item in items:
        print(f"Item: {item[1]}, Price: {item[2]}")
    show_user_menu()

def exit_program():
    show_restaurant_menu()
    print("Exiting program.")
    exit()

if __name__ == "__main__":
    show_user_menu()
