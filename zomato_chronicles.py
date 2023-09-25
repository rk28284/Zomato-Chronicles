import json

# Load menu data from menu.json
with open('menu.json', 'r') as menu_file:
    menu = json.load(menu_file)

def display_menu(menu):
    print("Menu:")
    for dish_id, details in menu.items():
        print(f"{dish_id}: {details['name']} - ${details['price']} ({'Available' if details['available'] else 'Not Available'})")

## add dish
def add_dish(menu):
    dish_id = input("Enter Dish ID: ")
    name = input("Enter Dish Name: ")
    price = float(input("Enter Dish Price: "))
    available = input("Is the Dish Available? (yes/no): ").lower() == 'yes'

    # Add the new dish to the menu dictionary
    menu[dish_id] = {"name": name, "price": price, "available": available}

    # Update menu.json with the new data
    with open('menu.json', 'w') as menu_file:
        json.dump(menu, menu_file, indent=4)
    
    print(f"{name} has been added to the menu.")

##remove
def remove_dish(menu):
    dish_id = input("Enter Dish ID to remove: ")
    if dish_id in menu:
        name = menu[dish_id]['name']
        del menu[dish_id]
        with open('menu.json', 'w') as menu_file:
            json.dump(menu, menu_file, indent=4)
        print(f"{name} has been removed from the menu.")
    else:
        print("Dish not found in the menu.")
##update dishes
def update_availability(menu):
    dish_id = input("Enter Dish ID to update availability: ")
    if dish_id in menu:
        available = input("Is the Dish Available now? (yes/no): ").lower() == 'yes'
        menu[dish_id]['available'] = available
        with open('menu.json', 'w') as menu_file:
            json.dump(menu, menu_file, indent=4)
        print(f"Availability of {menu[dish_id]['name']} has been updated.")
    else:
        print("Dish not found in the menu.")


def take_order(menu, orders):
    display_menu(menu)

    customer_name = input("Enter customer's name: ")
    order_ids = input("Enter dish IDs separated by commas: ").split(',')

    # Check if each dish is available and add it to the order if it is
    order = []
    for dish_id in order_ids:
        if dish_id in menu and menu[dish_id]['available']:
            order.append({'dish_id': dish_id, 'dish_name': menu[dish_id]['name'], 'price': menu[dish_id]['price']})
        else:
            print(f"Dish with ID {dish_id} is not available.")

    if order:
        # Generate a unique order ID
        order_id = len(orders) + 1
        orders[order_id] = {'customer_name': customer_name, 'order': order, 'status': 'received'}
        print(f"Order ID {order_id} received from {customer_name}.")
    else:
        print("No valid dishes added to the order.")

def update_order_status(orders):
    order_id = int(input("Enter order ID to update status: "))
    if order_id in orders:
        new_status = input("Enter new status (preparing/ready for pickup/delivered): ")
        if new_status in ['preparing', 'ready for pickup', 'delivered']:
            orders[order_id]['status'] = new_status
            print(f"Order ID {order_id} status updated to {new_status}.")
        else:
            print("Invalid status.")
    else:
        print("Order not found.")

# Add functions for preparing, ready for pickup, and delivered statuses here if needed.

def review_orders(orders):
    print("All Orders:")
    for order_id, order_info in orders.items():
        print(f"Order ID: {order_id}")
        print(f"Customer: {order_info['customer_name']}")
        print("Order:")
        for dish in order_info['order']:
            print(f"- {dish['dish_name']} (${dish['price']})")
        print(f"Status: {order_info['status']}\n")
