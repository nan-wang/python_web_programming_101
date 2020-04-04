from socket import *

HOST = ''
PORT = 2011
BUFSIZE = 1025
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)
while True:
    data = input('> ')
    if not data:
        break
    udpCliSock.sendto(bytes(data, 'utf8'), ADDR)
    data, ADDR = udpCliSock.recvfrom(BUFSIZE)
    if not data:
        break
    print(data.decode('utf8'))

udpCliSock.close()
