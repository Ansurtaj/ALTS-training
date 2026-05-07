import os

filename = "students.txt"

# Add Student Record
def add_student():
    file = open(filename, "a")

    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    marks = input("Enter Marks: ")

    record = roll + "," + name + "," + marks + "\n"
    file.write(record)

    file.close()

    print("Student Record Added Successfully!\n")


# Display All Records
def display_students():
    try:
        file = open(filename, "r")

        data = file.readlines()

        if len(data) == 0:
            print("No Records Found.\n")
        else:
            print("\nStudent Records")
            print("--------------------------")

            for line in data:
                roll, name, marks = line.strip().split(",")
                print("Roll No:", roll)
                print("Name    :", name)
                print("Marks   :", marks)
                print("--------------------------")

        file.close()

    except FileNotFoundError:
        print("File does not exist.\n")


# Search Student
def search_student():
    roll_search = input("Enter Roll Number to Search: ")

    found = False

    try:
        file = open(filename, "r")

        for line in file:
            roll, name, marks = line.strip().split(",")

            if roll == roll_search:
                print("\nRecord Found")
                print("Roll No:", roll)
                print("Name   :", name)
                print("Marks  :", marks)
                found = True
                break

        file.close()

        if not found:
            print("Record Not Found.\n")

    except FileNotFoundError:
        print("File does not exist.\n")


# Modify Student Record
def modify_student():
    roll_modify = input("Enter Roll Number to Modify: ")

    found = False
    new_records = []

    try:
        file = open(filename, "r")

        for line in file:
            roll, name, marks = line.strip().split(",")

            if roll == roll_modify:
                print("Record Found. Enter New Details")

                new_name = input("Enter New Name: ")
                new_marks = input("Enter New Marks: ")

                new_records.append(roll + "," + new_name + "," + new_marks + "\n")
                found = True

            else:
                new_records.append(line)

        file.close()

        file = open(filename, "w")
        file.writelines(new_records)
        file.close()

        if found:
            print("Record Modified Successfully!\n")
        else:
            print("Record Not Found.\n")

    except FileNotFoundError:
        print("File does not exist.\n")


# Delete Student Record
def delete_student():
    roll_delete = input("Enter Roll Number to Delete: ")

    found = False
    new_records = []

    try:
        file = open(filename, "r")

        for line in file:
            roll, name, marks = line.strip().split(",")

            if roll == roll_delete:
                found = True
                continue

            new_records.append(line)

        file.close()

        file = open(filename, "w")
        file.writelines(new_records)
        file.close()

        if found:
            print("Record Deleted Successfully!\n")
        else:
            print("Record Not Found.\n")

    except FileNotFoundError:
        print("File does not exist.\n")


# Main Menu
while True:

    print("\n===== STUDENT RECORD MANAGEMENT =====")
    print("1. Add Student Record")
    print("2. Display Student Records")
    print("3. Search Student Record")
    print("4. Modify Student Record")
    print("5. Delete Student Record")
    print("6. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        display_students()

    elif choice == 3:
        search_student()

    elif choice == 4:
        modify_student()

    elif choice == 5:
        delete_student()

    elif choice == 6:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice! Please Try Again.")