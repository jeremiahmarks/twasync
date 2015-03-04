from http://krondo.com/blog/?p=1445

###from [this comment](http://krondo.com/?p=1445&cpage=1#comment-2570)

> 1. Invoke your operation as you normally would. In this 
case that means creating the PoetrySocket objects.
> 2. Invoke callLater on another function whose job it is to 
cancel the first one, if the first one hasn’t already 
finished. What the second function actually does is going 
to be context-specific. For a PoetrySocket object, that 
probably means unregistering itself from the reactor and 
closing the raw socket. Does that make sense?

###from [this pastebin](http://pastebin.com/QSqnG0Wd)
*This is from [this comment](http://krondo.com/?p=1445&cpage=1#comment-7562),
the reply to this comment will get its own section*
**Later: holy cow, check out how they did the first exercise,
it is in the try/except section of poetry_main()**

    def cancelPoetryReading(sockets):
        for i, sock in enumerate(sockets):
            print "Timeout!"
            sock.connectionLost("Timeout occurred")
       
    def poetry_main():
        addresses = parse_args()
     
        start = datetime.datetime.now()
     
        try:
            sockets = [PoetrySocket(i + 1, addr) for i, addr in enumerate(addresses)]
            print "SOCKETS: ",sockets
        except socket.error:
            print 'Arr, there be a socket error. Methinks you tried to land on the wrong port.'
            return
     
        from twisted.internet import reactor
        reactor.callLater(3,cancelPoetryReading,sockets)
        reactor.run()
     
        elapsed = datetime.datetime.now() - start
     
        for i, sock in enumerate(sockets):
            print 'Task %d: %d bytes of poetry' % (i + 1, len(sock.poem))
     
        print 'Got %d poems in %s' % (len(addresses), elapsed)
     
     
    if __name__ == '__main__':
        poetry_main()

###[This is the reply](http://krondo.com/?p=1445&cpage=1#comment-7566) that I mentioned earlier.
*in response to the question "Why not use setTimeout on our sockets instead of using callLater?"*

> To answer your second question, the setTimeout socket method
> only makes sense for blocking sockets. It in effect declares that you are
> only willing to block while reading or writing to a socket for so long.
> 
> But in Twisted, or any other asynchronous I/O system, you never block on
> sockets. In effect, the socket timeout is always zero. Blocking on a socket
> would basically defeat the whole point of using asynchronous I/O which is
> to only service the ports which are not going to block. So to do things like
> timeouts on individual sockets, you need another mechanism.
> 
> By the wait, callLater does end up setting a timeout, but it’s
> on the select() (or poll(), etc.) call, not on
> individual sockets

