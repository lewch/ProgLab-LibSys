from .context import libsys
from libsys import Student
from libsys import StudentManager
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import pytest
class TestStudentManager:
    def test_register_student(self):
        student_manager = StudentManager(":memory:")
        student = Student(id=1000, name="Tom")

        student_manager.register_student(student)

        engine = create_engine("sqlite:///:memory:")
        with Session(engine) as session:
            # Check if the student added exists in the database
            assert session.query(Student).filter(Student.id==student.id) is not None

    def test_get_student(self):
        student_manager = StudentManager(":memory:")
        source = Student(id=1000, name="Tom")
        student_manager.register_student(source)

        target = student_manager.get_student(source.id)
        assert source == target
