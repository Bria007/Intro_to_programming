Python 3.13.5 (v3.13.5:6cb20a219a8, Jun 11 2025, 12:23:45) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
>>> class ItemToPurchase:
...     def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_description="none"):
...         self.item_name = item_name
...         self.item_price = item_price
...         self.item_quantity = item_quantity
...         self.item_description = item_description
...     def print_item_cost(self):
...         total_cost = self.item_price * self.item_quantity
...         print(f"{self.item_name} {self.item_quantity} @ ${int(self.item_price)} = ${int(total_cost)}")
...     def print_item_description(self):
...         print(f"{self.item_name}: {self.item_description}")
... 
...         
>>> print("Item 1")
Item 1
>>> name1 = input("Enter the item name:\n")
Enter the item name:
Chocolate Chips
>>> price1 = float(input("Enter the item price:\n"))
Enter the item price:
3
>>> quantity1 = int(input("Enter the item quantity:\n"))
Enter the item quantity:
1
>>> item1 = ItemToPurchase(name1, price1, quantity1)
>>> print("\nItem 2")

Item 2
>>> name2 = input("Enter the item name:\n")
Enter the item name:
Bottled Water
>>> price2 = float(input("Enter the item price:\n"))
Enter the item price:
1
>>> quantity2 = int(input("Enter the item quantity:\n"))
Enter the item quantity:
10
>>> item2 = ItemToPurchase(name2, price2, quantity2)
>>> print("\nTOTAL COST")

TOTAL COST
>>> item1.print_item_cost()
Chocolate Chips 1 @ $3 = $3
>>> item2.print_item_cost()
Bottled Water 10 @ $1 = $10
>>> total = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
>>> print(f"Total: ${int(total)}\n")
Total: $13

>>> class ShoppingCart:
...     def __init__(self, customer_name="none", current_date="January 1, 2020"):
...         self.customer_name = customer_name
...         self.current_date = current_date
...         self.cart_items = []
...     def add_item(self, item):
...         self.cart_items.append(item)
...     def remove_item(self, item_name)
...     
SyntaxError: expected ':'
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
          self.customer_name = customer_name
           self.current_date = current_date
           
SyntaxError: unexpected indent
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
    def add_item(self, item):
        self.cart_items.append(item)
    def remove_item(self, item_name):
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing removed.")
    def modify_item(self, modified_item):
        found = False
        for item in self.cart_items:
            if item.item_name == modified_item.item_name:
                if modified_item.item_quantity != 0:
                    item.item_quantity = modified_item.item_quantity
                if modified_item.item_price != 0:
                    item.item_price = modified_item.item_price
                if modified_item.item_description != "none":
                    item.item_description = modified_item.item_description
                found = True
                break
            if not found:
                print("Item not found in cart. Nothing modified.")
    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)
    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
              item.print_item_cost()
            print(f"Total: ${int(self.get_cost_of_cart())}")
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()

            
def print_menu(cart):
    menu = (
        "\nMENU\n"
        "a - Add item to cart\n"
        "r - Remove item from cart\n"
        "c - Change item quantity\n"
        "i - Output items' descriptions\n"
        "o - Output shopping cart\n"
        "q - Quit\n"
        )
    while True:
        print(menu)
        choice = input("Choose an option:\n").lower()
        if choice == "a":
            print("ADD ITEM TO CART")
            name = input("Enter the item name:\n")
            description = input("Enter the item description:\n")
            price = float(input("Enter the item price:\n"))
            quantity = int(input("Enter the item quantity:\n"))
            item = ItemToPurchase(name, price, quantity, description)
            cart.add_item(item)
        elif choice == "r":
            print("REMOVE ITEM FROM CART")
            name = input("Enter name of item to remove:\n")
            cart.remove_item(name)
        elif choice == "c":
            print("CHANGE ITEM QUANTITY")
            name = input("Enter the item name:\n")
            quantity = int(input("Enter the new quantity:\n"))
            item = ItemToPurchase(item_name=name, item_quantity=quantity)
            cart.modify_item(item)
        elif choice == "i":
            print("OUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()
        elif choice == "o":
            print("OUTPUT SHOPPING CART")
            cart.print_total()
        elif choice == "q":
            break
        else:
            continue

        
def main()
SyntaxError: expected ':'
def main():
 print("Enter customer's name:")
 customer_name = input()
 print("Enter today's date:")
 current_date = input()
 print(f"\nCustomer name: {customer_name}")
 print(f"Today's date: {current_date}")
 cart = ShoppingCart(customer_name, current_date)
 print_menu(cart)

 
if __name__ == "__main__":
    main()

    
Enter customer's name:
John
Enter today's date:
August 3, 2025

Customer name: John
Today's date: August 3, 2025

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit

Choose an option:
a
ADD ITEM TO CART
Enter the item name:
Chocolate Chips
Enter the item description:
cookies
Enter the item price:
3
Enter the item quantity:
5

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit

Choose an option:
q
