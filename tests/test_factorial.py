import pytest
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from classic_exercises.factorial import FactorialCalculator, FactorialIterator

# 6! == 720


@pytest.fixture
def n():
    return 6


@pytest.fixture
def expected():
    return 720


class TestFactorial:
    def test_calc1(self, n, expected):
        fc = FactorialCalculator()
        assert fc.calculate(n) == expected

    def test_calc2(self, n, expected):
        fc = FactorialCalculator()
        assert fc.calc2(n) == expected

    def test_iterator(self, n, expected):
        actual: int = 0
        for i, f in zip(range(n + 1), FactorialIterator(n)):
            # print("{0}! == {1}".format(i, f))
            actual = f
        assert actual == expected  # Comparing just the last one
