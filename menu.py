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

# # 1. Set up order list. Order list will store a list of dictionaries for
# # menu item name, item price, and quantity ordered
# order = []

# # Launch the store and present a greeting to the customer
# print("Welcome to the variety food truck.")

# # Function to display a menu section (including nested items)
# def display_menu(menu, level=0):
#     indent = "    " * level
#     for item, price in menu.items():
#         if isinstance(price, dict):
#             print(f"{indent}{item}:")
#             display_menu(price, level + 1)
#         else:
#             print(f"{indent}{item} - ${price:.2f}")

# while True:
#     print("\nMenu:")
#     display_menu(menu)
    
#     # Input for choosing a section/item
#     section_choice = input("\nEnter a section (Snacks, Meals, Drinks, Dessert or 'exit' to finish): ").title()
    
#     if section_choice.lower() == "exit":
#         break
    
#     if section_choice in menu:
#         # Display the chosen section
#         print(f"\n{section_choice}:")
#         display_menu(menu[section_choice])
        
#         # Input for choosing an item within the section
#         item_choice = input(f"\nChoose an item from {section_choice}: ").title()
        
#     if item_choice in menu[section_choice]:
#             # If the item is a nested dict (like pizza flavors), display sub-options
#             if isinstance(menu[section_choice][item_choice], dict):
#                 print(f"\n{item_choice} options:")
#                 display_menu(menu[section_choice][item_choice])
                
#                 # Choose a sub-item
#                 sub_item_choice = input(f"\nChoose an option for {item_choice}: ").title()
                
#                 if sub_item_choice in menu[section_choice][item_choice]:
#                     price = menu[section_choice][item_choice][sub_item_choice]
#                     quantity = input(f"Enter quantity for {sub_item_choice} (default 1): ")
#                     quantity = int(quantity) if quantity.isdigit() else 1
#                     order.append({
#                         "Item": f"{item_choice} ({sub_item_choice})",
#                         "Price": price,
#                         "Quantity": quantity
#                     })
#         else:
#                 # If it's a regular item, just add it
#                 price = menu[section_choice][item_choice]
#                 quantity = input(f"Enter quantity for {item_choice} (default 1): ")
#                 quantity = int(quantity) if quantity.isdigit() else 1
#                 order.append({
#                     "Item": item_choice,
#                     "Price": price,
#                     "Quantity": quantity
#                 })
#     else:
#         print(f"{item_choice} is not available in {section_choice}.")
# else:
#     print(f"{section_choice} is not a valid section.")
    
# # Display the final order summary
# print("\nYour Order:")
# total = 0
# for item in order:
#     print(f"{item['Quantity']}x {item['Item']} - ${item['Price'] * item['Quantity']:.2f}")
#     total += item['Price'] * item['Quantity']

# print(f"\nTotal: ${total:.2f}")

# 1. Set up order list. Order list will store a list of dictionaries for
# #  menu item name, item price, and quantity ordered
order = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order  =  True
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
    menu_category = input("Type menu number:")

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
                        num_item_spaces = 24 - len(key  + key2) - 3
                        item_spaces = "  "  *  num_item_spaces
                        print(f"{i} | {key} - {key2}{item_spaces} | ${value2}")
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
            item_number = input("Please enter the menu item number: ")

            # 3. Check if the customer typed a number
            if  item_number.isdigit():
                # Convert the menu selection to an integer
                item_number = int(item_number)

                # 4. Check if the menu selection is in the menu items
                if item_number in menu_items.keys():    #Revati-TA
                #if  item_number in menu_items:
                    # Store the item name as a variable
                    Selection_made = menu_items[item_number]["Item name"]
                    # Item_name = Selection_made["Item name"]
                    Item_price = menu_items[item_number]["Price"]

                    # Ask the customer for the quantity of the menu item
                    quantity = input(f"How many {Selection_made} would you like to order? (default is 1 if invalid input) ")

                    # Check if the quantity is a number, default to 1 if not  #Revati-TA
                    if not quantity.isdigit():
                        quantity = 1
                    else:
                        quantity = int(quantity)
                    
                    # # Check if the quantity is a number, default to 1 if not
                    # if not Quantity.isdigit():
                    #     quantity = int(Quantity)
                    # else:

                    #     print("invalid quantity entered, defaulting to 1.")
                    #     quantity = 1


                    # Add the item name, price, and quantity to the order lists
                    order.append({
                        "Item name": Selection_made,    #Revati-TA
	                    #"Item_name" : Selection_made,
	                    "Price" : Item_price,
                        "quantity":quantity
	                    #"Quantity" : quantity
                    })
                else:
                    # Tell the customer that their input isn't valid
                    print("Sorry, that number isn't an option.")
            else:
                # Tell the customer they didn't select a menu option
                print(f"{item_number} was not a menu option.")
        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")
        
        #5. Check the customer's input    #Revati-TA
        if keep_ordering.lower() == 'y':
            # Keep ordering
            place_order = True
            break
        elif keep_ordering.lower() == 'n':
            # Complete the order
            place_order = False
            print("Thank you for your order.")
            break
        else:
            # Tell the customer to try again
            print("I didn't understand your response. Please try again.")

        # # 5. Check the customer's input
        # keep_ordering = keep_ordering.upper()
                
        # #  Keep ordering
        # if keep_ordering == "Y":
        # #  Exit the keep ordering question loop
        #     break
        # #  Complete the order
        #     # Since the customer decided to stop ordering, thank them for
        #     # their order
        # if keep_ordering == 'N':
        #     print("Thank you for your order!")
        #     break 
        
# Exit the keep ordering question loop

## Tell the customer to try again
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order\
print(order)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

#6. Loop through the items in the customer's order
for item in range(len(order)):


    # 7. Store the dictionary items as variables
    item_name = order[item]["Item name"]
    item_price = order[item]["Price"]
    item_quantity = order[item]["quantity"]

    # 8. Calculate the number of spaces for formatted printing
    # price_formatted = f"${item_price:.2f}"
    # quantity_formatted = f"{item_quantity:>8}"
    num_item_spaces = 30 - len(item_name)
    num_price_spaces = 8 - len(str(item_price))

    # 9. Create space strings
    item_spaces = " " * num_item_spaces
    price_spaces = " " * num_item_spaces

    # 10. Print the item name, price, and quantity
    print(f"{item_name}{item_spaces} | {item_price}{price_spaces} | {item_quantity}")

# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.#
total_cost = sum(item["Price"] * item["quantity"] for item in order)
print(f"\nTotal cost of your order: ${total_cost:.2f}")
##Second submission revision of code completed ###
