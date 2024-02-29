import pytest
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from classic_exercises.max_profit_calculator import MaxProfitCalculator


@pytest.fixture
def input_prices():
    return [7, 1, 5, 3, 6, 4]


@pytest.fixture
def testobj(input_prices):
    return MaxProfitCalculator(input_prices)


@pytest.fixture
def expected():
    return 5


class TestSpecialSubstring:
    def test_result_type(self, testobj):
        actual = testobj.calculate()
        assert isinstance(actual, int)

    def test_result_values(self, testobj, expected):
        actual = testobj.calculate()
        assert actual == expected
