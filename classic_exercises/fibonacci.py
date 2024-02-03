class FibonacciCalculator:
    r"""Fibonacci sequence is a sequence in which each number is the sum
    of the two preceding ones.
    2024, Evgueni.Antonov@gmail.com

    Sequence of numbers from 0 to 10:
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
    """

    def calculate(self, n: int) -> int:
        if n < 0:
            raise ValueError("Method expects a positive integer argument.")

        if n == 0:
            return 0

        if n < 3:
            return 1

        return self.calculate(n - 2) + self.calculate(n - 1)
