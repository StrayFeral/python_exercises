import pytest
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from classic_exercises.distinct_characters_substring import DistinctCharacters


test_data = [
    (DistinctCharacters("ecebaa", 2), 3),
    (DistinctCharacters("aabacccac", 2), 6),
    (DistinctCharacters("aabacccac", 1), 3),
]


class TestSpecialSubstring:
    @pytest.mark.parametrize("testobj, expected", test_data)
    def test_result_type(self, testobj, expected):
        actual = testobj.substring_length()
        assert isinstance(actual, int)

    @pytest.mark.parametrize("testobj, expected", test_data)
    def test_result_values(self, testobj, expected):
        actual = testobj.substring_length()
        assert actual == expected
