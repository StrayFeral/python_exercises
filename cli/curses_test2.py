#!/usr/bin/env python

# Initializing curses test 2

import curses


# Init
stdscr                          = curses.initscr()


def main(stdscr):
    # Clear screen
    stdscr.clear()
    
    stdscr.addstr("Hello World", curses.A_REVERSE)
    
    stdscr.refresh()
    stdscr.getkey() # Pause (Press Any Key)


curses.wrapper(main)
