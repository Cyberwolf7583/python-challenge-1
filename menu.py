# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza - Cheese": 8.99,
        "Pizza - Pepperoni": 10.99,
        "Pizza - Vegetarian": 9.99,    
        "Burger - Chicken": 7.49,
        "Burger - Beef": 8.49
        },
    "Drinks": {
        "Soda - Small": 1.99,
        "Soda - Medium": 2.49,
        "Soda - Large": 2.99,
        "Tea - Green": 2.49,
        "Tea - Thai iced": 3.99,
        "Tea - Irish breakfast": 2.49,
        "Coffee - Espresso": 2.99,
        "Coffee - Flat white": 2.99,
        "Coffee - Iced": 3.49
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake - New York": 4.99,
        "Cheesecake - Strawberry": 6.49,
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# Set up an order list
order = []

# Function to display a menu section (including nested items)
def display_menu(menu, level=0):
    indent = "    " * level
    for item, price in menu.items():
        if isinstance(price, dict):
            print(f"{indent}{item}:")
            display_menu(price, level + 1)
        else:
            print(f"{indent}{item} - ${price:.2f}")

while True:
    print("\nMenu:")
    display_menu(menu)
    
    # Input for choosing a section/item
    section_choice = input("\nEnter a section (Snacks, Meals, Drinks, Dessert or 'exit' to finish): ").title()
    
    if section_choice.lower() == "exit":
        break
    
    if section_choice in menu:
        # Display the chosen section
        print(f"\n{section_choice}:")
        display_menu(menu[section_choice])
        
        # Input for choosing an item within the section
        item_choice = input(f"\nChoose an item from {section_choice}: ").title()
        
        if item_choice in menu[section_choice]:
            # If the item is a nested dict (like pizza flavors), display sub-options
            if isinstance(menu[section_choice][item_choice], dict):
                print(f"\n{item_choice} options:")
                display_menu(menu[section_choice][item_choice])
                
                # Choose a sub-item
                sub_item_choice = input(f"\nChoose an option for {item_choice}: ").title()
                
                if sub_item_choice in menu[section_choice][item_choice]:
                    price = menu[section_choice][item_choice][sub_item_choice]
                    quantity = input(f"Enter quantity for {sub_item_choice} (default 1): ")
                    quantity = int(quantity) if quantity.isdigit() else 1
                    order.append({
                        "Item": f"{item_choice} ({sub_item_choice})",
                        "Price": price,
                        "Quantity": quantity
                    })
            else:
                # If it's a regular item, just add it
                price = menu[section_choice][item_choice]
                quantity = input(f"Enter quantity for {item_choice} (default 1): ")
                quantity = int(quantity) if quantity.isdigit() else 1
                order.append({
                    "Item": item_choice,
                    "Price": price,
                    "Quantity": quantity
                })
        else:
            print(f"{item_choice} is not available in {section_choice}.")
    else:
        print(f"{section_choice} is not a valid section.")
    
# Display the final order summary
print("\nYour Order:")
total = 0
for item in order:
    print(f"{item['Quantity']}x {item['Item']} - ${item['Price'] * item['Quantity']:.2f}")
    total += item['Price'] * item['Quantity']

print(f"\nTotal: ${total:.2f}")

# order_list = ("snacks", "meals", "drinks", "dessert")

print("order_list")

order = []

while True:
    print("Menu:")
    for i, (item, price) in enumerate(menu.items(), 1):
        print(f"{i}. {item} - ${price}")
    
    choice = input("Choose an item number: ")
    if choice.isdigit() and int(choice) in range(1, len(menu) + 1):
        item_name = list(menu.keys())[int(choice) - 1]
        quantity = input("Enter quantity (default 1): ")
        quantity = int(quantity) if quantity.isdigit() else 1
        
        order.append({
            "Item name": item_name,
            "Price": menu[item_name],
            "Quantity": quantity
        })
        
    cont = input("Keep ordering? (Y/N): ").lower()
    if cont == 'n':
        break

print("Order:", order)



#  Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
# Initialize an empty order list
order_list = []


# Example of how the order_list might look after adding items
print(order_list)


# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
            menu_item_number = int(input("Please enter the menu item number: "))
            # Display menu items (assuming you have a menu list with item numbers)
menu = {}            
item_number = 1
for category, items in menu.items():
    print(f"\n{category}:")
    for item, price in items.items():
        print(f"{item_number}. {item} - ${price:.2f}")
        item_number += 1


# Print the menu to show options
print("Menu:")
for number, item in menu.items():
    print(f"{number}: {item}")

# Ask customer to input menu item number
menu_item_number = int(input("Please enter the menu item number: "))

# Confirm their selection
if menu_item_number in menu:
    print(f"You selected: {menu[menu_item_number]}")
else:
    print("Invalid menu item number.")


            # 3. Check if the customer typed a number

if user_input.isdigit():
    number = int(user_input)
    print(f"Input '{number}' is a number!")
else:
    print(f"{user_input} is not a number.")

    print("That is not a valid number. Please enter a number.")           

                # Convert the menu selection to an integer


                # 4. Check if the menu selection is in the menu items
    if menu_item_number in menu:
        print(f"You selected: {menu[menu_item_number]}")
    else: 
        raise ValueError("That is not a valid number. Please enter a number.")
              

                    # Store the item name as a variable


                    # Ask the customer for the quantity of the menu item


                    # Check if the quantity is a number, default to 1 if not


                    # Add the item name, price, and quantity to the order list


                    # Tell the customer that their input isn't valid


                # Tell the customer they didn't select a menu option


            # Tell the customer they didn't select a menu option
    print(f"{menu_category} was not a menu option.")
        # Tell the customer they didn't select a number
    print("You didn't select a number.")

while True:
        # Ask the customer if they would like to order anything else
    keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

        # 5. Check the customer's input
    customer_input = input("What is your menu selection: ")
if customer_input.isdigit():
    age = int(customer_input)
    print(f"Thank you, your age is {age}.")
else:
    print("Invalid input. Please enter a number.") 

                # Keep ordering

                # Exit the keep ordering question loop

                # Complete the order

                # Since the customer decided to stop ordering, thank them for
                # their order

                # Exit the keep ordering question loop


                # Tell the customer to try again


# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
print(order)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order
customer_order == [customer_input == input] 

    # 7. Store the dictionary items as variables
snacks = customer_order["snacks"]
meals = customer_order["meals"]
drinks = customer_order["drinks"]
desserts = customer_order["desserts"]




    # 8. Calculate the number of spaces for formatted printing
field_width = 15
print(f"{'Item':<{field_width}} {'Order':<{field_width}}")
for item, order in customer_order.items():
    print(f"{item:<{field_width}} {order:<{field_width}}")

    # 9. Create space strings
    print("-" * 40)


    # 10. Print the item name, price, and quantity
# Customer's order as a dictionary with item names, prices, and quantities
customer_order = {
    "Pizza": {"price": 12.99, "quantity": 2},
    "Fries": {"price": 3.49, "quantity": 1},
    "Soda": {"price": 1.99, "quantity": 3},
    "Ice Cream": {"price": 4.99, "quantity": 2}
}

# Define the width for formatting
item_width = 15
price_width = 10
quantity_width = 10

# Print the headers
print(f"{'Item':<{item_width}} {'Price':>{price_width}} {'Quantity':>{quantity_width}}")

# Loop through the dictionary to print each item
for item, details in customer_order.items():
    price = details["price"]
    quantity = details["quantity"]
    print(f"{item:<{item_width}} ${price:>{price_width - 1}.2f} {quantity:>{quantity_width}}")
    




# 11. Calculate the cost of the order using list comprehension
total_price = sum(item['price'] * item['quantity'] for item in order)
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
total_price = sum(item['price'] * item['quantity'] for item in order)
print("\nTotal price for your order: ${:.2f}".format(total_price))
