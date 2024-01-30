from collections import Counter
import numpy
import pandas
from typing import Dict, List


class UniqueCounter:
    """Class to count unique values in a list.
    2021, Evgueni.Antonov@gmail.com"""

    def solution1(self, some_list: list) -> int:
        """This is not very pythonic.
        I used to do this in Perl when reading files, so it is
        applicable to other programming languages.

        A good thing here is, this is extremely easy to understand in
        any language."""

        unique_holder: Dict[List, int] = {}

        for val in some_list:
            if val not in unique_holder.keys():
                unique_holder[val] = 0

            # Now we know how many times each value is in the list
            unique_holder[val] += 1

        return len(unique_holder)

    def solution2(self, some_list: list) -> int:
        """Some pythonic way. Obviously this is gonna be faster.
        Also, this is the simplest pythonic way."""
        return len(set(some_list))

    def solution3(self, some_list: list) -> int:
        """Using Counter - probably the best pythonic way.

        Counter counts hashable objects and seems to be created
        exactly for this job."""

        # Converting two lists into a single dictionary
        counts = dict(zip(Counter(some_list).keys(), Counter(some_list).values()))

        return len(Counter(some_list).keys())

    def solution4(self, some_list: list) -> int:
        """Using Numpy - another pythonic way.

        While this perfectly does the job, it is actually created with
        lots of other things in mind and doing this, if we don't need it
        for other things, feels a bit like using a tank for grocery
        shopping. Well, my opinion."""

        # On top of that, the returned values are sorted
        values, counts1 = numpy.unique(some_list, return_counts=True)

        counts = dict(zip(values, counts1))

        return len(values)

    def solution5(self, some_list: list) -> int:
        """And finally - Pandas.
        However I got this one from Internet. I am not really familiar
        with Pandas at the moment.

        Leaving this here just for the record.

        Again - using Pandas just for this task feels like using a tank
        for grocery shopping, but it does the job and I list it here
        for the record.

        5 solutions are more than enough."""

        return pandas.Series(some_list).nunique()
