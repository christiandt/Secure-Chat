import socket, select, sys, json


TCP_IP = socket.gethostbyname(socket.gethostname())
TCP_PORT = 5000
BUFFER_SIZE = 1024


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((TCP_IP, TCP_PORT))
server.listen(5)

connections = []
connections.append(server)
users = dict()
socketIP = dict()


print "Server started on "+TCP_IP

while 1:
	# Check if there are any readable sockets
	try:
		readable_sockets,writeable_sockets,error_sockets = select.select(connections,[],[])
	except:
		print "Server killed"
		sys.exit(0)

	for s in readable_sockets:

		if s == server:
			connection, address = server.accept()
			print "connection from "+str(address)
			socketIP[connection] = address[0]
			connections.append(connection)
			
		else:
			try:
				receivedData = s.recv(BUFFER_SIZE)
				if receivedData[0:7] == "REMOVE:":
					try:
						del users[receivedData[7:]]
					except:
						None
				else:
					if not "GET" in receivedData:
						users[receivedData] = socketIP[s]
					s.send(json.dumps(users))
			except:
				print "error receiving data"
			connections.remove(s)
			s.close()
			