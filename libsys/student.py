from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from base import Base


class Student(Base):
    """
    A class for students where instances can be stored as entities
    in the 'Student' table of a SQLAlchemy database.
    """

    # Metadata for a library database
    # Name of the table
    # noinspection SpellCheckingInspection
    __tablename__ = 'Student'
    # Primary Key Column in the table with column name 'name'
    identifier = Column(Integer, primary_key=True)
    # Column in the table with column name 'publisher'
    name = Column(String)

    def __init__(self, identifier, name, **kw: Integer):
        """
        :param identifier: The identifier of the student.
        :param name: The name of the student.
        """
        super().__init__(**kw)
        self.identifier = identifier
        self.name = name

    def __repr__(self):
        """
        :return: a string representing the title
        """
        return f'Student(identifier: {self.identifier}, ' \
               f'name: {self.name})'

    def __eq__(self, other):
        return (isinstance(other, self.__class__)) and \
            (self.identifier == other.identifier) and \
            (self.name == other.name)
