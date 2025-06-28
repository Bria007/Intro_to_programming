Python 3.13.4 (v3.13.4:8a526ec7cbe, Jun  3 2025, 21:14:54) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
>>> current_time = int(input("What is the current time (0-23)? "))
What is the current time (0-23)? 9
>>> hours_to_wait = int(input("How many hours to wait for the alarm? "))
How many hours to wait for the alarm? 10
>>> alarm_time = (current_time + hours_to_wait) % 24
>>> print("The alarm will go off at", alarm_time, ":00 hours.")
The alarm will go off at 19 :00 hours.
