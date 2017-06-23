import sys
from threading import Thread




def escutando():
	from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
	PORT_NUMBER = 5009
	SIZE = 1024
	hostName = gethostbyname( '0.0.0.0' )
	mySocket = socket( AF_INET, SOCK_DGRAM )
	mySocket.bind( (hostName, PORT_NUMBER) )

	print 'Escutando',PORT_NUMBER
	
	while True:
	    (data,addr) = mySocket.recvfrom(SIZE)
            print data


escutando1 = Thread(target=escutando)

escutando1.start()

