Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> class ItemToPurchase:
...     def __init__(self):
...         self.item_name = "none"
...         self.item_price = 0.0
...         self.item_quanitity = 0
...     def print_item_cost(self):
...         total_cost = self.item_price * slef.item_quantity
...         print(f"{self.item_name} {self.item_quantity} @ ${int(self.item_price)} = ${int(total_cost)}")
... 
...         
>>> item1 = ItemToPurchase()
>>> item1.item_name = "Chocolate Chips"
>>> item1.item_price = 3.0
>>> item.item_quantity = 1
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    item.item_quantity = 1
NameError: name 'item' is not defined. Did you mean: 'item1'?
>>> item1.item_quantity = 1
>>> 
>>> item2 = ItemToPurchase()
>>> item2.item_name = "Bottled Water"
>>> item2.item_price = 1.0
>>> item2.item_quantity = 10
>>> 
>>> print("Total Cost")
Total Cost
>>> item1.print_item_cost()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    item1.print_item_cost()
  File "<pyshell#8>", line 7, in print_item_cost
    total_cost = self.item_price * slef.item_quantity
NameError: name 'slef' is not defined
>>> item2.print_item_cost()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    item2.print_item_cost()
  File "<pyshell#8>", line 7, in print_item_cost
    total_cost = self.item_price * slef.item_quantity
NameError: name 'slef' is not defined
total = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
print(f"\nTotal: ${int(total)}")

Total: $13
