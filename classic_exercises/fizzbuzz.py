import itertools
from typing import List


class FizzBuzzer:
    """Class to calculate the FizzBuzz problem.
    2024, Evgueni.Antonov@gmail.com

    WHAT IS THE FIZZBUZZ PROBLEM:
    We start to iterate all numbers from 1 up to
    the given end number (in my case, this is 'rng'). For the current
    iterated number, we print 'Fizz', if the number is divisible by 3,
    we print 'Buzz', if the number is divisible by 5 or finally we
    print 'FizzBuzz', if the number is divisible by 3 AND 5.

    This class is made as a little exercise in Python and offers
    few solutions.

    Enjoy and thanks for taking the time to review this.

    NOTE: Originally I came up with solution1(). Then decided to
    dig the net and see what else could be done, so then found
    solution2() and solution3(). I did some time testing, but bash
    time was giving me a bit of weird results on some runs, so I am
    leaving this testing up to you.

    You can diff the outputs of the methods individually, they all
    work the same in the end.

    2024-01-29: Update. I deleted solution3() as I re-factored the
    solutions to return proper values, instead of just printing to
    screen. I also noticed, the source article of solution2() and
    solution3() has been deleted from the author's blog. Anyway.
    This time I also implemented proper tests.
    """

    fbrange = 20  # A default

    def solution1(self, rng: int = fbrange) -> List[str]:
        """First FizzBuzz solution, that comes to everybody's mind.
        I made this one.

        Also of all proposed solutions, this is the the simplest."""

        l: List[str] = [0] * n
        
        for i in range(1, rng + 1):
            s: str = ""

            if i % 3 == 0:
                s = "Fizz"

            if i % 5 == 0:
                s = f"{s}Buzz"

            # Hey, I know, many people would go here with another IF,
            # which will handle the situation where the number will be
            # divisible by both 3 and 5, because they will have a
            # print on each IF. However by using concatenation, we cut
            # out this third IF and save a bit of processing time.
            # (not that on a modern computer anyone really needs it,
            # but it shows a better approach)

            # PS: I know most people would use the '+' operator to
            # handle the concatenation, but I like more the format().
            # You may try it f-strings if you want.

            if len(s) == 0:
                s = str(i)
            l.append(s)
        return l

    def solution2(self, rng: int = fbrange) -> List[str]:
        """Getting a bit more technical. I got this one from
        https://towardsdatascience.com/4-easy-ways-to-beat-fizz-buzz-in-python-cfa2dcb9b813

        and experimented a lot with it. While it is confusing at first,
        it provides a cool insight of some other Python mechanics.

        To be honest, to me this is a bit of cheating, as we do not get
        real 'calculation'. Instead we get sort of a look-up table,
        in form of iterators with pre-defined iterables, which we later
        combine and in the end dump to the screen."""

        # Creating iterator with pre-defined iterables for "Fizz"
        fizz_iterator = itertools.cycle([""] * 2 + ["Fizz"])

        # Creating iterator with pre-defined iterables for "Buzz"
        buzzes_iterator = itertools.cycle([""] * 4 + ["Buzz"])

        # Combining the previous two iterators into a new iterator,
        # containing the iterables for both "Fizz" and "Buzz"
        fizzbuzz_iterator = (
            f"{fizz}{buzz}" for fizz, buzz in zip(fizz_iterator, buzzes_iterator)
        )

        ### And yet another iterator, this time containing iterables
        ### formatted for final display on screen.
        ## displayables_iterator = (
        ##     f"{i}{fizzbuzz_item}"
        ##     for fizzbuzz_item, i in zip(fizzbuzz_iterator,
        ##         itertools.count(1))
        ## )

        ### Finally! Dumping the range to STDOUT (by creating a slice)
        ###  for i in itertools.islice(displayables_iterator, rng):
        ###     print(i)
        ## l: List[str] = list(itertools.islice(displayables_iterator,
        ##     rng))

        # 2024-01-29 Code appended by me (Evgueni)
        # New update: Going tricky with a cool list comprehension in
        # order to make the result look exactly like the result of
        # solution1()
        a: List[str] = list(itertools.islice(fizzbuzz_iterator, rng))
        l: List[str] = [a[i] if a[i] != "" else f"{i+1}" for i in range(rng)]
        return l
