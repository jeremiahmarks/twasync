#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: jeremiah.marks
# @Date:   2015-03-03 18:26:58
# @Last Modified 2015-03-03
# @Last Modified time: 2015-03-03 21:23:07


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

    def count(self):
        if self.counter == 0:
            self.complete = True
            self.lc.stop()
            print "%s just finished its last cycle.  It ran for a total of %f seconds"%(self.name, time.time()-self.starttime)
        else:
            self.counter -= 1
            print "%s just ticked and has %i ticks left. delay is %f"%(self.name, self.counter, self.delayTime)


class counterHolder(object):

    def __init__(self, *args):
        self.allCountdowns=[loopingCounter(counterStart, name, delayTime) for counterStart, name, delayTime in args]
        self.activeCounters = (1 for eachCounter in self.allCountdowns if eachCounter.complete==False)

    def startTheLoop(self):
        for eachCounter in self.allCountdowns:
            eachCounter.lc.start(eachCounter.delayTime)
            self.theActualLoop(eachCounter)
    def theActualLoop(self,countDownTimer):
        if not countDownTimer.complete:
            countDownTimer.count()
            self.activeCounters=sum(1 for eachCounter in self.allCountdowns if eachCounter.complete==False)
            if self.activeCounters==0: reactor.stop()
        else:
            self.activeCounters=sum(1 for eachCounter in self.allCountdowns if eachCounter.complete==False)
            print "%s just finished!\t\t%i"%(countDownTimer.name, self.activeCounters)
            if self.activeCounters==0: reactor.stop()

if __name__ == '__main__':
    from twisted.internet import reactor
    groupOfCountdowns = counterHolder([10,"a",1.5],[2,"b", 15],[15,"c", 0.7])
    reactor.callWhenRunning(groupOfCountdowns.startTheLoop)
    reactor.run()