

###Things to improve from the last part of the tutorial

* stop interfacing with low level stuff. 
* start using some twisted style error handling.
* increase reusability. 

**A Twisted abstraction is usually defined by an Interface 
specifying how an object embodying that abstraction should 
behave.**

##Most higher-level abstractions in Twisted are built by using lower-level ones, not by replacing them.
> if some earlier abstraction A implements feature F, then F 
> is probably not implemented by any other abstraction. 
> Rather, if another abstraction B needs feature F, it will 
> use A rather than implement F itself.  (In general, an 
> implementation of B will either sub-class an implementation 
> of A or refer to another object that implements A).

> When you choose to use Twisted you are also choosing to 
> use the Reactor Pattern, and that means programming in the 
> “reactive style” using callbacks and cooperative 
> multi-tasking. If you want to use Twisted correctly, you 
> have to keep the reactor’s existence (and the way it 
> works) in mind.

##Transports, Protocols, and Protocol Factories, oh MY!

* transports
    * defined by ITransport from the main interfaces module
    * represents a single connection that can xmit data
    * supports I/O with
        * TCP connections
        * UNIX Pipes
        * UDP sockets
        * other
    * Transport abstraction represents connections and 
    handles async I/O for any connection it represents
    * tport does not receive data, it reads from connections 
    and returns the data in callbacks
    * writing waits until it is not blocking
* protocols
    * defined by IProtocol in the same interfaces module
    * represents a protocol
    * each protocol object provides for one specific connection
        * each connection that needs to be made needs an 
        instance of a protocol
        * great place to store stateful protocols and partial data
* protocol factories
    * provides instances of protocols 
    * defined by IProtocolFactory

