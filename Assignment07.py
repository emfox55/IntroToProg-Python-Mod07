# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using class and objects.
# Change Log: (Who, When, What)
#   EFox,11/19/2024,Created Assignment 06 Script
#   EFox,11/26/2024,
#       - Converted dictionary rows to student class objects.
#       - Added properties and private attributes
#       - Added inheritance
# ------------------------------------------------------------------------------------------ #
import json


# Data --------------------------------------- #
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a student for a course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

menu_choice: str  # hold the choice made by the user.
students: list = []  # a table of student data


class Person:
    """
    A class representing person data.

    Properties:
        first_name (str): The student's first name.
        last_name (str): The student's last name.

    ChangeLog:
        EFox,11/26/2024,Created the class.
    """

    def __init__(self, first_name: str = '', last_name: str = ''):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self.__first_name.title()  # formatting code

    @first_name.setter
    def first_name(self, value: str):
        if value.isalpha() or value == "":  # is character or empty string
            self.__first_name = value
        else:
            raise ValueError("The last name should not contain numbers.")

    @property
    def last_name(self):
        return self.__last_name.title()  # formatting code

    @last_name.setter
    def last_name(self, value: str):
        if value.isalpha() or value == "":  # is character or empty string
            self.__last_name = value
        else:
            raise ValueError("The last name should not contain numbers.")

    def __str__(self):
        return f'{self.first_name},{self.last_name}'


class Student(Person):
    """
    A class representing student data.

    Properties:
        first_name (str): The student's first name.
        last_name (str): The student's last name.
        course_name (str): The registered course name of the student.

    ChangeLog: (Who, When, What)
    EFox,11/26/2024,Created Class
    """

    def __init__(self, first_name: str = '', last_name: str = '', course_name: str = ''):
        super().__init__(first_name=first_name, last_name=last_name)
        self.course_name = course_name
        
    @property
    def course_name(self):
        return self.__course_name

    @course_name.setter
    def course_name(self, value: str):
        self.__course_name =  value

    def __str__(self):
        return f'{self.first_name},{self.last_name},{self.course_name}'


# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with JSON files

    ChangeLog: (Who, When, What)
    EFox,11/19/2024,Created class
    EFox,11/26/2024,Converted code to use student objects instead of dictionaries
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        A function to read the data from a specified JSON file, and into list.

        ChangeLog: (Who, When, What)
        EFox,11/19/2024,Created Function
        EFox,11/26/2024,Converted list of dictionaries to list of student objects

        :param file_name: string data with name of file to read from
        :param student_data: list of dictionary rows to be filled with file data

        :return: list
        """

        try:
            file = open(file_name, "r")

            list_of_dictionary_data = json.load(file)  # the load function returns a list of dictionary rows.
            for student in list_of_dictionary_data:  # Convert the list of dictionary rows into Student objects
                student_object: Student = Student(first_name=student["FirstName"],
                                                  last_name= student["LastName"],
                                                  course_name=student["CourseName"])
                student_data.append(student_object)

            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages(message = 'File must exist before running this script!', error = e)
        except Exception as e:
            IO.output_error_messages(message = 'There was a non-specific error', error = e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data:list):
        """
        A function to write the data to a specified JSON file from a list

        ChangeLog: (Who, When, What)
        EFox,11/19/2024,Created Function
        EFox,11/26/2024,Converted code to use student objects instead of dictionaries

        :param file_name: string data with name of file to write to
        :param student_data: list of dictionary rows to be writen to the file

        :return: None
        """
        try:
            list_of_dictionary_data: list = []
            for student in student_data:  # Convert List of Student objects to list of dictionary rows.
                student_json: dict \
                    = {"FirstName": student.first_name, "LastName": student.last_name, "CourseName": student.course_name}
                list_of_dictionary_data.append(student_json)

            file = open(FILE_NAME,'w')
            json.dump(list_of_dictionary_data,file)
            file.close()
        except TypeError as e:
            IO.output_error_messages(message = 'Are the file contents in a valid JSON format?', error= e)
        except Exception as e:
            IO.output_error_messages(message = 'There was a non-specific error', error = e)
        finally:
            if file.closed == False:
                file.close()

        print('The following data was saved to file!')
        IO.output_student_courses(student_data = student_data)


# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that regulate data shown
    to and collected from the user

    ChangeLog: (Who,When,What)
    EFox,11/19/2024,Created Class
    EFox,11/26/2024,Converted methods to use student objects instead of dictionaries
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays a custom error messages to the user

         ChangeLog: (Who, When, What)
         EFox,11/19/2024,Created Function

         :param message: string with message data to display
         :param error: Exception object with technical message to display

         :return: None
         """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays a menu of choices to the user

        ChangeLog: (Who, When, What)
        EFox,11/19/2024,Created Function

        :return: None
        """
        print()
        print(MENU)
        print()

    @staticmethod
    def input_menu_choice(menu: str) -> str:
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        EFox,11/19/2024,Created function

        :return: string with the user's choice
        """
        menu_choice = input('What would you like to do: ')
        while menu_choice not in ['1','2','3','4']:
            IO.output_error_messages('Please enter a number between 1 and 4.')
            menu_choice = input("What would you like to do: ")
        return menu_choice

    @staticmethod
    def output_student_courses(student_data: list):
        """ This function displays the student data to the user

        ChangeLog: (Who, When, What)
        EFox,11/19/2024,Created function
        EFox,11/26/2024,Converted code to use student objects instead of dictionaries

        :param student_data: list of student object data to be displayed

        :return: None
        """
        print("-" * 50)
        for student in student_data:
            print(f'Student {student.first_name} '
                  f'{student.last_name} is enrolled in {student.course_name}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets the first name, last name, and course name from the user

        ChangeLog: (Who, When, What)
        EFox,11/19/2024,Created Function
        EFox,11/26/2024,Converted code to use student objects instead of dictionaries

        :param student_data: list of dictionary rows to be filled with input data

        :return: list
        """

        try:
            student = Student()
            student.first_name = input('Enter the student\'s first name ')
            student.last_name = input('Enter the student\'s last name ')
            student.course_name = input('Enter the name of the course ')
            student_data.append(student)
            print(f"You have registered {student.first_name} {student.last_name} for {student.course_name}.")
        except ValueError as e:
            IO.output_error_messages(message = 'The value is not valid.', error = e)
        except Exception as e:
            IO.output_error_messages(message = 'Error: There was a problem with your entered data.', error = e)
# End of class and function definitions


# When the program starts, read the file data into a list of lists (table)
students = FileProcessor.read_data_from_file(file_name = FILE_NAME, student_data = students)

# Present and Process the data
while True:
    # Present the menu of choices
    print(MENU)
    # Store user menu choice
    menu_choice = IO.input_menu_choice(menu = MENU)

    if menu_choice == '1':
        # Input user data
        IO.input_student_data(student_data = students)
        continue

    elif menu_choice == '2':
        # Present the current data
        IO.output_student_courses(student_data = students)
        continue

    elif menu_choice == '3':
        # Save the data to a file
        FileProcessor.write_data_to_file(file_name = FILE_NAME, student_data = students)
        continue

    elif menu_choice == '4':
        # Stop the loop
        break

print("Program Ended")
