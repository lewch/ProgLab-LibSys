from title import *
class title_manager:
    '''
    A class for title manager which manages the titles store in a database.
    '''

    def __init__(self, path):
        '''
        # Connect to the database at the given path
        :param path: A file path to the database
        '''
        self.engine = create_engine("sqlite:///" + path)

    def add_title(self,title):
        '''
        Add a title to the table of Title instances in the library database.
        :param title: A title to be added
        :return: None
        '''
        # Create a table for Title instances
        Title.__table__.create(self.engine, checkfirst=True)
        with Session(self.engine) as session:
            # Add a title to the Title table
            session.add(title)
            # Commit the change and update the database
            session.commit()

    def show(self):
        '''
        Print out the Title table.
        :return: None
        '''
        # Set the width of each column
        row_formatter = "{:<30} {:<20} {:<10} {:<4}"
        with Session(self.engine) as session:
            # Print the header
            print(row_formatter.format("Name", "Publisher", "Genre", "Quantity"))
            # Print the entities
            for title in session.query(Title):
                print(row_formatter.format(title.name, title.publisher, title.genre, title.quantity))

    def clear(self):
        '''
        Delete the entire table of titles
        :return:None
        '''
        # Use the drop method inherited from DeclarativeBase class to delete the table
        Title.__table__.drop(self.engine)

