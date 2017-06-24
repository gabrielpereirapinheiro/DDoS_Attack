import sys
from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread

#Funcao que manda o comando
def mandando():

	#Define o IP que vai enviar o ataque
	SERVER_IP   = '192.168.43.165'

	PORT_NUMBER = 13005
	SIZE = 1024
	print ("Enviando para o IP {0} na porta {1}\n".format(SERVER_IP, PORT_NUMBER))
	mySocket = socket( AF_INET, SOCK_DGRAM )

	mySocket.sendto('pare_ataque',(SERVER_IP,PORT_NUMBER))



#Thread que ira inicar o ataque
mandando1 =Thread(target=mandando)

#Comeca o ataque
mandando1.start()

