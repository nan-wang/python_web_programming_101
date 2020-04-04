from socket import *
from time import ctime

HOST = ''
PORT = 2011
BUFSIZE = 1025
ADDR = (HOST, PORT)

with socket(AF_INET, SOCK_STREAM) as tcpSerSock:
    tcpSerSock.bind(ADDR)
    tcpSerSock.listen(5)

    while True:
        print('waiting for connection...')
        tcpCliSock, addr = tcpSerSock.accept()
        print('...connected from: {}'.format(addr))

        while True:
            data = tcpCliSock.recv(BUFSIZE)
            if not data:
                break
            tcpCliSock.send(
                bytes('[{}] {}'.format(ctime(), data.decode('utf8')), 'utf8'))
        tcpCliSock.close()
