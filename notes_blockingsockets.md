#blocking vs non-blocking sockets
*from http://www.scottklement.com/rpg/socktut/nonblocking.html*

> When you issue a call to connect(), your program doesn't regain control until either the connection is made, or an error occurs.
> 
> The solution to this problem is called "non-blocking sockets".
> 
> By default, TCP sockets are in "blocking" mode. For example, when you call recv() to read from a stream, control isn't returned to your program until at least one byte of data is read from the remote site. This process of waiting for data to appear is referred to as "blocking"
> 
> Its possible to set a descriptor so that it is placed in "non-blocking" mode. When placed in non-blocking mode, you never wait for an operation to complete.


