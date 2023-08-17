import os
from user_interaction import UserInteraction
from option import *


class UserInterface:
    '''
    A class that draws user interfaces and provide them to users to interact with the system.
    '''

    def __init__(self, title_manager):
        '''
        A constructor of a user interface object
        :param title_manager: The title_manager which manages titles stored in the database
        '''
        # The user interaction instance which controls the user interactions
        self.user_interaction = UserInteraction(title_manager)

    def screen(self, header, options):
        '''
        A template for all screens that has a screen header and lists all the options which can be chosen for interactions.
        Please note that the last option is reserved for returning to the previous screen or exiting the programme.
        :param header: the name of the screen, such as "Welcome Screen"
        :param options: a list of options that will be displayed under the header
        :return: None
        '''
        while True:
            # Clear the console and make an empty screen
            os.system("clear")
            # Print the header
            print("*****" + header + "*****")

            # Print the descriptions of option in order
            for i in range(0, len(options)):
                print(str(i) + ". " + options[i].description)
            # Print the bottom line
            print("*****" + "*" * len(header) + "*****")

            # Ask the user to choose an option
            number = int(input("\nPlease enter the option number: "))
            # When the last option is selected, return to the previous screen.
            if number == len(options) - 1:
                return
            # Otherwise, execute the function according to the option
            else:
                option = options[number]
                option.execute()
                continue

    def main_screen(self):
        '''
        A welcome screen or main screen of the system.
        :return: None
        '''
        options = [Option("Admin Login", self.admin_screen),
                   Option("Exit", exit)]
        self.screen("Library Management System", options)

    def admin_screen(self):
        '''
        An admin screen for librarians to manage titles stored in the library.
        :return:
        '''
        options = [Option("Show all titles", self.user_interaction.show_titles),
                   Option("Add a title", self.user_interaction.add_title),
                   Option("Go back")]
        self.screen("Admin", options)
