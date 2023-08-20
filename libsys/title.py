from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from base import Base


class Title(Base):
    """
    A class for titles where instances stored as entities
    in the 'Title' table of a SQLAlchemy database.
    """

    # Metadata for a library database
    # Name of the table
    # noinspection SpellCheckingInspection
    __tablename__ = 'Title'
    # Primary Key Column in the table with column name 'name'
    name = Column(String, primary_key=True)
    # Column in the table with column name 'publisher'
    publisher = Column(String)
    # Column in the table with column name 'genre'
    genre = Column(String)
    # Column in the table with column name 'quantity'
    quantity = Column(Integer)

    def __init__(self, name, publisher, genre, quantity, **kw: Integer):
        """
        :param name: names of the books.
        :param publisher: Publisher of the books.
        :param genre: Genre of the books.
        :param quantity: Amount the books.
        """
        super().__init__(**kw)
        self.name = name
        self.publisher = publisher
        self.genre = genre
        self.quantity = quantity

    def __repr__(self):
        """
        :return: a string representing the title
        """
        return f'Title(name: {self.name}, ' \
               f'publisher: {self.publisher}, ' \
               f'genre: {self.genre}, ' \
               f'quantity: {self.quantity})'
