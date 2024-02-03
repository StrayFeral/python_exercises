#!/usr/bin/env python3

# Testing simple way to handle command-line arguments

import sys
import os


# pprint(sys.argv)

# Exit code 0 (os.EX_OK) means OK
if len(sys.argv) < 2:
    print("no arguments!")
    sys.exit(os.EX_USAGE)

if sys.argv[1].lower() == "hey":
    print("hey ho!")
else:
    print("wrong argument1 value!")
    sys.exit(os.EX_USAGE)

sys.exit(os.EX_OK)
