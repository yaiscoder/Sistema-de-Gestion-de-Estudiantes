# These are the functions located in another file.
from functions import *

# Variables are defined for the operation of the program.
list_student = []
option = 0

# A "while" loop is used to validate the chosen option according to the action to be performed in the menu
while option != 6:

    # The "if", "elif", and "else" conditions are used for each menu action.
    # # In addition, the corresponding functions are called for each menu action.

    show_menu()
    try: # It is validated that what the user enters is an int
        option = int(input("Enter the corresponding number (1-6): "))

    except ValueError:
        print("-"*30)
        print("¡Error! The entered value is invalid")
        print("-"*30)

    if option == 1: # Register a new student
        register_student(list_student)

    elif option == 2: # show all the student
        show_student_list(list_student)

    elif option == 3: #search a student with there "name"
        print("-"*30)
        search = input("Enter the student you want to search: ").strip().lower()
        print("-"*30)
        s = search_student(list_student, search)
        if s:
            print("-"*30)
            print(f"The student is: {s}")
            print("-"*30)
        else:
            print("-"*30)
            print("The student you are looking for is not registered")
            print("-"*30)
    
    elif option == 4: # update a student's information
        print("-"*30)
        search = input("Enter the name of the student to be updated: ")
        print("-"*30)
        if update_student(list_student, search):
            print("-"*30)
            print("The information was updated correctly")
            print("-"*30)
        else:
            print("-"*30)
            print("The information was NOT updated correctly")
            print("-"*30)
    
    elif option == 5: # Delete a student
        print("-"*30)
        search = input("Enter the name of the student to be deleted: ")
        print("-"*30)
        if delete_student (list_student, search):
            print("-"*30)
            print("The student was successfully removed")
            print("-"*30)
        else:
            print("-"*30)
            print("The student was NOT eliminated")
            print("-"*30) 

    
    elif option == 6: # exit the program
        print("-"*30)
        print("Come back soon!")
        print("-"*30)
        break

else: # validates that the number entered is in the range (1-6)
    print("-"*30)
    print("invalid option!")
    print("-"*30)
