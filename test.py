import sys
import os
from tipc import tipc
import time


#This will be invoked whenever someone sends us a message
def callback(msg):
    print msg

tipc.setup(callback)

tipc.send("Hello unicast", os.getpid())
tipc.sendall("Hello multicast")
time.sleep(1)
sys.exit()
