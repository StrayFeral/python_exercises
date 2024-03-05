class FactorialCalculator:
    r"""Class to calculate the factorial of a number.
    2024, Evgueni.Antonov@gmail.com

    WHAT IS FACTORIAL OF A NUMBER:
    The factorial of a number is the product of all the integers from 1
    to that number.

    For example, the factorial of 6 is 1*2*3*4*5*6 = 720. Factorial is
    not defined for negative numbers, and the factorial of zero is one,
    0! = 1."""
    
    def __init__(self) -> None:
        self.memo: dict = {
            0: 1,
            1: 1,
        }

    def calculate(self, n: int) -> int:
        """Okay, this is fairly simple and any newbie out there must
        be able to understand it. Factorial is a classic programming
        problem, listed in all programming books (I guess all?).

        This is a simple recursion example.
        
        Update 2024-03-05: Implemented memoization.

        Enjoy."""

        if n < 0:
            raise ValueError("Method expects a positive integer argument.")
        
        if n not in self.memo:
            self.memo[n] =  n * self.calculate(n - 1)
        
        return self.memo[n]

    def calc2(self, n: int) -> int:
        """Second solution. Much simpler, without recursion."""

        f = 1
        if n not in self.memo:
            for i in range(n, 1, -1):
                f = f * i
            self.memo[n] = f
        return self.memo[n]


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
