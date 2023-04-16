# WORK IN PROGRESS !!!!!!!!!!!!!!!!!

import dill
from typing import List, ClassVar, Set
from collections import deque
from pprint import pprint



class GearWheel:
    """Single gear wheel. A generator.
    
    Args:
        symbol_set: A set of symbols - will be ordered
    
    Returns:
        str
    """
    
    def __init__(self, symbol_set: set, init_value: str = "") -> None:
        self.__index: int = 0
        self.__seq: List[str] = list(symbol_set)
        self.__seq.sort()
        
        if len(symbol_set) == 0:
            raise ValueError("The symbol_set argument cannot be an empty set.")
        
        # In case we are initialized with a value from the set
        if init_value:
            self.__index = self.__seq.index(init_value)
        
        
    #def spin(self):
    #    for item in self.__seq:
    #        yield item
    #    while self.__index < len(self.__seq):
    #        yield self.__seq[self.__index]
    #        self.__index += 1
        
    
    
    def __iter__(self):
        r"""We always need to define __iter__() so the iterator will
        work in a FOR loop"""
        return self
    
    
    def __next__(self) -> str:
        if self.__index < len(self.__seq):
            x = self.__seq[self.__index]
            self.__index += 1
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
    
    
    def __init__(self, symbol_set: set, min_length: int, max_length: int) -> None:
        self.__gears: List[GearWheel] = []
        
        self.__symbol_set = symbol_set
        self.__min_length = min_length
        self.__max_length = max_length
        
        if min_length or max_length == 0:
            raise ValueError("The min_length or max_length arguments cannot be zero.")
        
        for i in range(1, min_length):
            self.__gears.append(GearWheel(self.__symbol_set))
    
    #def spin_wheels(self) -> str: # Next
    def __next__(self) -> str:
        result_list: List[str] = []
        
        for i in length(self.__gears) -1:
            if i-1 == -1:
                try:
                    result_list[i] = next(self.__gears[i])
                except:
                    self.__gears[i] = GearWheel(self.__symbol_set)
            elif result_list[i-1] == startovia simvol:
                # spin wheel
        
        
        # finally ________________
        # zawyrti tekushtoto
        # on exception go resetni i zawyrti sledwashtoto
        spin_wheels = True
        i = 0
        while spin_wheels:
            try:
                result = next(self.__gears[i])
                yield result # towa triabwa da e string !!
                i += 1
                
            except StopIteration:
                self.__gears[i] = GearWheel(self.__symbol_set)
                i += 1
                
                # Add a new gear
                if i == len(self.__gears) and i <= self.__max_length:
                    self.__gears.append(GearWheel(self.__symbol_set))
                else:
                    spin_wheels = False
                    # raise StopIteration # ???
        
        
        
        #for gear in self.__gears:
        #    symbol = gear.spin()
        #    yield symbol
        
        result = "".join(result_list)
        
        if result == self.__symbol_set[-1] * self.__max_length:
            raise StopIteration
        
        #return result
        #yield result
    
    
    #def __getstate__(self) -> str:
    #    """Provides ONLY properties which will be serialized."""
    #    attributes = self.__dict__.copy() # Copy all attributes
    #    #del attributes['attribute_name_here'] # Deletes attributes which will not be serialized
    #    return attributes
    #    
    #    # dill.dump(self) # ??? serialization
    
    
    def __setstate__(self, state: str):
        self.__dict__ = state
        # self.bleh = bloh # Re-initialize attributes which were not serialized and adding them back



# ---------------------------------------------------------------- MAIN
if __name__ == "__main__":
    # Setup
    symbol_set = {"0", "1", "2", "a", "b"} # It will be sorted anyway
    min_length = 2
    max_length = 4
    
    # Test
    permutator = GearPermutator(symbol_set, min_length, max_length)
    #permutator.meh()
