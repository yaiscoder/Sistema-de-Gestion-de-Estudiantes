# import random to generate the random "id"
import random

# Show option from menu

def show_menu ():
    print("-"*30)
    print("====== MENU ======")
    print("-"*30)
    print("1. Register student")
    print("2. Show student list")
    print("3. Search student")
    print("4. Update student")
    print("5. Delete student")
    print("6. Exit")
    print("-"*30)

# Register a new student

def register_student(list_student):
    """
    registers a student and adds them to the list.

    parameter:
    List_student (list): list of student
    id (int): Student id
    name (str): Student name
    age (int): Student age
    program (str): Student program
    status (str): Student status

    Return:
    None
    """

    id = random.randint(0, 9999)
    name = input("Enter the student name: ")
    try:
        age = int(input("Enter the student age: "))
        if age <= 0:
            print("-"*30)
            print("¡Error! The age can't be negative")
            print("-"*30)
            confirm = input("Do you want to try again? (yes/no): ").strip().lower()
            print("-"*30)
            if confirm == "yes":
                age = int(input("Enter the student age: ")) 
            else:
                print("-"*30)
                print("¡You can't register the student!")
                print("-"*30)
        elif age > 0:
            program = input("Enter the student program: ")
            status = input("Enter the student status (active/inactive): ")
            student = {
                'id': id,
                'name': name,
                'age': age,
                'program': program,
                'status': status
            }
            list_student.append(student)
            print("-"*30)
            print("¡The student was added correctly!")
            print("-"*30)
        
                
    except ValueError:
        print("-"*30)
        print("¡Error! The entered value is invalid")
        print("-"*30)

# Show all students that are register

def show_student_list(list_student):
    """
    displays the complete list of registered students.

    parameter:
    List_student (list): list of student

    Return:
    None
    """
    if len(list_student) == 0:
        print("-"*30)
        print("The list is empty")
        print("-"*30)
    else: 
        for i in list_student:
            print("-"*30)
            print(f"ID: {i['id']} | Name: {i['name']} | Age: {i['age']} | Program: {i['program']} | Status: {i['status']}")
            print("-"*30)

# Search a student with there name

def search_student(list_student, search):
    """
    search for a student by name

    parameter:
    List_student (list): list of student
    search (str): Name of student to look for 

    Return:
    dict: if find the student
    None: if not find the student
    """
    
    if len(list_student) == 0:
        print("-"*30)
        print("The list is empty")
        print("-"*30)
    else:
        for i in list_student:
            if i['name'] == search:
                return i


# Update the student information

def update_student(list_student, search):

    """
    update specific student information

    parameter:
    List_student (list): list of student
    search (str): Name of student to look for 
    new_age (int): A new age for the student
    new_program (str): A new program for the student
    new_status (str): A new status for the student

    Return:
    bool: True, if the student information is update
    None: False, if the student information isn't update
    """
    
    if len(list_student) == 0:
        print("-"*30)
        print("The list is empty")
        print("-"*30)
    else: 
        option = 0
        student = search_student(list_student, search)
        print("-"*30)
        print("What do you want to change: ")
        print("1. Age")
        print("2. Program")
        print("3. Status")
        print("-"*30)
        try:
            option = int(input("Enter the corresponding number (1-3): "))
        except ValueError:
            print("-"*30)
            print("¡Error! The entered value is invalid")
            print("-"*30)
        if student:
            if option == 1: 
                try:
                    new_age = int(input("Enter the student new age: "))
                    if new_age <= 0:
                        print("-"*30)
                        print("¡Error! The age can't be negative")
                        print("-"*30)
                        confirm = input("Do you want to try again? (yes/no): ").strip().lower()
                        print("-"*30)
                        if confirm == "yes":
                            new_age = int(input("Enter the student age: ")) 
                        else:
                            print("-"*30)
                            print("¡You can't register the student!")
                            print("-"*30)
                    elif new_age > 0:
                        student['age'] = new_age
                except ValueError:
                    print("-"*30)
                    print("¡Error! The entered value is invalid")
                    print("-"*30)
            elif option == 2:
                new_program = input("Enter the student program: ")
                if new_program:
                    student['program'] = new_program
            elif option == 3:
                new_status = input("Enter the student status (active/inactive): ")
                if new_status:
                    student['status'] = new_status
            return True
        return False
    
# Remove student from record

def delete_student(list_student, search):
    
    """
    Delete specific student 

    parameter:
    List_student (list): list of student
    search (str): Name of student to look for 
    
    Return:
    bool: True, if the student is delete
    None: False, if the student isn't delete
    """

    if len(list_student) == 0:
        print("-"*30)
        print("The list is empty")
        print("-"*30)
    else: 
        d = search_student (list_student, search)
        if d:
            list_student.remove(d)
            return True
        return False