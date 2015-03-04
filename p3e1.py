#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jeremiah Marks
# @Date:   2015-03-04 00:21:03
# @Last Modified 2015-03-04
# @Last Modified time: 2015-03-04 00:26:00
############################################################
## Exercise:
## Update the countdown.py program to have three 
##  independently running counters going at different rates.
##  Stop the reactor when all counters have finished.

import time
class Countdown(object):

    def __init__(self, counterStart, name, delayTime):
        self.complete=False
        self.counter, self.name, self.delayTime = (counterStart, name, delayTime)
        self.starttime=time.time()

    def count(self):
        if self.counter == 0:
          ## this should move to a control loop
            #reactor.stop()
            self.complete=True
            print "%s just finished its last cycle.  It ran for a total of %f seconds"%(self.name, time.time()-self.starttime)
        else:
            self.counter -= 1
            print "%s just ticked and has %i ticks left. delay is %f"%(self.name, self.counter, self.delayTime)

class Countdowns(object):
    """
    Note:  This is a terrible class name since it is only one
    letter different than the other class.  That said, it 
    is designed to hold multiple countdown timers, so
    whatever, I do what I want.
    """

    def __init__(self, *args):
        self.allCountdowns=[Countdown(counterStart, name, delayTime) for counterStart, name, delayTime in args]
        self.activeCounters=sum(1 for eachCounter in self.allCountdowns if eachCounter.complete==False)

    def startTheLoop(self):
        for eachActiveCounter in self.allCountdowns:
            self.theActualLoop(eachActiveCounter)

    def theActualLoop(self, countDownTimer):
        if not countDownTimer.complete:
            countDownTimer.count()
            if countDownTimer.counter==0:
                reactor.callLater(0,self.theActualLoop, countDownTimer)
            else:
                reactor.callLater(countDownTimer.delayTime,self.theActualLoop, countDownTimer)
        else:
            print "%s just finished!"%(countDownTimer.name)
            self.activeCounters=sum(1 for eachCounter in self.allCountdowns if eachCounter.complete==False)
            if self.activeCounters==0: reactor.stop()

if __name__ == '__main__':
    from twisted.internet import reactor
    groupOfCountdowns=Countdowns([10,"a",1.5],[2,"b", 15],[15,"c", 0.7])
    reactor.callWhenRunning(groupOfCountdowns.startTheLoop)
    reactor.run()