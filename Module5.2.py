Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> def main():
...     books = int(input("Enter the number of books you purchased this month: "))
...     if books < 0:
...         print("Invalid input.Number of book cannot be negative.")
...     elif books == 0:
...         points = 0
...     elif books == 1:
...         points = 2
...     elif books == 2:
...         points = 3
...     elif books == 4:
...         points = 5
...     elif books == 6:
...         points = 7
...     elif books == 8:
...         points = 9
...     if books >=0:
...         print(f"You have earned {points} points.")
... 
...         
>>> main()
Enter the number of books you purchased this month: 2
You have earned 3 points.
