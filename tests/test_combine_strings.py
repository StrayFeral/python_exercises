import pytest
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from classic_exercises.combine_strings import StringCombinator


@pytest.fixture
def input1():
    return "abcde"


@pytest.fixture
def input2():
    return "ABC"


@pytest.fixture
def testobj(input1, input2):
    return StringCombinator(input1, input2)


@pytest.fixture
def expected():
    return "aAbBcCde"


class TestStringCombinator:
    def test_result_type(self, testobj):
        actual = testobj.combine()
        assert isinstance(actual, str)

    def test_result_values(self, testobj, expected):
        actual = testobj.combine()
        assert actual == expected
