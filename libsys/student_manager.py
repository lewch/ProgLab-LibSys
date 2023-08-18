import copy

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from student import Student


class StudentManager:
    """
    A class for student manager which manages the student stored in a database.
    """

    def __init__(self, path=":memory:"):
        """
        # Connect to the database at the given path
        :param path: A file path to the database
        """
        self.engine = create_engine("sqlite:///" + path)
        # Create a table for Student instances
        Student.__table__.create(self.engine, checkfirst=True)

    def register_student(self, student):
        """
        Add a student to the table of Student instances in the library database.
        :param student: A student to be added
        :return: None
        """
        # Create a deep copy of the student so the origin will not be bound to the session
        student_copy = copy.deepcopy(student)
        with Session(self.engine) as session:
            # Add a student to the Student table
            session.add(student_copy)
            # Commit the change and update the database
            session.commit()

    def get_student(self, id):
        """
        Get a copy of a student with a given id in the database.
        :param id: the name of the student
        :return: a copy of the student stored in the database or None if not found
        """
        with Session(self.engine) as session:
            student = session.get(Student, id)
            return copy.deepcopy(student)

    def show_students(self):
        """
        Print out the Student table.
        :return: None
        """
        # Set the width of each column
        row_formatter = "{:<8} {:<30}"
        with Session(self.engine) as session:
            # Print the caption
            print("Table of students")
            # Print the header
            print(row_formatter.format("ID", "Name"))
            # Print the entities
            for student in session.query(Student):
                print(row_formatter.format(student.id, student.name))

    def clear_students(self):
        """
        Delete the entire table of students
        :return:None
        """
        # Use the drop method inherited from DeclarativeBase class to delete the table
        Student.__table__.drop(self.engine)
