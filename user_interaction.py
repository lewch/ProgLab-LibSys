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
