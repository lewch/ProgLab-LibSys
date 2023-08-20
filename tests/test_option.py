# noinspection PyUnresolvedReferences
import pytest

from libsys import Option


class TestOption:
    def test_execute(self):
        number = 3
        option = Option(3, description="Hello", func=lambda x: x ** 2)
        assert option.execute() == number ** 2

    def test_execute_none_func(self):
        option = Option(description="Hello", func=None)
        assert option.execute() is None
