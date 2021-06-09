#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pprint

# Note: pprint in Python is like Data::Dumper in Perl - always nice to have it
pp                              = pprint.PrettyPrinter(indent = 4) # Data::Dumper
# pp.pprint(something)
# (and no - pprint have nothing to do with bubble sorting, 
# but from my years old Perl practice, I always have such a thing
# declared and ready to use)


class BubbleSorter:
    """Class to do bubble sorting on a list.
    2021, Evgueni.Antonov@gmail.com
    
    WHAT IS THE BUBBLE SORTING ALGORITHM:
    Simple sorting, that iterates trough list elements, compares them
    and swaps them, if they are in the wrong order.
    
    NOTE: All list elements are supposed to be of the same type.
    (classic example is with integers)"""
    
            
    def sort(self, some_list:list):
        """Bubble sort method - the very basic and classic way, I
        first learned to do it in Pascal in the year 1991.
        
        This method expects a list of integers!"""
        
        # Okay, let's sort someting else first - most modern
        # programming languages DO have their own sorting implementations
        # which usually work pretty well and fast. You do not need this.
        # However this is a more than classic programming task, which
        # every programmer is supposed to learn at school.
        
        # So this is how I first learned to do this in Pascal in the
        # far good year of 1991. Back then I was a happy high-schooler,
        # just learning the basics of DOS and the back then modern
        # Pascal programming language, after I already knew some
        # BASIC programming for Apple ][ clones.
        
        # Basically we have two loops: one going forward and one
        # going backwards, checking and swapping elements, if not in
        # order. This way the values pop up like bubbles to the
        # surface (the list end).
        
        for i in range(0, len(some_list) - 1):
            for j in reversed(range(i + 1, len(some_list))):
                # Just in case... (in Pascal you don't need to do it, but here you may)
                if not isinstance(some_list[i], int) or not isinstance(some_list[j], int):
                    raise Exception("The list element is not an integer! Can't continue!")
                    
                # Swapping
                if some_list[i] > some_list[j]:
                    some_list[i], some_list[j] = some_list[j], some_list[i]
        
        

# ================================================================ MAIN
if __name__ == '__main__':
    try:
        cool_list               = [4, 1, 5, 3, 2]
        b                       = BubbleSorter()
        
        print("Hey y'all, let's do bubble sort of this list:")
        pp.pprint(cool_list) # Now see why pprint is useful?
        
        print("---------------------------- sorted:")
        b.sort(cool_list)
        pp.pprint(cool_list)
        
        print("Program end. Bye.")
    
    
    except Exception as e:
        print("================== Uncaught exception:")
        print(str(e))

