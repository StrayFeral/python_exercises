#!/usr/bin/env python

# Google Fire test

"""
FIRE adds cli interface to an existing callable. If callable is a class
then first parameter is a method, next params are all method arguments.

--help or -h is recognized and automatic help is shown.

Output string manipulations are possible:
Usage: fire_test.py -n=<NAME> <command>
  available commands:    capitalize | casefold | center | count | encode |
                         endswith | expandtabs | find | format | format_map |
                         index | isalnum | isalpha | isascii | isdecimal |
                         isdigit | isidentifier | islower | isnumeric |
                         isprintable | isspace | istitle | isupper | join |
                         ljust | lower | lstrip | maketrans | partition |
                         removeprefix | removesuffix | replace | rfind |
                         rindex | rjust | rpartition | rsplit | rstrip |
                         split | splitlines | startswith | strip | swapcase |
                         title | translate | upper | zfill

For detailed information on this command, run:
  fire_test.py -n=John --help

"""

import fire

def hello(name="World"):
  return "Hello %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)
