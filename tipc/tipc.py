import socket
import sys
import os
import thread
import time

TYPE= 89988
sock = 0

def rcv_thread(sock, callback):
    while 1:
        try:
            msg = sock.recv(66000)
        except socket.error as err:
            print 'TIPC recv error: ' + str(msg[0]) + ' : ' + msg[1]
        callback(msg)

def setup(callback):
    global sock
    pid = os.getpid()
    try:
        sock = socket.socket(socket.AF_TIPC, socket.SOCK_RDM)
    except socket.error as msg:
        print 'Failed to create TIPC socket: ' + str(msg[0]) + ' : ' + msg[1]
        sys.exit()
    try:
        sock.bind((socket.TIPC_ADDR_NAME ,TYPE, pid, 0))
    except socket.error as msg:
        print 'Failed to bind TIPC socket: ' + str(msg[0]) + ' : ' + msg[1]
        sys.exit()
    try:
        thread.start_new_thread(rcv_thread, (sock,callback))
    except thread.error as msg:
        print 'Failed to start receive thread' + str(msg[0]) + ' : ' + msg[1]
        sys.exit()


def send(msg, pid):
    global sock
    try:
        sock.sendto(msg, (socket.TIPC_ADDR_NAME, TYPE, pid, 0))
    except socket.error as err:
        print 'Failed to send message: ' + str(err[0]) + ' : ' + err[1]

def sendall(msg):
    global sock
    try:
        sock.sendto(msg, (socket.TIPC_ADDR_NAMESEQ, TYPE, 0, ~0))
    except socket.error as err:
        print 'Failed to send message: ' + str(err[0]) + ' : ' + err[1]



