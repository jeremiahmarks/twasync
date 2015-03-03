#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jeremiah Marks
# @Date:   2015-03-02 23:11:48
# @Last Modified 2015-03-03
# @Last Modified time: 2015-03-03 01:26:41


# From http://krondo.com/blog/?p=1333 - suggested Exercises


# 1. Update the countdown.py program to have three 
  # independently running counters going at different rates.
  # Stop the reactor when all counters have finished.
# 2. Consider the LoopingCall class in twisted.internet.task. 
  # Rewrite the countdown program above to use LoopingCall. 
  # You only need the start and stop methods and you don’t 
  # need to use the “deferred” return value in any way. 
  # We’ll learn what a “deferred” value is in a later Part.
############################################################
## 1 
############################################################

#####
# Basic naive approach
#####

# class Countdown(object):
 
#     counter = 5
 
#     # def __init__(self, counterStart):
#     #   self.counter = counterStart
#     #   self.count()

#     def count(self):
#         if self.counter == 0:
#             reactor.stop()
#         else:
#             print self.counter, '...'
#             self.counter -= 1
#             reactor.callLater(1, self.count)

#     def cten(self):
#       self.counter=10
#       self.count()
#     def cfiv(self):
#       self.counter=5
#       self.count()
#     def ctwe(self):
#       self.counter=20
#       self.count()


# if __name__ == '__main__':
#     from twisted.internet import reactor
     
#     reactor.callWhenRunning(Countdown().cten)
#     reactor.callWhenRunning(Countdown().cfiv)
#     reactor.callWhenRunning(Countdown().ctwe)
     
#     print 'Start!'
#     reactor.run()
#     print 'Stop!'
############################################################
## Notes:
        ## this approach stops as soon as the first timer
        ## completes.
        ## I need to be able to store the three timers in an
        ## object and then check if all of the timers have 
        ## completed. 
############################################################

#####
## second attempt
#####


# class Countdown(object):

#     def __init__(self, counterStart):
#       self.complete=False
#       self.counter = counterStart

#     def count(self):
#         if self.counter == 0:
#           ## this should move to a control loop
#             #reactor.stop()
#             self.complete=True
#         else:
#             print self.counter, '...'
#             self.counter -= 1
#             reactor.callLater(1, self.count)

# class Countdowns(object):
#     """
#     Note:  This is a terrible class name since it is only one
#     letter different than the other class.  That said, it 
#     is designed to hold multiple countdown timers, so
#     whatever, I do what I want.
#     """
#     def __init__(self, *args):
#       self.allCountdowns=[Countdown(counterStart) for counterStart, name in args]
#       self.activeCounters=sum(1 for eachCounter in self.allCountdowns if eachCounter.complete==False)

#     def startTheLoop(self):
#       for eachActiveCounter in self.allCountdowns:
#         self.theActualLoop(eachActiveCounter)

#     def theActualLoop(self, countDownTimer):
#       if not countDownTimer.complete:
#           countDownTimer.count()
#           reactor.callLater(1,self.theActualLoop, countDownTimer)
#       else:
#           print "One loop complete"
#           self.activeCounters=sum(1 for eachCounter in self.allCountdowns if eachCounter.complete==False)
#           print "%i loops to go!" %(self.activeCounters)
#           if self.activeCounters==0: reactor.stop()

# if __name__ == '__main__':
#     from twisted.internet import reactor
#     groupOfCountdowns=Countdowns([3,"a"],[5,"b"],[10,"c"])
#     reactor.callWhenRunning(groupOfCountdowns.startTheLoop)
#     reactor.run()
############################################################
## Notes:
    # This runs as intended, however I have seen examples that
    # Include a variable timer, and they also have some easier 
    # text to understand what is going on. I think that I will
    # implement that basic functionality and then move to problem
    # 2
############################################################

###
## Third approach
###
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
############################################################
## Notes:
    ## this runs more or less as expected. I found that I was 
    ## calling reactor.callLater in both classes, once I resolved
    ## that issue, the program ran more or less as expected.
    ## although I did need to retool the process where it completes.
    ## The way that it was before made it so that the reactor
    ## was getting called for the delay even after there were
    ## zero cycles left.  
############################################################