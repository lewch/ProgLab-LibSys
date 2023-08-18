import os

from option import Option
from user_interaction import UserInteraction


class UserInterface:
    """
    A class that draws user interfaces and provide them to users to interact with the system.
    """

    def __init__(self, title_manager, student_manager):
        """
        A constructor of a user interface object
        :param title_manager: The title manager which manages titles stored in the database
        :param student_manager: The student manager which manages students stored in the database
        """
        # The user interaction instance which controls the user interactions
        self.user_interaction = UserInteraction(title_manager, student_manager)

    @staticmethod
    def screen(header, options):
        """
        A template for all screens that has a screen header and lists all the options
        which can be chosen for interactions. Please note that the last option is
        reserved for returning to the previous screen or exiting
        the programme.
        :param header: the name of the screen, such as "Welcome Screen"
        :param options: a list of options that will be displayed under the header
        :return: None
        """
        while True:
            # Clear the console and make an empty screen
            os.system("clear")
            # Print the header
            print("*****" + header + "*****")

            # Print the descriptions of option in order
            for i, option in enumerate(options):
                print(str(i) + ". " + option.description)
            # Print the bottom line
            print("*****" + "*" * len(header) + "*****")

            # Ask the user to choose an option
            number = int(input("\nPlease enter the option number: "))
            # When the last option is selected, return to the previous screen.
            if number == len(options) - 1:
                return
            # Otherwise, execute the function according to the option
            option = options[number]
            option.execute()
            continue

    def main_screen(self):
        """
        A welcome screen or main screen of the system.
        :return: None
        """
        options = [Option(description="Admin Login", \
                          func=self.admin_screen),
                   Option(description="Student Login", \
                          func=self.student_screen),
                   Option(description="Exit", \
                          func=exit)]
        UserInterface.screen("Library Management System", options)

    def admin_screen(self):
        """
        An admin screen for librarians to manage titles stored in the library.
        :return: None
        """
        options = [Option(description="Show all titles", \
                          func=self.user_interaction.show_titles),
                   Option(description="Add a title", \
                          func=self.user_interaction.add_title),
                   Option(description="Find a title", \
                          func=self.user_interaction.find_title),
                   Option(description="Amend a title", \
                          func=self.user_interaction.amend_title),
                   Option(description="Remove a title", \
                          func=self.user_interaction.remove_title),
                   Option(description="Go back")]
        UserInterface.screen("Admin", options)

    def student_screen(self):
        """
        A student screen for students to manage their information stored in the library.
        :return: None
        """
        options = [Option(description="Registration", \
                          func=self.user_interaction.add_student),
                   Option(description="Show all students", \
                          func=self.user_interaction.show_students),
                   Option(description="Show all titles", \
                          func=self.user_interaction.show_titles),
                   Option(description="Borrow a book", \
                          func=self.user_interaction.borrow_book),
                   Option(description="Go back")]
        UserInterface.screen("Student", options)
