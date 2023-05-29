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
        self._x: int = x


    @property
    def x(self) -> int:
        return self._x

    
    @x.setter
    def x(self, new_x: int) -> None:
        self._x = new_x
    
    
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
