# ------------------------------------------------------------------------------------------ #
# Title: Assignment 05
# Desc: Demonstrates using dictionaries, files, and exception handling
# Change Log: 
#   Noah Cooper, 8/25/24: First iteration, based on assignment 4.
#   Noah Cooper, 8/27/24: Attempting to clean up previous systems from assignment 4.
#   Noah Cooper, 8/28/24: Adjusted script in attempt to further clean up previous systems.
#   Noah Cooper, 8/30/24: Implemented dictionary writing.
#   Noah Cooper, 8/31/24: Implemented exception handling.
#   Noah Cooper, 9/1/24: Finalized script.
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
MENU = str ("=== Course Registration Program ===\nSelect from the following \
menu:\n1: Register a Student for a Course\n2: Show Current Data\n3: Save \
Data to a File\n4: Exit program")
FILE_NAME: str = "Enrollments.csv"

# Define the Data Variables
student_first_name: str = ''
student_last_name: str = ''
course_name: str = ''
csv_data: str = ''
file_obj = None
menu_choice: str = ''
student_data: dict = {}
students: list = []
file_data: list = []

# Create the file if it is not present, read data and append to students dictionary.
try:
    file_obj: object = open(FILE_NAME, "a")
    file_obj.close()
    file = open(FILE_NAME, "r")
    for row in file.readlines():
        file_data: list = row.split(',')
        student_data = {"FirstName": file_data[0], "LastName":file_data[1], "Class":file_data[2].strip()}
        students.append(student_data)
    file.close()
except Exception as e:
    print("Error: Unable to create and/or read file")
    print("-- Technical Error Message -- ")
    print(e.__doc__)
    print(e.__str__())
# If file is already present, this append will do nothing.
# Read the file. For each row in the file we read, split all entries with a "," seperator.
# Assign proper keys and append onto students dictionary.
# Provide exception handling and display error if cannot read or write to file.

# Present the menu of choices
while True:
    print(MENU)
    menu_choice = input("Select an option: ")

# Input user data
    if menu_choice == "1":
        try:
            student_first_name = input("\nEnter student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("Error: The first name should not contain numbers!")
            student_last_name = input("Enter student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("Error: The last name should not contain numbers!")
            course_name = input("Enter course name: ")
            student_data = {"FirstName": student_first_name, "LastName": student_last_name, "Class": course_name}
            students.append(student_data)
            print(f"Data accepted! You have registered {student_first_name} {student_last_name} for {course_name}.")
            print("Please remember to save to file.\n")
        except Exception as e:
            print("Error: Unable to process data.")
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        continue
# Take user input and save to student_data dictionary. Append that data to the students dictionary we defined earlier.
# Format and display data for the user.
# Provide exception handling and display error if cannot recognize data.

# Present the current data
    elif menu_choice == "2":
        for student in students:
            print("Your data:")
            print(f'Student {student["FirstName"]} ' f'{student["LastName"]} is enrolled in {student["Class"]}')
        continue
# Display each row in students dictionary. Format to string.

# Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            for student in students:
                csv_data = f'{student["FirstName"]},{student["LastName"]},{student["Class"]}\n'
                file.write(csv_data)
            file.close()
            print("\nData saved to Enrollments.csv!")
            print("Your data:")
            for student in students:
                print(f'Student {student["FirstName"]} 'f'{student["LastName"]} is enrolled in {student["Class"]}')
        except Exception as e:
            print("Error: Unable to write data .")
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        continue
# Open the file for writing. Since we have the previous data already stored in the students dictionary,
# we can safely overwrite the pre-existing data without losing the data we have now.
# For each row in students, set to csv_data, and write csv_data to file.
# Re-print data for user.
# Provide exception handling and display error if cannot write data to file.

# Stop the loop
    elif menu_choice == "4":
        print("\nGoodbye!")
        break

    else:
        print("Input not recognized! Please select from the menu choices 1-4.")