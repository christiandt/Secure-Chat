import socket, select, sys, json


PRIVATE_TCP_IP = socket.gethostbyname(socket.gethostname())
PUBLIC_TCP_IP = ""
TCP_PORT = 5005
BUFFER_SIZE = 1024


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((PRIVATE_TCP_IP, TCP_PORT))
server.listen(5)

connections = []
connections.append(server)
users = dict()

print "Server started on"+PRIVATE_TCP_IP

while 1:
	# Check if there are any readable sockets
	readable_sockets,writeable_sockets,error_sockets = select.select(connections,[],[])

	for s in readable_sockets:

		if s == server:
			connection, address = server.accept()
			connections.append(connection)
			
		else:
			try:
				receivedData = s.recv(BUFFER_SIZE)
				ip, port = s.getsockname()
				users[receivedData] = ip
				s.send(json.dumps(users))
				#print receivedData + " - " + ip
			except:
				print "error receiving data"
			connections.remove(s)
			s.close()
	
		