#!/usr/bin/env python

# Progress bar test

from time import sleep
from tqdm import tqdm

text = ""
for char in tqdm(["b", "o", "z", "a"]):
    sleep(0.25)
    text += char
