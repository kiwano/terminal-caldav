#!/usr/bin/python

import curses
import time
import os
import dbus
import subprocess


# Initialize curses
def init_rt():
  stdscr = curses.initscr()
  curses.start_color()
  curses.cbreak()
  curses.noecho()
  curses.nonl()
  curses.intrflush(0)
  stdscr.keypad(1)
  stdscr.nodelay(1)
  return stdscr

# Uninitialize curses so the terminal is usable again after exit
def uninit_rt():
  curses.nocbreak()
  curses.echo()
  curses.nl()
  curses.intrflush(1)
  curses.endwin()
  exit()

# Handle keystrokes
def process_key(stroke):

  if stroke == ord('q'):
    uninit_rt()
  elif stroke == curses.KEY_RESIZE:
    redraw_screen()

# some of the clock data code here probably warrants reuse for display purposes
def get_clockdata():
  curtime = time.localtime()
  timetext = []
  timetext.append(time.strftime('  %a'))
  timetext.append(time.strftime(' %b %d'))
  timetext.append(time.strftime('%H:%M:%S'))
  return{'text': timetext, 'attr': [curses.A_NORMAL, curses.A_NORMAL, curses.A_NORMAL]}

# Update the display
def write_info(item):
  print "foo"

# set up a polling loop
menuitem = 0
stdscr = init_rt()
init_audio()

while 1:
  keystroke = stdscr.getch()
  menuitem = process_key(keystroke);
  write_info(menuitem);
  stdscr.move(0, 0)
  stdscr.refresh();
  time.sleep(0.1)

uninit_rt()

