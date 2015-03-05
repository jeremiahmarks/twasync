#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jeremiah Marks
# @Date:   2015-03-04 22:17:33
# @Last Modified 2015-03-04
# @Last Modified time: 2015-03-04 23:48:45

import subprocess

ports = [14002, 14004, 14006]
bytesizes=[50,40,20]
poetry=['ecstasy.txt',  'fascination.txt',  'science.txt']
pathToSampleCode="~/twasync/jdavisp3-twisted-intro-8f9d137"

serverVars=zip(ports,poetry,bytesizes)
######
## Note this will kill anything that has the names of your
##  poems in its process name
######

def killServer(poemName):
    subprocess.call("pkill -f "+ poemName, shell=True)

def startServers():
    global serverVars
    global pathToSampleCode
    startString="python %s/blocking-server/slowpoetry.py --port %i %s/poetry/%s --num-bytes %i &"
    for eachDataSet in serverVars:
        try:
            subprocess.call(startString%(pathToSampleCode, eachDataSet[0], pathToSampleCode, eachDataSet[1], eachDataSet[2]), shell=True)
        except OSError:
            killServer(eachDataSet[1])
            try:
                subprocess.call(startString%(eachDataSet[0], eachDataSet[1], eachDataSet[2]), shell=True)
            except OSError:
                print "I tried, but I cannot start a server for %s on port %i"%(eachDataSet[1], eachDataSet[0])
        except socket.error:
            killServer(eachDataSet[1])
            try:
                subprocess.call(startString%(eachDataSet[0], eachDataSet[1], eachDataSet[2]), shell=True)
            except socket.error:
                print "I tried, but I cannot start a server for %s on port %i"%(eachDataSet[1], eachDataSet[0])

if __name__ == '__main__':
    for pname in poetry:
        killServer(pname)
    startServers()
