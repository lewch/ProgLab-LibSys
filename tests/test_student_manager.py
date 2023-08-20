# noinspection PyUnresolvedReferences
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from libsys import Student
from libsys import StudentManager


# @pytest.fixture(scope="module")
# def session():
#     engine = create_engine("sqlite:///:memory:")
#     Base.metadata.create_all(engine)
#     session = Session()
#     yield session
#     session.rollback()
#     session.close()
#
# @pytest.fixture(scope="module")
# def student():
#     return Student(identifier=1000, name="Tom")
#
# @pytest.fixture(scope="module")
# def student_manager():
#     return StudentManager(":memory:")
# class TestStudentManager:
#     def test_register_student(self, session, student):
#         # student_manager.register_student(student)
#         # session.query(Student).delete()
#         session.add(student)
#         session.commit()
#
#
#
#         # assert True
#         assert session.query(Student).filter(Student.identifier == student.identifier) is not None

class TestStudentManager:
    def test_register_student(self):
        student_manager = StudentManager(":memory:")
        student = Student(identifier=1000, name="Tom")

        student_manager.register_student(student)

        engine = create_engine("sqlite:///:memory:")
        with Session(engine) as session:
            # Check if the student added exists in the database
            assert session.query(Student).filter(
                Student.identifier == student.identifier) is not None

    def test_get_student(self):
        student_manager = StudentManager(":memory:")
        source = Student(identifier=1000, name="Tom")
        student_manager.register_student(source)

        target = student_manager.get_student(source.identifier)
        assert source == target
