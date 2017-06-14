import socket
import time


def countdown(t):
    while t >= 1:
        print "Iniciando Server em " + str(t) + '...'
        time.sleep(1)
        t -= 1
    print('Server Running! \n')


# create a raw socket and bind it to the public interface
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

HOST = '192.168.0.15'
s.bind(('', 0))



countdown(3)

i = 0




while 1:
	msg = s.recvfrom(12000)
	if msg:
		i = i+1
		print str(i) + " Syn Packets Received! \n"


