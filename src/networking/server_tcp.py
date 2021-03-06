'''
Created on 20.08.2014

@author: proSingularity
'''

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 60000))
s.listen(1)  # listen to only one connection
try:
    while True:
        comm, addr = s.accept()
        while True:
            data = comm.recv(1024)

            if not data:
                comm.close()
                break

            print("[%s] %s" % (addr[0], data.decode()))
            message = input("Answer: ").encode(encoding='utf_8',
                                               errors='strict')
            comm.send(message)
finally:
    s.close()
    