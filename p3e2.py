#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: jeremiah.marks
# @Date:   2015-03-03 18:26:58
# @Last Modified by:   jeremiah.marks
# @Last Modified time: 2015-03-03 19:05:30


#Part3 exercise 2

###        Problem 2
  # 2. Consider the LoopingCall class in twisted.internet.task.
  # Rewrite the countdown program above to use LoopingCall.
  # You only need the start and stop methods and you don’t
  # need to use the “deferred” return value in any way.
  # We’ll learn what a “deferred” value is in a later Part.

## twisted documentation on internet.task:
  ## http://twistedmatrix.com/documents/current/api/twisted.internet.task.html
## on task.LoopingCall:
  ## http://twistedmatrix.com/documents/current/api/twisted.internet.task.LoopingCall.html


## Highlights:
  ## twisted.internet.task.LoopingCall.__init__(self, f, *a, **kw)
    ## f =The function to call.
    ## a =A tuple of arguments to pass the function.
    ## kw =A dictionary of keyword arguments to pass to the function.
  ## twisted.internet.task.LoopingCall.start(self, interval, now=True)
    ## interval -- The number of seconds between calls. May be less than one. Precision will depend on the underlying platform, the available hardware, and the load on the system.
    ## now -- If True, run this call right now. Otherwise, wait until the interval has elapsed before beginning.


import time
from twisted.internet.task import LoopingCall

class loopingCounter(object):

    def __init__(self, counterStart, name, delayTime):
      self.complete=False
      self.counter, self.name, self.delayTime = (counterStart, name, delayTime)
      self.starttime=time.time()
      self.lc=LoopingCall(self.count)

    def count(self)