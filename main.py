from user_interface import *
from title_manager import *
def main():
    # A title manager to manage titles in the database.
    title_manager = TitleManager(":memory:")

    # An instance of user interface that provides a command line interface.
    user_interface = UserInterface(title_manager)
    # Load the main screen
    user_interface.main_screen()

if __name__ == "__main__":
    main()