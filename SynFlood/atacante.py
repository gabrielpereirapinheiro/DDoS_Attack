from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_DGRAM)
hostName = gethostbyname('0.0.0.0')
serverSocket.bind((hostName,serverPort))
print 'The server is ready to receive'
while 1:
     
     sentence, addr = serverSocket.recvfrom(1024)
     print 'From Client: ', sentence
     


serverSocket.close()
