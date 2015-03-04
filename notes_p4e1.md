#Notes about part 4 exercise 1

###From [this comment](http://krondo.com/?p=1445&cpage=1#comment-8480)
*while this is not the solution I chose it seems like it would work.*

    def __init__(self, task_num, address):
        self.task_num = task_num
        self.address = address
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if self.sock.connect_ex(address) == 0:
            self.sock.setblocking(0)
            reactor.addReader(self)
        else:
            print ‘Could not connect to Task’, task_num