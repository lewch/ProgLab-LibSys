from student_manager import StudentManager
from title_manager import TitleManager
from user_interface import UserInterface


def main():
    """
    Run the main function of the System.
    """
    # A title manager to manage titles in the database.
    title_manager = TitleManager("library.db")
    # A student manager to manage students in the database.
    student_manager = StudentManager("library.db")

    # An instance of user interface that provides a command line interface.
    user_interface = UserInterface(title_manager, student_manager)
    # Load the main screen
    user_interface.main_screen()


if __name__ == "__main__":
    main()
