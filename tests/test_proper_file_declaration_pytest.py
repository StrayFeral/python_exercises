import pytest

"""WORK IN PROGRESS!!"""

import sys
sys.path.append('..')
from proper_class_declaration import DummyClass

b1 = DummyClass(11)
b2 = DummyClass(22)
b3 = DummyClass(11)


def test_default_values():
    assert b1.x == 11
    assert b2.x == 22
    assert b3.x == 11


def test_plus_operator():
    assert b1 + b2 == DummyClass(33)
    assert b1.x == 11 # Value should not be changed
    assert b2.x == 22 # Value should not be changed


def test_minus_operator():
    assert b2 - b1 == DummyClass(11)
    assert b1.x == 11 # Value should not be changed
    assert b2.x == 22 # Value should not be changed


def test_equals_operator():
    assert (b1 == b3) is True


def test_str_operator():
    assert str(b1) == "11"


def test_augmented_addition():
    b1 += b2
    assert b1.x == 33 # 11 + 22
    assert b2.x == 22


def test_augmented_subtraction():
    b2 -= b1
    assert b1.x == 11
    assert b2.x == 11 # 22 - 11
