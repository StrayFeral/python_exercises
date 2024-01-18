#!/usr/bin/env python

import pprint

# Note: pprint in Python is like Data::Dumper in Perl - always nice to have it
pp = pprint.PrettyPrinter(indent=4)  # Data::Dumper
# pp.pprint(something)
# (and no - pprint have nothing to do with current class,
# but from my years old Perl practice, I always have such a thing
# declared and ready to use)


class Singleton:
    """Simple singleton pattern class.
    2021, Evgueni.Antonov@gmail.com"""

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance


# ================================================================ MAIN
if __name__ == "__main__":
    try:
        print("Singleton test")

        s = Singleton()
        pp.pprint(s)  # Now see why pprint is useful?

        print("object id: {0}".format(id(s)))

        d = Singleton()
        print("object id: {0}".format(id(d)))

        print("Program end. Bye.")

    except Exception as e:
        print("================== Uncaught exception:")
        print(str(e))
