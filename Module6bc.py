Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> def print_menu(cart):
...     menu = """
... MENU
... a - Add item to cart
... r - Remove item from cart
... c - Change item quantity
... i - Output items' descriptions
... o - Output shopping cart
... q - Quit
... """
...     choice = ""
...     while choice != "q":
...         print(menu)
...         choice = input("Choose an option:\n").lower()
...         if choice == "a":
...             print("ADD ITEM TO CART")
...             name = input("Enter the item name:\n")
...             description = input("Enter the item description:\n")
...             price = int(input("Enter the item quantity:\n"))
...             quantity = int(input("Enter the item quantity:\n"))
...             item = ItemToPurchase(name, description, price, quantity)
...             cart.add_item(item)
...         elif choice == "r":
...             print("REMOVE ITEM FROM CART")
...             name = input("Enter name of item to remove:\n")
...             cart.remove_item(name)
...         elif choice == "c":
...             print("CHANGE ITEM QUANTITY")
...             name = input("Enter the item name:\n")
...             quantity = int(input("Enter the new quantity:\n"))
...             item = ItemToPurchase(name=name, quantity=quantity)
...             cart.modify_item(item)
...         elif choice == "i":
...             print("OUTPUT ITEMS' DESCRIPTIONS")
...             cart.print_descriptions()
...         elif choice == "o":
...             print("OUTPUT SHOPPING CART")
            cart.print_total()
        elif choice == "q":
            break
        else: print("Invalid option, please choose again.")

        
def main():
    name = input("Enter customer's name:\n")
    date = input("Enter today's date:\n")
    print()
    print(f"Customer name: {name}")
    print(f"Today's date: {date}")
    cart = ShoppingCart(name, date)
    print_menu(cart)

    
main()
Enter customer's name:
chebria
Enter today's date:
july 20th

Customer name: chebria
Today's date: july 20th
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    main()
  File "<pyshell#50>", line 7, in main
    cart = ShoppingCart(name, date)
NameError: name 'ShoppingCart' is not defined

main ()
Enter customer's name:
John Doe
Enter today's date:
February 1, 2020

Customer name: John Doe
Today's date: February 1, 2020
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    main ()
  File "<pyshell#50>", line 7, in main
    cart = ShoppingCart(name, date)
NameError: name 'ShoppingCart' is not defined
def print_total(self):
    print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
    total_items = self.get_num_items_in_cart()
    print(f"Number of Items: {total_items}")
    if total_items == 0:
        print("Shopping Cart is Empty")
    else:
        for item in self.cart_items:
            print(f"{item.name} {item.quantity} @ ${item.price} = ${item.quantity* item.price}")
            print(f"Total: ${self.get_cost_of_cart()}")

            
print_total()
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    print_total()
TypeError: print_total() missing 1 required positional argument: 'self'
