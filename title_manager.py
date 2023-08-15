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
    def update_title(self, name, new_name = None, new_publisher = None, new_genre = None, new_quantity = None):
        '''
        Update a title with a given book name in the database with given values.
        :param name: the book name of the title
        :param new_name: the new book name of the title
        :param new_publisher: the new publisher of the title
        :param new_genre: the new genre of the title
        :param new_quantity: the new quantity of the title
        :return: None
        '''

        # A dictionary that indicates what values need to be changed
        update_dict = {"name": new_name, "publisher": new_publisher, "genre": new_genre, "quantity": new_quantity}
        # Filter out those items which value is the default - None, as they are not assigned to be changed
        update_dict = {k: v for k, v in update_dict.items() if v is not None}

        with Session(self.engine) as session:
            # Select the title entry with the name passed into this method,
            # and update the entry with the new values
            session.query(Title).filter(Title.name == name).update(update_dict)
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

