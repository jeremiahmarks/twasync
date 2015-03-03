#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: jeremiah.marks
# @Date:   2015-03-02 14:01:03
# @Last Modified 2015-03-02
# @Last Modified time: 2015-03-02 22:43:09
# from:  http://krondo.com/?p=1209


## other articles of note :  

## Blocking vs non-blocking sockets
  ## http://www.scottklement.com/rpg/socktut/nonblocking.html


# From the command line ran :  

# jlmarks@NV55C-jlmarks:~/twasync$ python jdavisp3-twisted-intro-8f9d137/blocking-server/slowpoetry.py jdavisp3-twisted-intro-8f9d137/poetry/ecstasy.txt Serving jdavisp3-twisted-intro-8f9d137/poetry/ecstasy.txt on port 34922.
# Somebody at ('127.0.0.1', 56659) wants poetry!
# Sending 10 bytes
# Sending 10 bytes
# Sending 10 bytes
# Sending 10 bytes
# Sending 10 bytes
# Sending 10 bytes
# Sending 10 bytes
# Sending 10 bytes
# Sending 10 bytes


# Then, from a different terminal I ran 

# netcat localhost 34922



# This returned the poem, x bytes at a time.  This illustrates
#   a basic server.  

#############

# Then I started slowpoetry on three different ports with three different poems

#  after that I ran the blocking-client on the three different ports where it 
# downloaded the poem from each server, one after the other.  

# python jdavisp3-twisted-intro-8f9d137/blocking-client/get-poetry.py 10000 10001 10002
# Task 1: get poetry from: 127.0.0.1:10000
# Task 1: got 3003 bytes of poetry from 127.0.0.1:10000 in 0:03:30.968563
# Task 2: get poetry from: 127.0.0.1:10001
# Task 2: got 615 bytes of poetry from 127.0.0.1:10001 in 0:00:43.455451
# Task 3: get poetry from: 127.0.0.1:10002
# Task 3: got 653 bytes of poetry from 127.0.0.1:10002 in 0:00:46.261120
# Got 3 poems in 0:05:00.685134


# Then I ran the async client 

# jlmarks@NV55C-jlmarks:~/twasync$ python jdavisp3-twisted-intro-8f9d137/async-client/get-poetry.py 10000 10001 10002
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 2: got 10 bytes of poetry from 127.0.0.1:10001
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 2: got 5 bytes of poetry from 127.0.0.1:10001
# Task 2 finished
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 3: got 10 bytes of poetry from 127.0.0.1:10002
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 3: got 3 bytes of poetry from 127.0.0.1:10002
# Task 3 finished
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 10 bytes of poetry from 127.0.0.1:10000
# Task 1: got 3 bytes of poetry from 127.0.0.1:10000
# Task 1 finished
# Task 1: 3003 bytes of poetry
# Task 2: 615 bytes of poetry
# Task 3: 653 bytes of poetry
# Got 3 poems in 0:03:30.970315
