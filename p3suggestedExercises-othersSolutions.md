#Solutions from other people, most likely from the comments of the actual post

The solutions from [plover](http://krondo.com/?p=1333&cpage=1#comment-20924)
really helped me learn a couple of new things.

The logic of the solution is very much how I imagined it, but
they showed some of the following functions that I didn't know

Their [solution to number one](http://pastebin.com/uGjv6Fnh) can be seen there.

* time.time()-self.startTime - I always fight with figuring time.  I really
liked their solution with this.
* self.pool = [Countdown(name, ticks, rate) for name, ticks, rate in args]
-- this is one of those things that I **know**, but referencing how
to pass and access *args is super handy.  If I would have had to look it up, I 
would not have used it.
* I am still not 100% sure about how they are doing "".format,
I need to look at that wrt my use of "%s"%(string)

Incase something happens to pastebin:

    # A solution to exercise 1 of the Twisted tutorial at http://krondo.com/?p=1333
    
    import time
    
    class Countdown(object):
    
        def __init__(self, name, ticks, rate):
            self.name, self.counter, self.rate = (name, ticks, rate)
    
        def count(self):
                print '{}: {:>2} ticks left at {} sec/tick ...'.format(self.name, self.counter, self.rate)
                self.counter -= 1
    
    class CountdownPool(object):
    
        def __init__(self, *args):
            self.pool = [Countdown(name, ticks, rate) for name, ticks, rate in args]
            self.pending = len(self.pool)
    
        def start(self):
            self.startTime = time.time()
            for ctdn in self.pool:
                self.count(ctdn)
    
        def count(self, ctdn):
            if ctdn.counter > 0:
                ctdn.count()
                reactor.callLater(ctdn.rate, self.count, ctdn)
            else:
                print 'Counter {} complete! ({:.3f} sec)'.format(ctdn.name, time.time()-self.startTime)
                self.pending -= 1
                if not self.pending: reactor.stop()
    
    
                
    from twisted.internet import reactor
    
    pool = CountdownPool(['one', 5, 1.0], ['two', 13, .3], ['tri', 8, .8])
    reactor.callWhenRunning(pool.start)
     
    print 'Start!'
    reactor.run()
    print 'Stop!'
