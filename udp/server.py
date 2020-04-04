from socket import *
from time import ctime

HOST = ''
PORT = 2011
BUFSIZE = 1025
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)

try:
    udpSerSock.bind(ADDR)
    while True:
        print('waiting for message...')
        data, addr = udpSerSock.recvfrom(BUFSIZE)
        recv_msg = data.decode('utf8')
        ret_msg = '[{}] {}'.format(ctime(), recv_msg)
        print('recv: {}'.format(recv_msg))
        print('ret: {}'.format(ret_msg))
        udpSerSock.sendto(bytes(ret_msg, 'utf8'), addr)
        print('...received from and returned to: {}'.format(addr))
finally:
    print('close server gracefully...')
    udpSerSock.close()

