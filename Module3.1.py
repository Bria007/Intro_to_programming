Python 3.13.4 (v3.13.4:8a526ec7cbe, Jun  3 2025, 21:14:54) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
>>> food = float(input("how much was the food? $"))
how much was the food? $20
>>> tip = food * 0.18
>>> tax = food * 0.07
>>> print("tip $", round(tip, 2))
tip $ 3.6
>>> print("tax: $", round(tax, 2))
tax: $ 1.4
>>> total = food + tip + tax
>>> print("total: $", round(total,2))
total: $ 25.0
