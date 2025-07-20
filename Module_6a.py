Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
class ItemToPurchase:
    def __init__(self, name="none", description="none", price=0, quantity=0):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

        
def print_item_cost(self):
    total = self.price * self.quantity
    print(f"{self.name} {self.quantity} @ ${self.price} = ${total}")

    
def print_item_description(self):
    print(f"{self.name}: {self.description}")

    
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

        
def add_item(self, item):
    self.cart_items.append(item)
... 
...     
>>> def remove_item(self, item_name):
...     found = False
...     for item in self.cart_items:
...         if item.name == item_name:
...             self.cart_items.remove(item)
...             found = True
...             break
...         if not found:
...             print("Item not found in cart. Nothing removed.")
... 
...             
>>> def modify_items(self, item_to_modify):
...     found = False
...     for item in self.cart_items:
...         if item.name == item_to_modify.name:
...             found = True
...             if item_to_modify.description != "none":
...                 item.description = item_to_modify.description
...             if item_to_modify.price != 0:
...                 item.price = item_to_modify.price
...             if item_to_modify.quantity != 0:
...                 item.quantity = item_to_modify.quantity
...                 break
...     if not found:
...         print("Item not found in cart. Nothing modified.")
... 
...         
>>> def get_num_items_in_cart(self):
...     return sum(item.quantity for item in self.cart_items)
... 
>>> def get_cost_of_cart(self):
...     return sum(item.price * item.quantity for item in self.cart_items)
... 
>>> def print_total(self)L
SyntaxError: expected ':'
>>> def print_total(self):
...     print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
...     total_items = self.get_num_items_in_cart()
    print(f"Number of Items: {total_items}")
    if total_items == 0:
        print("SHOPPING CART IS EMPTY")
    else:
        for item in self.cart_items:
            item.print_item_cost()
        print(f"Total: ${self.get_cost_of_cart()}")

        
def print_descriptions(self):
    print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
    print("Item Descriptions")
    for item in self.cart_items:
        item.print_item_description()

        
def print_menu(cart):
    menu = """
MENU
a - Add item to cart
r - Remove item from cart
c - Cahnge item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
"""
    choice = ""
    while choice != "q":
        print(menu)
        choice = input("Choose an option:\n").lower()

        
if choice == "a":
    print("ADD ITEM TO CART")
    name = input("Enter the items name:\n")
    description = input("Enter the item description:\n")
    price = int(input("Enter the item price:\n"))
    quantity = int(input("Enter the item quantity:\n"))
    item = ItemToPurchase(name, description, price, quantity)
    cart.add_item(item)

    
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    if choice == "a":
NameError: name 'choice' is not defined
if choice == "a":
            print("ADD ITEM TO CART")
            name = input("Enter the item name:\n")
            description = input("Enter the item description:\n")
            price = int(input("Enter the item price:\n"))
            quantity = int(input("Enter the item quantity:\n"))
            item = ItemToPurchase(name, description, price, quantity)
            cart.add_item(item)

Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    if choice == "a":
NameError: name 'choice' is not defined
choice = ""
    while choice != "q":
        print(menu)
        choice = input("Choose an option:\n").lower()

SyntaxError: multiple statements found while compiling a single statement
choice = ""
while choice != "q":
    print(menu)
    choice = input("Choose an option:\n").lower()

    
Traceback (most recent call last):
  File "<pyshell#106>", line 2, in <module>
    print(menu)
NameError: name 'menu' is not defined
def print_menu(cart):
    menu = """
MENU
a - Add itme to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
"""
    choice = ""
    while choice != "q"
    
SyntaxError: expected ':'
choice = ""
while choice != "q":
    print(menu)
    choice = input("Choose an option:\n").lower()

    
Traceback (most recent call last):
  File "<pyshell#123>", line 2, in <module>
    print(menu)
NameError: name 'menu' is not defined
