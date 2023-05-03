import re
from typing import List
import threading



class GearIterator:
    r"""GearIterator.
    2023 Evgueni.Antonov@gmail.com
    
    Briefly simulates old gear permutators, like the old cars odometer.
    
    The class is serializable, works with both pickle and dill.
    The class implements the context management protocol.
    The class is thread safe.
    
    Args:
        symbol_list: List of symbols. Mind the order of symbols!
        min_length: Minimum length, default is zero
        max_length: Maximum length, default is zero - means no limit
        init_value: Value to initialize with
    
    Returns:
        str
    """
    
    def __init__(self, symbol_list: List[str], min_length: int = 0, max_length: int = 0, init_value: str = "") -> None:
        if len(symbol_list) == 0:
            raise ValueError("Empty symbol_list given.")
        
        if len(symbol_list) != len(set(symbol_list)):
            raise ValueError("Duplicate symbols in the symbol_list.")
        
        if max_length > 0 and min_length > max_length:
            raise ValueError("min_length is greather than max_length.")
        
        if len(init_value) > 0 and (len(init_value) < min_length or (max_length > 0 and len(init_value) > max_length)):
            raise ValueError("Incorrect init_value length.")
        
        regex_str = re.sub(r"[\s,']", "", str(symbol_list))
        regex_str = re.sub(r"\[", "[^", regex_str)
        regex = re.compile(regex_str)
        if regex.search(init_value):
            raise ValueError("Incorrect symbols in init_value, which are not in the symbols_list.")
        
        self.__init_value_returned: bool = False
        self.__index: int = 0
        self.__symbol_list: List[str] = symbol_list.copy()
        self.__min_length = min_length
        self.__max_length = max_length
        self.__init_value = init_value[::-1] # Reverse the string
        
        min_len = min_length
        if min_len == 0:
            min_len = 1
        
        self.__gears: List[list] = []
        
        # Initialization with init_value
        for symbol in self.__init_value:
            seq = self.__symbol_list.copy()
            
            while seq[0] != symbol:
                seq.pop(0)
            
            self.__gears.append(seq)
        
        # Additional initialization until min_length is reached
        for i in range(len(self.__gears), min_len):
            seq = self.__symbol_list.copy()
            
            if len(self.__init_value) > 0 and i < len(self.__init_value):
                symbol = self.__init_value[i]
                while seq[0] != symbol:
                    seq.pop(0)
            
            self.__gears.append(seq)
        
    
    def __repr__(self) -> str:
        result = ""
        for gear in self.__gears:
            result += gear[0]
        return result[::-1] # Reverse the string
    
    
    def __iter__(self) -> object:
        return self
        
    
    def __next__(self) -> str:
        # Critical section
        with threading.Lock():
            if not self.__init_value_returned:
                self.__init_value_returned = True
                return repr(self)
            
            spin_wheels = True
            i = 0
            while spin_wheels:
                self.__gears[i].pop(0)
                
                # Reset gear
                if len(self.__gears[i]) == 0:
                    self.__gears[i] = self.__symbol_list.copy()
                    i += 1
                    
                    # Add a new gear
                    if i == len(self.__gears) and i < self.__max_length:
                        self.__gears.append(self.__symbol_list.copy())
                        spin_wheels = False
                    
                    if i == self.__max_length:
                        raise StopIteration
                else: # Wheel not yet reached the final set value
                    spin_wheels = False
            
            return repr(self)
    
    
    def __enter__(self) -> object:
        r"""Context management protocol.
        
        Not sure we will need this, but it's there"""
        return self
    
    
    def __exit__(self, exc_type, exc_value, exc_tb) -> bool:
        r"""Context management protocol.
        
        StopIteration exception will not be propagated.
        
        Not sure we will need this, but it's there"""
        return True # We won't propagate the StopIteration exception
