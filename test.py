# py1
#-*-encoding:utf-8-*-
#服务器
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',65534))
s.listen(5)
print('waiting for connecting.....')

while True:
    sock,addr=s.accept()
    print('New connecting from %s :%d' %(addr[0],addr[1]))
    sock.send(b'Welcome!')
    while True:
        data=sock.recv(1024)
        if not data or data.decode('utf-8')=='exit':
            break
        sock.send(bytes('Hello %s' %data.decode('utf-8'),encoding='utf-8'))
    sock.close()
    print('Connecting from %s is over'%addr[0])
