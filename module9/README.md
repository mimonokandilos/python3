# MODULE 9:


## output so far:
TCP server started at 127.0.0.1:12345
TCP client connected to server 127.0.0.1:12345
Client connection successfully closed
.UDP server started at 127.0.0.1:12345
UDP client created
Client connection successfully closed
./usr/local/Cellar/python@3.10/3.10.9/Frameworks/Python.framework/Versions/3.10/lib/python3.10/threading.py:953: ResourceWarning: unclosed <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 12345), raddr=('127.0.0.1', 50255)>
  self._target(*self._args, **self._kwargs)
ResourceWarning: Enable tracemalloc to get the object allocation traceback
Client connection successfully closed
EServer socket closed

======================================================================
ERROR: test_get_local_ip (__main__.TestNetworkingOperations)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/mikemonokandilos/python/module9/test_module9.py", line 39, in test_get_local_ip
    local_ip = get_local_ip()
  File "/Users/mikemonokandilos/python/module9/networking_operations.py", line 6, in get_local_ip
    return socket.gethostbyname(socket.gethostname())
socket.gaierror: [Errno 8] nodename nor servname provided, or not known

----------------------------------------------------------------------
Ran 3 tests in 5.121s

FAILED (errors=1)
