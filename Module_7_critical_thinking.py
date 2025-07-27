Python 3.13.5 (v3.13.5:6cb20a219a8, Jun 11 2025, 12:23:45) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
>>> course_rooms = {
...     "CSC101": "3004",
...     "CSC102": "4501",
...     "CSC103": "6755",
...     "NET110": "1244",
...     "COM241": "1411"
... }
>>> course_instructors = {
...     "CSC101": "Haynes",
...     "CSC102": "Alvarado",
...     "CSC103": "Rich",
...     "NET110": "Burke",
...     "COM241": "Lee"
... }
... 
... 
>>> course_times = {
...     "CSC101": "8:00 a.m.",
...     "CSC102": "9:00 a.m.",
...     "CSC103": "10:00 a.m.",
...     "NET110": "11:00 a.m.",
...     "COM241": "1:00 p.m."
... }
>>> course_number = input("Enter a course number (e.g., CSC101): ").strip().upper()
... 
Enter a course number (e.g., CSC101): CSC101
>>> if course_number in course_rooms:
...     print(f"\nCourse Information for {course_number}:")
...     print(f"Room Number: {course_rooms[course_number]}")
...     print(f"Instructor: {course_instructors[course_number]}")
...     print(f"Meeting Time: {course_times[course_number]}")
... 
...     

Course Information for CSC101:
Room Number: 3004
Instructor: Haynes
Meeting Time: 8:00 a.m.
