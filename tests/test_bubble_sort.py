import pytest
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from classic_exercises.bubble_sort import BubbleSorter


@pytest.fixture
def input_list():
    return [4, 1, 5, 3, 2]


@pytest.fixture
def testobj():
    return BubbleSorter()


@pytest.fixture
def expected():
    return [1, 2, 3, 4, 5]


class TestBubbleSorter:
    def test_sort(self, input_list, testobj, expected):
        testobj.sort(input_list) # Modifies the original list
        assert input_list == expected
