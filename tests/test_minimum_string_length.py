import pytest
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from classic_exercises.minimum_string_length import MinimumStringLength


test_data = [
    (MinimumStringLength(), "ca", 2),
    (MinimumStringLength(), "cabaabac", 0),
    (MinimumStringLength(), "aabccabba", 3)
]


class TestSpecialSubstring:
    @pytest.mark.parametrize("testobj, s, expected", test_data)
    def test_result_type(self, testobj, s, expected):
        actual = testobj.calculate(s)
        assert isinstance(actual, int)

    @pytest.mark.parametrize("testobj, s, expected", test_data)
    def test_result_values(self, testobj, s, expected):
        actual = testobj.calculate(s)
        assert actual == expected
