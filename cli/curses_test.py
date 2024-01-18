#!/usr/bin/env python

# Initializing curses test 1

import curses

# Init
stdscr = curses.initscr()
stdscr.keypad(True)
curses.noecho()
curses.cbreak()


# Terminating
stdscr.keypad(False)
curses.nocbreak()
curses.echo()
curses.endwin()
