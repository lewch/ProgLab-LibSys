import os

from title_manager import *


class UserInteraction:
    '''
    A class that controls the user interactions with the system.
    For example, asking the user to type the information of a title,
    if they would like to add the new title to the library database.
    '''

    def __init__(self, title_manager):
        '''
        A constructor for the user_interaction class.
        :param title_manager: The title_manager which manages titles stored in the database
        '''
        self.title_manager = title_manager

    def add_title(self):
        '''
        Add a new title to the database after asking the user to input the information of the title
        :return: None
        '''
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
        self.go_back()

    def show_titles(self):
        '''
        Show all titles stored in a table.
        :return:
        '''
        # Clear the console and make an empty screen
        os.system("clear")

        # Show all the titles in the database.
        self.title_manager.show_titles()

        # Ask the user to go back to the previous screen
        self.go_back()

    def find_title(self):
        '''
        Find a title stored in the library database.
        Print out the title information if found, otherwise show an error message.
        :return: None
        '''
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

        self.go_back()

    def amend_title(self):
        '''
        Amend a title in the library database according to user's input.
        :return: None
        '''
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
            new_name = input("Please enter the new name of the books or press Enter to skip the change.\n") or None
            new_publisher = input("Please enter the new publisher of the books or press Enter to skip the change.\n") or None
            new_genre = input("Please enter the new genre of the books or press Enter to skip the change.\n") or None
            new_quantity = input("Please enter the new quantity of the books or press Enter to skip the change.\n") or None
            if new_quantity is not None:
                new_quantity = int(new_quantity)
            # Update the title in the database
            self.title_manager.update_title(title.name, new_name = new_name, new_publisher = new_publisher, new_genre=new_genre, new_quantity=new_quantity)

            # Show the information of the amended title
            new_title = self.title_manager.get_title(title.name if new_name is None else new_name)
            print("\nYour title now has been changed to:\n" + str(new_title))

        self.go_back()
    def go_back(self):
        '''
        A method that returns to the previous screen when any key is pressed.
        :return:
        '''
        print()
        key = None
        while True:
            if key is None:
                key = input("Press any key to go back.\n")
                break
