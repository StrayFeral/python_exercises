import pytest

import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from proper_class_declaration import DummyClass


# Solution 2) Use pre-defined data
data_1 = [(DummyClass(11), DummyClass(22), DummyClass(33), (11, 22))]
data_2 = [(DummyClass(22), DummyClass(11), DummyClass(11), (22, 11))]
data_3 = [(DummyClass(11), DummyClass(11), True)]
data_4 = [(DummyClass(11), "11")]
data_5 = [(DummyClass(11), DummyClass(22), 33, 22)]
data_6 = [(DummyClass(22), DummyClass(11), 11, 11)]


class TestDummyClassPytestVersion:
    """Proper unit test for DummyClass.

    The folowing code was separated and made in a more Pythonic way.

    This class went trough several refactorings:
    1) The unittest way
    2) The fixture way
    3) Finally - the parametrizing way

    pytest -m smoke test_proper_class_declaration_pytest.py # Smoke testing
    pytest test_proper_class_declaration_pytest.py          # Regression testing
    """

    # Solution 1) Use pytest fixtures
    # @pytest.fixture
    # def b1(self):
    #    return DummyClass(11)
    # .............. and so on ...........

    @pytest.mark.parametrize("a, b, expected_1, expected_2", data_1)
    def test_plus_operator(self, a, b, expected_1, expected_2):
        assert a + b == expected_1
        assert (a.x, b.x) == expected_2

    @pytest.mark.smoke
    @pytest.mark.parametrize("a, b, expected_1, expected_2", data_2)
    def test_minus_operator(self, a, b, expected_1, expected_2):
        assert a - b == expected_1
        assert (a.x, b.x) == expected_2

    @pytest.mark.parametrize("a, b, expected", data_3)
    def test_equals_operator(self, a, b, expected):
        assert (a == b) is expected

    @pytest.mark.parametrize("a, expected", data_4)
    def test_str_operator(self, a, expected):
        assert str(a) == expected

    @pytest.mark.smoke
    @pytest.mark.parametrize("a, b, expected_1, expected_2", data_5)
    def test_augmented_addition(self, a, b, expected_1, expected_2):
        x1, x2 = a, b
        x1 += x2
        assert x1.x == expected_1
        assert x2.x == expected_2

    @pytest.mark.parametrize("a, b, expected_1, expected_2", data_6)
    def test_augmented_subtraction(self, a, b, expected_1, expected_2):
        x1, x2 = a, b
        x1 -= x2
        assert x1.x == expected_1
        assert x2.x == expected_2
