#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pprint
from collections import Counter
import numpy
import pandas

# Note: pprint in Python is like Data::Dumper in Perl - always nice to have it
pp                              = pprint.PrettyPrinter(indent = 4) # Data::Dumper
# pp.pprint(something)
# (and no - pprint have nothing to do with this exercise, 
# but from my years old Perl practice, I always have such a thing
# declared and ready to use)


class UniqueCounter:
    """Class to count unique values in a list.
    2021, Evgueni.Antonov@gmail.com"""
    
    
    def solution1(self, some_list:list) -> int:
        """This is not very pythonic.
        I used to do this in Perl when reading files, so it is
        applicable to other programming languages.
        
        A good thing here is, this is extremely easy to understand in
        any language."""
        
        unique_holder           = {}
        
        for val in some_list:
            if val not in unique_holder.keys():
                unique_holder[val] = 0
            
            # Now we know how many times each value is in the list
            unique_holder[val]  += 1
        
        print("*** Solution1: How many times each value is found:")
        pp.pprint(unique_holder)
        
        return len(unique_holder)
    
    
    def solution2(self, some_list:list) -> int:
        """Some pythonic way. Obviously this is gonna be faster.
        Also, this is the simplest pythonic way."""
        return len(set(some_list))
    
    
    def solution3(self, some_list:list) -> int:
        """Using Counter - probably the best pythonic way.
        
        Counter counts hashable objects and seems to be created
        exactly for this job."""
        
        print("*** Solution3: How many times each value is found:")
        # Converting two lists into a single dictionary
        counts                  = dict(zip(Counter(some_list).keys(), Counter(some_list).values()))
        pp.pprint(counts)
        
        return len(Counter(some_list).keys())
    
    
    def solution4(self, some_list:list) -> int:
        """Using Numpy - another pythonic way.
        
        While this perfectly does the job, it is actually created with
        lots of other things in mind and doing this, if we don't need it
        for other things, feels a bit like using a tank for grocery
        shopping. Well, my opinion."""
        
        # On top of that, the returned values are sorted
        values, counts1         = numpy.unique(some_list, return_counts=True)
        
        print("*** Solution4: How many times each value is found:")
        counts                  = dict(zip(values, counts1))
        pp.pprint(counts)
        
        return len(values)
    
    
    def solution5(self, some_list:list) -> int:
        """And finally - Pandas.
        However I got this one from Internet. I am not really familiar
        with Pandas at the moment.
        
        Leaving this here just for the record.
        
        Again - using Pandas just for this task feels like using a tank
        for grocery shopping, but it does the job and I list it here
        for the record.
        
        5 solutions are more than enough."""
        
        return pandas.Series(some_list).nunique()





# ================================================================ MAIN
if __name__ == '__main__':
    try:
        cool_list               = [1, 3, 21, 3, 45, 3, 'meh', 'blah', 21, 9, 3]
        uc                      = UniqueCounter()
        
        print("Hey y'all, let's count the unique values in this list:")
        pp.pprint(cool_list) # Now see why pprint is useful?
        
        print("Solution1 unique values found: {0}".format(uc.solution1(cool_list)))
        print("Solution2 unique values found: {0}".format(uc.solution2(cool_list)))
        print("Solution3 unique values found: {0}".format(uc.solution3(cool_list)))
        print("Solution4 unique values found: {0}".format(uc.solution4(cool_list)))
        print("Solution5 unique values found: {0}".format(uc.solution5(cool_list)))
        
        print("Program end. Bye.")
    
    
    except Exception as e:
        print("================== Uncaught exception:")
        print(str(e))


