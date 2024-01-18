#!/usr/bin/env python

# Progress bar test

from time import sleep
from progress.bar import IncrementalBar

bar = IncrementalBar(
    "Processing",
    max=20,
    suffix="[%(index)d/%(max)d] [ETA:%(eta)d|ELA:%(elapsed)d] %(percent)d%%",
)

for i in range(20):
    sleep(0.25)  # Do some work
    bar.next()

bar.finish()
