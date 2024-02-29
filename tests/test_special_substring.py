import pytest
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from classic_exercises.special_substring import SpecialSubstring


@pytest.fixture
def input_string():
    #       0100001
    return "giraffe"


@pytest.fixture
def input_char_value():
    #       abcdefghijklmnopqrstuvwxyz
    return "01111001111111111011111111"


@pytest.fixture
def input_k():
    return 2


@pytest.fixture
def testobj(input_string, input_char_value, input_k):
    return SpecialSubstring(input_string, input_char_value, input_k)


@pytest.fixture
def expected():
    return 3


class TestSpecialSubstring:
    def test_result_type(self, testobj):
        actual = testobj.max_normal_substring_length()
        assert isinstance(actual, int)

    def test_result_values(self, testobj, expected):
        actual = testobj.max_normal_substring_length()
        assert actual == expected
    
    def test_result2_type(self, testobj):
        actual = testobj.calc2()
        assert isinstance(actual, int)

    def test_result2_values(self, testobj, expected):
        actual = testobj.calc2()
        assert actual == expected
