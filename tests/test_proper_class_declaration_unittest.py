import unittest

import sys
sys.path.append('..')
from proper_class_declaration import DummyClass



class TestDummyClassUnittestVersion(unittest.TestCase):
    """Proper unit test for DummyClass.
    
    The folowing code was separated and made in a more Pythonic way.
    
    python -m unittest test_proper_class_declaration_unittest.py
    """
    
    def setUp(self):
        self.b1 = DummyClass(11)
        self.b2 = DummyClass(22)
        self.b3 = DummyClass(11)
    
    
    def test_default_values(self):
        self.assertEqual(self.b1.x, 11, 'incorrect default x.')
        self.assertEqual(self.b2.x, 22, 'incorrect default x.')
        self.assertEqual(self.b3.x, 11, 'incorrect default x.')
    
    
    def test_plus_operator(self):
        self.assertEqual(self.b1 + self.b2, DummyClass(33), 'incorrect addition in plus operator.')
        self.assertEqual(self.b1.x, 11, 'incorrect addition in plus operator.') # Value should not be changed
        self.assertEqual(self.b2.x, 22, 'incorrect addition in plus operator.') # Value should not be changed
    
    
    def test_minus_operator(self):
        self.assertEqual(self.b2 - self.b1, DummyClass(11), 'incorrect addition in plus operator.')
        self.assertEqual(self.b1.x, 11, 'incorrect addition in plus operator.') # Value should not be changed
        self.assertEqual(self.b2.x, 22, 'incorrect addition in plus operator.') # Value should not be changed
    
    
    def test_equals_operator(self):
        self.assertEqual(self.b1 == self.b3, True, 'incorrect operation of the equals operator.')
    
    
    def test_str_operator(self):
        self.assertEqual(str(self.b1), "11", 'incorrect operation of the str operator.')
    
    
    def test_augmented_addition(self):
        self.b1 += self.b2
        self.assertEqual(self.b1.x, 33, 'incorrect addition.') # 11 + 22
        self.assertEqual(self.b2.x, 22, 'incorrect addition.')
    
    
    def test_augmented_subtraction(self):
        self.b2 -= self.b1
        self.assertEqual(self.b1.x, 11, 'incorrect subtraction.')
        self.assertEqual(self.b2.x, 11, 'incorrect subtraction.') # 22 - 11

    
    def tearDown(self):
        del(self.b1)
        del(self.b2)
        del(self.b3)
