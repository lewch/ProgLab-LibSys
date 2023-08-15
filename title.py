from sqlalchemy import *
from sqlalchemy.orm import *


class Base(DeclarativeBase):
    '''
    A declarative base class for the use of storing custom objects in a database.
    '''
    pass


class Title(Base):
    '''
    A class for titles where instances can be stored as entities in the 'Title' table of a SQLAlchemy database.
    '''

    # Metadata for a library database
    # Name of the table
    __tablename__ = 'Title'
    # Primary Key Column in the table with column name 'name'
    name = Column(String, primary_key=True)
    # Column in the table with column name 'publisher'
    publisher = Column(String)
    # Column in the table with column name 'genre'
    genre = Column(String)
    # Column in the table with column name 'quantity'
    quantity = Column(Integer)

    def __init__(self, name, publisher, genre, quantity):
        '''
        :param name: names of the books
        :param publisher: publisher of the books
        :param genre: genre of the books
        :param quantity: number of the books
        '''
        self.name = name
        self.publisher = publisher
        self.genre = genre
        self.quantity = quantity

    def __repr__(self):
        '''
        :return: a string representing the title
        '''
        return f'Title(name: {self.name}, ' \
               f'publisher: {self.publisher}, ' \
               f'genre: {self.genre}, ' \
               f'quantity: {self.quantity})'
