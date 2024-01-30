import pytest
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from classic_exercises.count_unique import UniqueCounter


@pytest.fixture
def input_list():
    return [1, 3, 21, 3, 45, 3, "meh", "blah", 21, 9, 3]


@pytest.fixture
def testobj():
    return UniqueCounter()


@pytest.fixture
def expected():
    return 7


class TestUniqueCounter:
    def test_solution1(self, input_list, testobj, expected):
        assert testobj.solution1(input_list) == expected

    def test_solution2(self, input_list, testobj, expected):
        assert testobj.solution2(input_list) == expected

    def test_solution3(self, input_list, testobj, expected):
        assert testobj.solution3(input_list) == expected

    def test_solution4(self, input_list, testobj, expected):
        assert testobj.solution4(input_list) == expected

    def test_solution5(self, input_list, testobj, expected):
        assert testobj.solution5(input_list) == expected
