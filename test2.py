# py1
#-*- encoding:utf-8 -*-
#客户端
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',65534))
print(s.recv(1024).decode('utf-8'))

for data in [b'1',b'2',b'3']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
