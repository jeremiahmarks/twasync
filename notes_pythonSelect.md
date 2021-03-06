#Python select module

###select.select
*from https://docs.python.org/2/library/select.html#select.select*

>  select.select(rlist, wlist, xlist[, timeout])
> 
>     This is a straightforward interface to the Unix select() system call. The first three arguments are sequences of ‘waitable objects’: either integers representing file descriptors or objects with a parameterless method named fileno() returning such an integer:
> 
>         rlist: wait until ready for reading
>         wlist: wait until ready for writing
>         xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
> 
>     Empty sequences are allowed, but acceptance of three empty sequences is platform-dependent. (It is known to work on Unix but not on Windows.) The optional timeout argument specifies a time-out as a floating point number in seconds. When the timeout argument is omitted the function blocks until at least one file descriptor is ready. A time-out value of zero specifies a poll and never blocks.
> 
>     The return value is a triple of lists of objects that are ready: subsets of the first three arguments. When the time-out is reached without a file descriptor becoming ready, three empty lists are returned.
> 
>     Among the acceptable object types in the sequences are Python file objects (e.g. sys.stdin, or objects returned by open() or os.popen()), socket objects returned by socket.socket(). You may also define a wrapper class yourself, as long as it has an appropriate fileno() method (that really returns a file descriptor, not just a random integer).

