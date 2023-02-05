from decimal import Decimal

class dot_dict(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

shopping_items = []

def validate(value_type_cb, input_msg, error_msg, check_against_cb): 
    while True:
        try:
            value = value_type_cb(input(input_msg))
        except ValueError:
            print(error_msg)
            continue
        else:
            if check_against_cb(value):
                return value
            else:
                print(error_msg)
                continue

def add_item():
    item_name = validate(str, "What item would you like to add? ", "The name is incorrect!", lambda x: x)
    item_price = Decimal('{0:.2f}'.format(validate(float, f"What is the price of {item_name}? ", "The price is incorrect!", lambda x: x >= 0)))
    shopping_items.append(dot_dict({'name': item_name, 'price': item_price}))
    print(f"'{item_name}' has been added to the cart.")

def view_cart():
    if len(shopping_items) == 0:
        print("The shopping cart is empty.")
    else:
        for i in range(len(shopping_items)):
            print(f'{i+1}. {shopping_items[i].name} - ${shopping_items[i].price}')

def remove_item():
    if len(shopping_items) == 0:
        print("The shopping cart is empty.")
    else:
        item_to_remove = validate(int, "Which item would you like to remove? ", "Sorry, that is not a valid item number.", lambda x: x > 0 and x <= len(shopping_items)) - 1
        shopping_items.pop(item_to_remove)
        print("Item removed.")

def compute_total(): 
    if len(shopping_items) == 0:
        print("The shopping cart is empty.")
    else:
        sum = 0 
        for i in range(len(shopping_items)):
            sum = sum + shopping_items[i].price
        print(f"The total price of the items in the shopping cart is ${sum}")

options = {1 : add_item, 2: view_cart, 3: remove_item, 4: compute_total}

print("Welcome to the Shopping Cart Program!\n")

while True:
    print('''Please select one of the following: 
            1. Add item
            2. View cart
            3. Remove item
            4. Compute total
            5. Quit''')
    
    selected_option = validate(int, "Please enter an action: ", "Please, enter a valid option between 1 and 5.", lambda x: x >= 1 and x <= 5)
    if(selected_option != 5):    
        options[selected_option]()
        print()
    else:
        print("Thank you. Goodbye.")
        break    

# Additional creativity: validation of inputs all over the program and check for the cart emptiness where it makes sense