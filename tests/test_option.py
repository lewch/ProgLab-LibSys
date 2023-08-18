from .context import libsys
from libsys import Option
import pytest
class TestOption:
    def test_execute(self):
        number = 3
        option = Option(3, description = "Hello", func=lambda x: x ** 2)
        assert option.execute() == number ** 2

    def test_execute_none_func(self):
        number = 3
        option = Option(description = "Hello", func=None)
        assert option.execute() == None
