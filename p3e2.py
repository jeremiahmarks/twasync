#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: jeremiah.marks
# @Date:   2015-03-03 18:26:58
# @Last Modified 2015-03-03
# @Last Modified time: 2015-03-03 21:52:13

# Part3 exercise 2
# from http://krondo.com/?p=1333
###        Problem 2
    # 2. Consider the LoopingCall class in twisted.internet.task.
    # Rewrite the countdown program above to use LoopingCall.
    # You only need the start and stop methods and you don’t
    # need to use the “deferred” return value in any way.
    # We’ll learn what a “deferred” value is in a later Part.

import time
from twisted.internet.task import LoopingCall

class loopingCounter(object):
    activeCounters=0

    def __init__(self, counterStart, name, delayTime):
        self.counter, self.name, self.delayTime = (counterStart, name, delayTime)
        self.starttime=time.time()
        loopingCounter.activeCounters+=1
        self.lc=LoopingCall(self.count)
        self.lc.start(self.delayTime)

    def count(self):
        if self.counter == 1:
            loopingCounter.activeCounters-=1
            self.lc.stop()
            print "%s just finished its last cycle.  It ran for a total of %f seconds"%(self.name, time.time()-self.starttime)
            if loopingCounter.activeCounters==0: reactor.stop()
        else:
            self.counter -= 1

if __name__ == '__main__':
    from twisted.internet import reactor
    groupOfCountdowns=[]
    for each in ([10,"a",1.5],[2,"b", 15],[15,"c", 0.7]):
        groupOfCountdowns.append(loopingCounter(each[0], each[1], each[2]))
    reactor.run()