#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jeremiah Marks
# @Date:   2015-03-04 00:08:43
# @Last Modified 2015-03-04
# @Last Modified time: 2015-03-04 01:13:54

############################################################
## Exercise: 
## Use callLater to make the client timeout if a poem hasn’t 
## finished after a given interval. Read about the return 
## value of callLater so you can cancel the timeout if the 
## poem finishes on time.
############################################################

############################################################
## A couple of notes. 
##      This is actually very ugly.  If I had more time to 
##      implement something better than wrapping potential
##      trouble spots in tries, I would probably do some
##      sort of checking to make sure it is a duck, but
##      I am more interested in playing with twisted.
############################################################

import datetime, errno, optparse, socket
from twisted.internet import main
import twisted.internet.error

## Create the method that will kill the poetry sockets that
## live too long

def socketKiller(listOfSockets):
    for eachSocket in listOfSockets:
        eachSocket.connectionLost("You're too slow")

def poetry_main(listOfPorts):
    addresses = []
    for eachPort in listOfPorts:
        addresses.append(('127.0.0.1',eachPort))
    start = datetime.datetime.now()
    sockets = [PoetrySocket(i + 1, addr) for i, addr in enumerate(addresses)]
    from twisted.internet import reactor
    reactor.callLater(5, socketKiller, sockets)
    reactor.run()
    elapsed = datetime.datetime.now() - start
    for i, sock in enumerate(sockets):
        print 'Task %d: %d bytes of poetry' % (i + 1, len(sock.poem))
    print 'Got %d poems in %s' % (len(addresses), elapsed)

############################################################
## Below here are the methods that I do not expect that I 
## will need to edit, but do need to keep the functionality
## of the original script
############################################################

############################################################
## oh, and of course "if name==main"
############################################################
def parse_args():
    usage = """usage: %prog [options] [hostname]:port ...
This is the Get Poetry Now! client, Twisted version 1.0.
Run it like this:
  python get-poetry.py port1 port2 port3 ...
If you are in the base directory of the twisted-intro package,
you could run it like this:
  python twisted-client-1/get-poetry.py 10001 10002 10003
to grab poetry from servers on ports 10001, 10002, and 10003.
Of course, there need to be servers listening on those ports
for that to work.
"""
    parser = optparse.OptionParser(usage)
    _, addresses = parser.parse_args()
    if not addresses:
        print parser.format_help()
        parser.exit()
    
    def parse_address(addr):
        if ':' not in addr:
            host = '127.0.0.1'
            port = addr
        else:
            host, port = addr.split(':', 1)
        if not port.isdigit():
            parser.error('Ports must be integers.')
        return host, int(port)
    return map(parse_address, addresses)


class PoetrySocket(object):
    poem = ''
    
    def __init__(self, task_num, address):
        self.task_num = task_num
        self.address = address
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.sock.connect(address)
        except socket.error as e:
            print "that failed."
            print e.message, e.args
        else:
            self.sock.setblocking(0)
        # tell the Twisted reactor to monitor this socket for reading
        from twisted.internet import reactor
        reactor.addReader(self)
    
    def fileno(self):
        try:
            return self.sock.fileno()
        except socket.error:
            return -1
    
    def connectionLost(self, reason):
        self.sock.close()
        # stop monitoring this socket
        from twisted.internet import reactor
        reactor.removeReader(self)
        # see if there are any poetry sockets left
        for reader in reactor.getReaders():
            if isinstance(reader, PoetrySocket):
                return
        try:
            reactor.stop() # no more poetry
        except twisted.internet.error.ReactorNotRunning as e:
            print e.message, e.args

    
    def doRead(self):
        bytes = ''
        while True:
            try:
                bytesread = self.sock.recv(1024)
                if not bytesread:
                    break
                else:
                    bytes += bytesread
            except socket.error, e:
                if e.args[0] == errno.EWOULDBLOCK:
                    break
                return main.CONNECTION_LOST
        if not bytes:
            print 'Task %d finished' % self.task_num
            return main.CONNECTION_DONE
        else:
            msg = 'Task %d: got %d bytes of poetry from %s'
            print  msg % (self.task_num, len(bytes), self.format_addr())
        self.poem += bytes
    
    def logPrefix(self):
        return 'poetry'
    
    def format_addr(self):
        host, port = self.address
        return '%s:%s' % (host or '127.0.0.1', port)

if __name__ == '__main__':
    poetry_main([10000,10001,10002])