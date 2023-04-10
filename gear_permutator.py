from typing import List, ClassVar, Set
from pprint import pprint



class GearWheel:
    """Single gear wheel. A generator.
    
    Args:
        symbol_set: A set of symbols
    
    Returns:
        str
    """
    
    # We use this to pad to the desired length, sorta None, however
    # sorted() cannot sort strings and NoneType
    null_value: str = "@@@"
    
    def __init__(self, symbol_set: set, init_value: str = ""):
        self._index: int = 0
        #self._seq: List[str] = sorted(list(symbol_set) + [self.null_value]) # Better be sorted
        self._seq: List[str] = list(symbol_set)
        self._seq.sort()
        self._seq.insert(0, self.null_value) # This have a special function
        
        if len(symbol_set) == 0:
            raise ValueError("The symbol_set argument cannot be an empty set.")
        
        # In case we are initialized with a value from the set
        if init_value:
            self._index = self._seq.index(init_value)
        
        
    #def spin(self):
    #    for item in self._seq:
    #        yield item
    
    
    def __iter__(self):
        r"""We always need to define __iter__() so the iterator will
        work in a FOR loop"""
        return self
    
    
    def __next__(self) -> str:
        if self._index < len(self._seq):
            x = self._seq[self._index]
            self._index += 1
            return x
        else:
            raise StopIteration



class GearPermutator:
    """A Gear Permutator class.
    2023 Evgueni.Antonov@gmail.com
    
    Args:
        symbol_set: A set of symbols, cannot be empty.
        min_length: Desired minimum result length.
        max_length: Desired result length.
    
    Returns/Yields:
        str
    """
    
    
    def __init__(self, symbol_set: set, min_length: int, max_length: int):
        self._gears: List[GearWheel] = []
        
        self._symbol_set = symbol_set
        self._min_length = min_length
        self._max_length = max_length
        
        if min_length or max_length == 0:
            raise ValueError("The min_length or max_length arguments cannot be zero.")
        
        for i in range(1, max_length):
            self._gears.append(GearWheel(self._symbol_set))
    
    #def spin_wheels(self) -> str: # Next
    def __next__(self) -> str:
        result_list: List[str] = []
        
        for i in length(self._gears) -1:
            if i-1 == -1:
                try:
                    result_list[i] = next(self._gears[i])
                except:
                    self._gears[i] = GearWheel(self._symbol_set)
            elif result_list[i-1] == startovia simvol:
                # spin wheel
        
        
        #for gear in self._gears:
        #    symbol = gear.spin()
        #    yield symbol
        
        result = "".join(result_list)
        
        if result == self._symbol_set[-1] * self._max_length:
            raise StopIteration
        
        #return result
        #yield result



# ---------------------------------------------------------------- MAIN
if __name__ == "__main__":
    # Setup
    symbol_set = {"0", "1", "2", "a", "b"} # It will be sorted anyway
    min_length = 2
    max_length = 4
    
    # Test
    permutator = GearPermutator(symbol_set, min_length, max_length)
    #permutator.meh()
