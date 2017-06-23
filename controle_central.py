import sys
from socket import socket, AF_INET, SOCK_DGRAM

from threading import Thread


def mandando():
	SERVER_IP   = '192.168.43.208'
	PORT_NUMBER = 5009
	SIZE = 1024
	print ("Test client sending packets to IP {0}, via port {1}\n".format(SERVER_IP, PORT_NUMBER))
	mySocket = socket( AF_INET, SOCK_DGRAM )

	print 'ok'
	while True:
		mySocket.sendto('inicie_ataque',(SERVER_IP,PORT_NUMBER))


mandando1 =Thread(target=mandando)

mandando1.start()

