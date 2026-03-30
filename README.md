# Student Management System

## Repository link: https://github.com/yaiscoder/Sistema-de-Gestion-de-Estudiantes.git

## Description:
This program allows you to register students, consult them, and perform CRUD operations (update, delete), all through an interactive menu.

## How to run the program
1. Download or clone the repository.
2. Change the entry branch to "main".
3. Run the main file (system.py).
4. Follow the menu instructions.
   
##  What features it includes
- It's a console application.
- It runs in Python through an interpreter (for example, Python 3).
- It allows you to register students with the following variables:
  - ID: Student ID.
  - Name: Student's name.
  - Age: Student's age.
  - Program: The program the student is enrolled in.
  - Status: Whether the student is active or inactive in the program.
- It allows you to print a list of all registered students.
- Search for a student in the list by name.
- Update a student's information.
- Delete a student.
- Exit the menu.

## Examples of use
### Register a student
```
print("====== MENU ======")
print("1. Register student")
print("2. Show student list")
print("3. Search student")
print("4. Update student")
print("5. Delete student")
print("6. Exit")
------------------------------
Enter the corresponding number (1-6): 1
Enter the student name: yaila
Enter the student age: 17
Enter the student program: python
Enter the student status (active/inactive): active
------------------------------
¡The student was added correctly!
------------------------------
