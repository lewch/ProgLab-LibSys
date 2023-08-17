from sqlalchemy import *

from base import Base


class Student(Base):
    """
    A class for students where instances can be stored as entities in the 'Student' table of a SQLAlchemy database.
    """

    # Metadata for a library database
    # Name of the table
    __tablename__ = 'Student'
    # Primary Key Column in the table with column name 'name'
    id = Column(Integer, primary_key=True)
    # Column in the table with column name 'publisher'
    name = Column(String)

    def __init__(self, id, name, **kw: Any):
        """
        :param id: identification number of the student
        :param name: name of the student
        """
        super().__init__(**kw)
        self.id = id
        self.name = name

    def __repr__(self):
        """
        :return: a string representing the title
        """
        return f'Student(id: {self.id}, ' \
               f'name: {self.name})'
