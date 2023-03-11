#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools
import pprint

# Note: pprint in Python is like Data::Dumper in Perl - always nice to have it
pp                              = pprint.PrettyPrinter(indent = 4) # Data::Dumper
# pp.pprint(something)
# (and no - pprint have nothing to do with FizzBuzz, but from my years
# old Perl practice, I always have such a thing declared and ready to
# use)


class FizzBuzzer:
    """Class to calculate the FizzBuzz problem.
    2021, Evgueni.Antonov@gmail.com
    
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
    """
    
    fizzbuzz_range              = 50 # A default
    
    
    def solution1(self, rng=fizzbuzz_range):
        """First FizzBuzz solution, that comes to everybody's mind.
        I made this one.
        
        Also of all proposed solutions, this is the the simplest."""
        
        for i in range(1, rng+1):
            s                   = ''
            
            if i % 3 == 0:
                s               = 'Fizz'
            
            if i % 5 == 0:
                s               = '{0}Buzz'.format(s)
            
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
            
            s                   = '[{0}] {1}'.format(i, s)
            print(s)
    
    
    def solution2(self, rng=fizzbuzz_range):
        """Getting a bit more technical. I got this one from
        https://towardsdatascience.com/4-easy-ways-to-beat-fizz-buzz-in-python-cfa2dcb9b813
        
        and experimented a lot with it. While it is confusing at first,
        it provides a cool insight of some other Python mechanics.
        
        To be honest, to me this is a bit of cheating, as we do not get
        real 'calculation'. Instead we get sort of a look-up table,
        in form of iterators with pre-defined iterables, which we later
        combine and in the end dump to the screen."""
        
        # Creating iterator with pre-defined iterables for "Fizz"
        fizz_iterator           = itertools.cycle([""] * 2 + ["Fizz"])
        
        # Creating iterator with pre-defined iterables for "Buzz"
        buzzes_iterator         = itertools.cycle([""] * 4 + ["Buzz"])
        
        # Combining the previous two iterators into a new iterator,
        # containing the iterables for both "Fizz" and "Buzz"
        fizzbuzz_iterator       = ("{0}{1}".format(fizz, buzz) for fizz, buzz in zip(fizz_iterator, buzzes_iterator))
        
        # And yet another iterator, this time containing iterables
        # formatted for final display on screen.
        displayables_iterator   = ("[{0}] {1}".format(i, fizzbuzz_item) for fizzbuzz_item, i in zip(fizzbuzz_iterator, itertools.count(1)))
        
        # Finally! Dumping the range to STDOUT (by creating a slice)
        for i in itertools.islice(displayables_iterator, rng):
            print(i)
    
    
    def solution3(self, rng=fizzbuzz_range):
        """A dirty one-liner. I got it from
        https://towardsdatascience.com/4-easy-ways-to-beat-fizz-buzz-in-python-cfa2dcb9b813
        
        While to some it might look high-tech and hacker-type, this is 
        exactly the style of the infernal famous Perl one-liners, 
        everybody avoid having in real-life (as it makes team work a 
        hell)."""
        
        # As I said, this is a dirty one. What is "map"? Well, if
        # you come from the Perl world, you know how this works.
        # Basically it creates an iterator from the iterables
        # (in our case this is the result of range()) and executes
        # the function (the lambda) on each iterable.
        
        # The asterisk in front of map() unpacks the return list for
        # the print() function call.
        
        # And yes, I know - in the original example, the author negated
        # the result of the division, but this was just making it more
        # bananas, so I put the equality comparisson, as the result
        # proves to be the same (as a one-liner it is bananas enough
        # already).
        
        # And don't get me wrong - kudos to the original author for
        # coming with solution2 and solution3.
        
        # One last thing - the original author was claiming, this
        # is working (and showing test results) a bit slower, than
        # solution2(), however on my time testing I got mixed results,
        # so I am giving up here.
        
        print(*map(lambda i: "[{0}] {1}{2}".format(i, 'Fizz' * (i % 3 == 0), 'Buzz' * (i % 5 == 0)), range(1, rng+1)), sep='\n')
        
        


# ================================================================ MAIN
if __name__ == '__main__':
    try:
        fbz                     = FizzBuzzer()
        print("Hey y'all, let's calculate FizzBuzz of {0}!".format(fbz.fizzbuzz_range))
        
        print("---------------------- solution 1 begin")
        fbz.solution1()
        
        print("---------------------- solution 2 begin")
        fbz.solution2()
        
        print("---------------------- solution 3 begin")
        fbz.solution3()
        
        print("---------------------- Program end. Bye.")
    
    
    except Exception as e:
        print("================== Uncaught exception:")
        print(str(e))
