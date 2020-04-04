from socket import *

HOST = ''
PORT = 2011
BUFSIZE = 1025
ADDR = (HOST, PORT)


with socket(AF_INET, SOCK_STREAM) as tcpCliSock:
    print('before connecting')
    tcpCliSock.connect(ADDR)
    print('after connecting')
    print('peer name: {}'.format(tcpCliSock.getpeername()))
    print('socket name: {}'.format(tcpCliSock.getsockname()))
    # check_port(tcpCliSock)
    while True:
        data = input('> ')
        if not data:
            break
        tcpCliSock.send(bytes(data, 'utf8'))
        print('after sending')
        print('peer name: {}'.format(tcpCliSock.getpeername()))
        print('socket name: {}'.format(tcpCliSock.getsockname()))
        data = tcpCliSock.recv(BUFSIZE)
        print('after recving')
        print('peer name: {}'.format(tcpCliSock.getpeername()))
        print('socket name: {}'.format(tcpCliSock.getsockname()))
        if not data:
            break
        print(data.decode('utf8'))
    tcpCliSock.close()
