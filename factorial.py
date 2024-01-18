#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pprint

# Note: pprint in Python is like Data::Dumper in Perl - always nice to have it
pp = pprint.PrettyPrinter(indent=4)  # Data::Dumper
# pp.pprint(something)
# (and no - pprint have nothing to do with factorial calculation,
# but from my years old Perl practice, I always have such a thing
# declared and ready to use)


class FactorialCalculator:
    r"""Class to calculate the factorial of a number.
    2021, Evgueni.Antonov@gmail.com

    WHAT IS FACTORIAL OF A NUMBER:
    The factorial of a number is the product of all the integers from 1
    to that number.

    For example, the factorial of 6 is 1*2*3*4*5*6 = 720. Factorial is
    not defined for negative numbers, and the factorial of zero is one,
    0! = 1."""

    def calculate(self, n: int) -> int:
        """Okay, this is fairly simple and any newbie out there must
        be able to understand it. Factorial is a classic programming
        problem, listed in all programming books (I guess all?).

        This is a simple recursion example.

        Enjoy."""

        if n < 0:
            return None
        if n == 0:
            return 1

        while n > 0:
            return n * self.calculate(n - 1)

    def calc2(self, n: int) -> int:
        """Second solution. Much simpler, without recursion."""

        f = 1
        for i in range(n, 1, -1):
            f = f * i
        return f


class FactorialIterator:
    r"""Factorial calculator in the form of a custom iterator.

    I am doing this just as an exercice in custom iterators.
    2023, Evgueni.Antonov@gmail.com"""

    def __init__(self, n: int):
        if n < 0:
            raise Exception("N must be greater than zero.")

        self._final_n = n
        self._n = 0

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self._n <= self._final_n:
            if self._n == 0:
                self._n += 1
                return 1

            n = 1
            for i in range(self._n, 1, -1):
                n = n * i

            self._n += 1
            return n

        else:
            raise StopIteration


# ================================================================ MAIN
if __name__ == "__main__":
    try:
        n = 6
        fc = FactorialCalculator()
        print("Hey y'all, let's calculate factorial of {0}!".format(n))

        # REMINDER: In mathematics, factorial of a number is noted,
        # using the exclamation mark! So in the string below, the
        # exclamation mark means "factorial" and not "not" !
        print("ANSWER:  {0}! == {1}".format(n, fc.calculate(n)))
        print("ANSWER2: {0}! == {1}".format(n, fc.calc2(n)))

        print("--------- Using custom iterator:")
        # We iterate two lists in paralel
        for i, f in zip(range(n + 1), FactorialIterator(n)):
            print("{0}! == {1}".format(i, f))

        print("Program end. Bye.")

    except Exception as e:
        print("================== Uncaught exception:")
        print(str(e))
