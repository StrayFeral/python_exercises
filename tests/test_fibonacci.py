import pytest
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from classic_exercises.fibonacci import FibonacciCalculator


@pytest.fixture
def nmin():
    return 0


@pytest.fixture
def nmax():
    return 10


@pytest.fixture
def expected():
    return [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


@pytest.fixture
def testobj():
    return FibonacciCalculator()


class TestFibonacci:
    def test_sequence(self, nmin, nmax, testobj, expected):
        actual = [testobj.calculate(n) for n in range(nmin, nmax+1)]
        assert actual == expected
    
    def test_sequence_fast_calc(self, nmin, nmax, testobj, expected):
        actual = [testobj.fast_calc(n) for n in range(nmin, nmax+1)]
        assert actual == expected
