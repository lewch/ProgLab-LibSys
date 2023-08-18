import os

from report import Report
from student import Student
from title import Title


class UserInteraction:
    """
    A class that controls the user interactions with the system.
    For example, asking the user to type the information of a title,
    if they would like to add the new title to the library database.
    """

    def __init__(self, title_manager, student_manager):
        """
        A constructor for the user_interaction class.
        :param title_manager: The title manager which manages titles stored in the database
        :param student_manager: The student manager which manages students stored in the database
        """
        self.title_manager = title_manager
        self.student_manager = student_manager

    def add_title(self):
        """
        Add a new title to the database after asking the user to input the information of the title
        :return: None
        """
        # Clear the console and make an empty screen
        os.system("clear")

        # Ask the user about the information of the new title
        name = input("What is the name of the books?\n")
        publisher = input("What is the publisher of the books?\n")
        genre = input("What is the genre of the books?\n")
        quantity = int(input("What is the quantity of the books? (Please type an number.)\n"))

        # Add the new title to the database
        title = Title(name, publisher, genre, quantity)
        self.title_manager.add_title(title)

        # Ask the user to go back to the previous screen
        UserInteraction.go_back()

    def show_titles(self):
        """
        Show all titles stored in a table.
        :return:
        """
        # Clear the console and make an empty screen
        os.system("clear")

        # Show all the titles in the database.
        self.title_manager.show_titles()

        # Ask the user to go back to the previous screen
        UserInteraction.go_back()

    def find_title(self):
        """
        Find a title stored in the library database.
        Print out the title information if found, otherwise show an error message.
        :return: None
        """
        # Clear the console and make an empty screen
        os.system("clear")

        name = input("What is the book name of the title you are looking for?\n")

        # Get the title with the input book name from the database
        title = self.title_manager.get_title(name)

        # Show an error message if not found.
        if title is None:
            print("Sorry, there is no book matches the name.")
        # Print out the title information if found.
        else:
            print("Your title is found below.")
            print(title)

        UserInteraction.go_back()

    def amend_title(self):
        """
        Amend a title in the library database according to user's input.
        :return: None
        """
        # Clear the console and make an empty screen
        os.system("clear")

        # Get the title with the input book name from the database
        name = input("What is the book name of the title you want to amend?\n")
        title = self.title_manager.get_title(name)

        # Show an error message if not found.
        if title is None:
            print("Sorry, there is no book matches the name.")
        # If found, print out the old title information,
        # ask what to change and show the information of the amended title.
        else:
            # print out the old title information,
            print("\nYour title is found below:\n" + str(title))

            # Ask the user what part of the title needs to change
            print()
            # If the input is an empty string, assign None as the value
            new_name = input("Please enter the new name of the books or \
            press Enter to skip the change.\n") or None
            new_publisher = input(
                "Please enter the new publisher of the books or \
                press Enter to skip the change.\n") or None
            new_genre = input(
                "Please enter the new genre of the books or \
                press Enter to skip the change.\n") or None
            new_quantity = input(
                "Please enter the new quantity of the books or \
                press Enter to skip the change.\n") or None
            if new_quantity is not None:
                new_quantity = int(new_quantity)
            # Update the title in the database
            self.title_manager.update_title(title.name, new_name=new_name,
                                            new_publisher=new_publisher,
                                            new_genre=new_genre, new_quantity=new_quantity)

            # Show the information of the amended title
            new_title = self.title_manager.get_title(title.name if new_name is None else new_name)
            print("\nYour title now has been changed to:\n" + str(new_title))

        UserInteraction.go_back()

    def remove_title(self):
        """
        Remove a title from the library database with a book name that the user inputs.
        :return: None
        """
        os.system("clear")

        name = input("What is the book name of the title you want to remove?\n")

        # Get the title with the input book name from the database
        title = self.title_manager.get_title(name)

        # Show an error message if not found.
        if title is None:
            print("Sorry, there is no book matches the name.")
        # Remove the title if found.
        else:
            self.title_manager.remove_title(name)

            # Show the information of the removed title
            print("\nThe title below has been removed:\n" + str(title))

        UserInteraction.go_back()

    def add_student(self):
        """
        Add a new student to the database after asking the student to input their information
        :return: None
        """
        # Clear the console and make an empty screen
        os.system("clear")

        # Ask the student to type their id and name
        id = int(input("What is your student id?\n"))
        name = input("What is your name?\n")

        # Add the new student to the database
        student = Student(id, name)
        self.student_manager.register_student(student)

        # Ask the user to go back to the previous screen
        UserInteraction.go_back()

    def show_students(self):
        """
        Show all students stored in the Student table.
        :return:
        """
        # Clear the console and make an empty screen
        os.system("clear")

        # Show all the students in the database.
        self.student_manager.show_students()

        # Ask the user to go back to the previous screen
        UserInteraction.go_back()

    def borrow_book(self):
        """
        Allow a student borrow a book of an existing title.
        :return: None
        """
        # Clear the console and make an empty screen
        os.system("clear")

        # Get the student with the input id from the database
        id = int(input("What is your student id?\n"))
        student = self.student_manager.get_student(id)

        # Show an error message if the student is not found
        if student is None:
            print("Sorry, you are not registered in our library.")
        else:
            # Get the title with the input book name from the database
            book_name = input("What is the book name of the title you want to borrow?\n")
            title = self.title_manager.get_title(book_name)
            # Show an error message if the title is not found
            if title is None:
                print("Sorry, there is no book matches the name.")
            # Show an error message if the quantity of the title reaches 0
            elif title.quantity == 0:
                print("Sorry, the title you requested are all lent out.")
            else:
                # Subtract the quantity of the title,
                # one of these books is lent out.
                self.title_manager.update_title(title.name, new_quantity=title.quantity - 1)
                # Generate a report of the borrowing
                Report.borrowing(student, title)

        UserInteraction.go_back()

    @staticmethod
    def go_back():
        """
        A method that returns to the previous screen when any key is pressed.
        :return:
        """
        print()
        key = None
        while True:
            if key is None:
                key = input("Press any key to go back.\n")
                break
