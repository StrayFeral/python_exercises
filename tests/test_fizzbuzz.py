import pytest
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from classic_exercises.fizzbuzz import FizzBuzzer


@pytest.fixture
def testobj():
    return FizzBuzzer()


@pytest.fixture
def expected():
    return [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz",
        "16",
        "17",
        "Fizz",
        "19",
        "Buzz",
    ]


class TestFizzBuzzer:
    def test_solution1_type(self, testobj):
        actual = testobj.solution1()
        assert isinstance(actual, list)

    def test_solution1_len(self, testobj):
        actual = testobj.solution1()
        assert len(actual) == testobj.fbrange

    def test_solution1_values(self, testobj, expected):
        actual = testobj.solution1()
        assert actual == expected

    def test_solution2_type(self, testobj):
        actual = testobj.solution2()
        assert isinstance(actual, list)

    def test_solution2_len(self, testobj):
        actual = testobj.solution2()
        assert len(actual) == testobj.fbrange

    def test_solution2_values(self, testobj, expected):
        actual = testobj.solution2()
        assert actual == expected
