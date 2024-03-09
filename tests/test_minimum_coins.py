import pytest
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from classic_exercises.minimum_coins import MinimumCoinsforPrice


coin_types = [1, 4, 5]

test_data = [
    (MinimumCoinsforPrice(coin_types), 13, 3),
    (MinimumCoinsforPrice(coin_types), 150, 30),
]


class TestSpecialSubstring:
    @pytest.mark.parametrize("testobj, price, expected", test_data)
    def test_result_type(self, testobj, price, expected):
        actual = testobj.calculate(price)
        assert isinstance(actual, int)

    @pytest.mark.parametrize("testobj, price, expected", test_data)
    def test_result_values(self, testobj, price, expected):
        actual = testobj.calculate(price)
        assert actual == expected
