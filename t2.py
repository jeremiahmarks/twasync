#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jeremiah Marks
# @Date:   2015-03-02 23:03:37
# @Last Modified 2015-03-02>
# @Last Modified time: 2015-03-02 23:04:26

import traceback
def stack():
    print 'the py stack'
    traceback.print_stack()

if __name__ == '__main__':
  from twisted.internet import reactor
  reactor.callWhenRunning(stack)
  reactor.run()