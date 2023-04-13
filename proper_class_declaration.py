import unittest



class DummyClass:
    """This is just a basic class.
    
    In this class the exercise is to override some basic dunder methods
    and to provide a basic unit testing. Also the class is properly
    annotated.
    
    Methods in this class are not commented, as all of them are
    pretty self explanatory. Sphinx should not have problems generating
    documentation out of this anyway.
    
    This class has been tested in two ways:
    mypy proper_class_declaration.py    # Passed
    python proper_class_declaration.py  # Passed
    """

    def __init__(self, x) -> None:
        self.__x: int = x


    @property
    def x(self) -> int:
        return self.__x

    
    @x.setter
    def x(self, new_x: int) -> None:
        self.__x = new_x
    
    
    def __add__(self, other) -> object:
        return DummyClass(self.x + other.x)
    
    
    def __sub__(self, other) -> object:
        return DummyClass(self.x - other.x)
    
    
    def __iadd__(self, other) -> object:
        return self.__add__(other)
    
    
    def __isub__(self, other) -> object:
        return self.__sub__(other)


    def __eq__(self, other) -> bool:
        return self.x == other.x


    def __repr__(self) -> str:
        return str(self.x)


    # No need - we have __repl__ declared.
    #def __str__(self) -> str:
    #    return repr(self.x)
    


class DummyClassTester(unittest.TestCase):
    """Tester class."""
    
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



if __name__ == "__main__":
    unittest.main()
