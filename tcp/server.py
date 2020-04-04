from socket import *
from time import ctime

HOST = ''
PORT = 2011
BUFSIZE = 1025
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
try:
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
            recv_msg = data.decode('utf8')
            ret_msg = '[{}] {}'.format(ctime(), recv_msg)
            print('recv: {}'.format(recv_msg))
            print('ret: {}'.format(ret_msg))
            tcpCliSock.send(bytes(ret_msg, 'utf8'))
        tcpCliSock.close()
finally:
    tcpSerSock.close()
