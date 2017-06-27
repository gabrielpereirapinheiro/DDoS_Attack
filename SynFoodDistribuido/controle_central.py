import sys
from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread

#Funcao que manda o comando
def mandando():

	#Mostra na tela
	print 'Enviando mensasa22sagem para todos na rede !'

	#Variavel auxiliar para enviar a todos na rede
	i = 2

	while(i<255):

		#Define o IP que vai enviar o ataque
		SERVER_IP   = '192.168.43.'+str(i)

		#Proximo endereco
		i=i+1

		#Porta do Ataque
		PORT_NUMBER = 13000

		#Buffer
		SIZE = 1024

		#Socket criado
		mySocket = socket( AF_INET, SOCK_DGRAM )

		#Enviando a mensagem comece
		mySocket.sendto('inicie_ataque',(SERVER_IP,PORT_NUMBER))

	x = 1;

	while (x!=0):
		x = input('\nDigite 0 para parar o ataque :')

	print '\nEnviando mensagens para parar o ataque'
		
	i = 1
	
	while (i<255):
		#Define o IP que vai enviar o ataque
		SERVER_IP   = '192.168.1.'+str(i)

		#Proximo endereco
		i=i+1

		#Enviando a mensagem comece
		mySocket.sendto('pare_ataque',(SERVER_IP,PORT_NUMBER))
	print '\nMensagens enviadas !'
				


mandando()