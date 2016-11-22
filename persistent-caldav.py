#!/usr/bin/python
#
# persistent-caldav.py
#
# An object that connects to the CalDAV service, gets the calendar data
# refreshes is periodically, and generally provides a wrapper that insulates
# any other code from dropped connections, or other CalDAV bugginess

from datetime import datetime
import caldav
from caldav.elements import dav, cdav

testurl = ''

class CalDAVConnection(object):

  def __init__(self, url):
    self.client = caldav.DAVClient(url)
    self.principal = self.client.principal()
    self.calendars = self.principal.calendars()
    if len(self.calendars) > 0:
      self.calendar = self.calendars[0]
      print "Using calendar", self.calendar
    else:
      print "No calendars at provided address"
      exit
    

foo = CalDAVConnection(testurl)
