# ------------------------------------------------------------------------------------------ #
# Title: Assignment 07
# Desc:
# Change Log: 
#   Noah Cooper, 9/8/24: First iteration. Defined Person and Student classes.
#   Noah Cooper, 9/9/24: Integrated Person and Student objects in functions used for assigning student data.
#   Noah Cooper, 9/9/24: Finalized script.
# ------------------------------------------------------------------------------------------ #

# Imports json library
import json

# Define the Data Constants
MENU: str = ("=== Course Registration Program ===\nSelect from the following \
menu:\n1: Register a Student for a Course\n2: Show Current Data\n3: Save \
Data to a File\n4: Exit program")
FILE_NAME: str = "Enrollments.json"

# Defining our necessary variables
students: list = []
menu_choice: str

class Student:

    #Assign default values
    def __init__(self, student_first_name: str = "", student_last_name: str = ""):
        self.student_first_name = student_first_name
        self.student_last_name = student_last_name

    #Check if name has no numbers and is not blank, raise exception if it does.
    @staticmethod
    def student_first_name(self, value: str):
        if value.isalpha() or value != "":
            self.student_first_name = value
        else:
            raise ValueError("The first name should not contain numbers or be blank.")
        return self.student_first_name

    # Check if name has no numbers and is not blank, raise exception if it does.
    @staticmethod
    def student_last_name(self, value: str):
        if value.isalpha() or value != "":
            self.student_last_name = value
        else:
            raise ValueError("The last name should not contain numbers or be blank.")
        return self.student_last_name


class Person:

    # Assign default values
    def __init__(self, course_name: str = ""):
        self.course_name = course_name

    # Check if name is not blank, raise exception if it does.
    @staticmethod
    def course_name(self, value: str):
        if value != "":
            self.course_name = value
        else:
            raise ValueError("The course name should not be blank.")
        return self.course_name


class FileProcessor:

    # Read data from file.
    # Json file loading automatically sorts our values based on the keys in dictionary
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except Exception as e:
            IO.output_error_messages(message="File could not be read!", error=e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    # Open the file for writing.
    # Write student_data list to file. Since we have the previous data already stored in the student_data list,
    # we can safely overwrite the pre-existing data without losing the data we have now.
    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
            print()
            print("Data saved successfully!")
            IO.output_student_courses(student_data=student_data)
        except Exception as e:
            IO.output_error_messages(message="File could not be written!", error=e)
        finally:
            if file.closed == False:
                file.close()


class IO:

    # Exception handling, referenced any time an exception occurs
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        print(message)
        if error is not None:
            print("An error has occurred!")
            print(error, error.__doc__, type(error), sep='\n')

    # Prints menu
    @staticmethod
    def output_menu(menu: str):
        print(menu)

    # Takes user input, displays error and re-displays menu if choice not recognized.
    @staticmethod
    def input_menu_choice():
        menu_option = "0"
        try:
            menu_option = input("Select an option: ")
            if menu_option not in ("1","2","3","4"):
                print("Input not recognized! Please select from the menu choices 1-4.")
            return menu_option
        except Exception as e:
            IO.output_error_messages(message="Input not recognized!", error=e)

    # Displays each entry in the student_data list. Formats data to strings, prints based on dictionary key values.
    @staticmethod
    def output_student_courses(student_data: list):
        print()
        print("Your data:")
        for entry in student_data:
            print(f'Student {entry["FirstName"]} '
                  f'{entry["LastName"]} is enrolled in {entry["CourseName"]}')
            continue
        print()

    # Take user input and append that data to the student_data list.
    # Display confirmation message.
    @staticmethod
    def input_student_data(student_data: list):
        try:
            Student.student_first_name = input("\nEnter student's first name: ")
            # if not student_first_name.isalpha():
            #     raise ValueError("Error: The first name should not contain numbers!")
            Student.student_last_name = input("Enter student's last name: ")
            # if not student_last_name.isalpha():
            #     raise ValueError("Error: The last name should not contain numbers!")
            Person.course_name = input("Enter course name: ")
            student = {"FirstName": Student.student_first_name,
                            "LastName": Student.student_last_name,
                            "CourseName": Person.course_name}
            student_data.append(student)
            print(f"Data accepted! You have registered {Student.student_first_name} {Student.student_last_name} for {Person.course_name}.")
            print("Please remember to save to file.\n")
        except Exception as e:
            IO.output_error_messages(message="Could not accept data!", error=e)
        return student_data


#Read the file using Read data function
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

while True:

    # Present the menu of choices
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break

    else:
        print("Input not recognized! Please select from the menu choices 1-4.")

print()
print("Goodbye!")