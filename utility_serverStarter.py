#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jeremiah Marks
# @Date:   2015-03-04 22:17:33
# @Last Modified 2015-03-04
# @Last Modified time: 2015-03-04 23:25:39

import subprocess

ports = [14002, 14004, 14006]
bytesizes=[50,40,20]
poetry=['ecstasy.txt',  'fascination.txt',  'science.txt']
serverVars=zip(ports,poetry,bytesizes)
######
## Note this will kill anything that has the names of your
##  poems in its process name
######


for eachPoem in poetry:
    subprocess.call("pkill -f "+ eachPoem, shell=True)

startString="python ~/twasync/jdavisp3-twisted-intro-8f9d137/blocking-server/slowpoetry.py --port %i ~/twasync/jdavisp3-twisted-intro-8f9d137/poetry/%s --num-bytes %i &"
for eachDataSet in serverVars:
    subprocess.call(startString%(eachDataSet[0], eachDataSet[1], eachDataSet[2]), shell=True)

def killServers():
    global poetry
    for eachPoem in poetry:
        subprocess.call("pkill -f "+ eachPoem, shell=True)