#!/usr/env/python

import time
import socket


""" 
The client will send a message to the server via UDP.  
The server will turn around and send a packet back to the client via UDP.
The client will measure the round trip time (RTT) and determine the average over 10 packets sent (as well as the loss rate, if any).

Note that the client must have a provision for a timeout, in case the sent packet is lost (or the server isn't working properly).

Gather your data using two different systems!
This means you shouldn't run the client and the server both on cs.student.plattsburgh.edu (except during testing.)
You can use a laptop, one of the lab machines, etc, as the "other” system.

The grade for this project will be determined as follows:

1/3 Correct functioning
1/3 Coding style (comments, neatness, performance)
1/3 A short write-up that explains the code (2 pages maximum, typed) that describes any difficulties that you had writing, running and debugging your program, and that cites all sources you used (textbooks, internet searches, etc).

Remember, comments tell why you are doing something, not what you are doing.
If the code is well written, what you are doing is self-evident.
The comments should explain your thinking.
Those comments are for the person who has to maintain your code in the future (and that may be you, years down the road!)

1) You need to watch your port usage. If you don't close a port when your program completes, that port will be "busy” for some amount of time (until the system frees it via a timeout.)
2) If you are logged on to one system (i.e. you're all on student.cs), you are all using the same pool of port numbers. "netstat -vaun” will display the used UDP ports on a system.

Resources:

https://docs.python.org/3.4/library/socket.html
On this page, pay particular attention to sections:

https://docs.python.org/3.4/library/socket.html#socket.socket
18.1.2.1. Exceptions
18.1.3. Socket Objects
"""

port = 6789

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.bind(('', port))

    while True:
        print('Waiting to receive message..')
        data, address = sock.recvfrom(4096)

        print('Received {} bytes from {}'.format(len(data), address))
        # print(data)

        if data:
            sent = sock.sendto(data, address)
            print('Sent {} bytes back to {}'.format(sent, address))
