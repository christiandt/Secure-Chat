import socket, select, sys
from PyQt4 import QtCore
from message import Message

class ChatServer(QtCore.QThread):

	def __init__(self, username):
		QtCore.QThread.__init__(self)
		self.username = username
		self.IP = socket.gethostbyname(socket.gethostname())
		self.TCP_PORT = 5005
		self.BUFFER_SIZE = 1024
		self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.IP = socket.gethostbyname(socket.gethostname())
		self.running=False
		self.serversocket.bind((self.IP, self.TCP_PORT))
		self.serversocket.listen(5)

		self.connections = []
		self.connections.append(self.serversocket)

		self.userSockets = dict()

	def getUser(self, data):
		message = Message()
		message.fromJson(str(data))
		return message.getUser()

	def sendMessage(self, contact, message):
		print "sending message to "+contact
		if contact in self.userSockets:
			socket = self.userSockets[contact]
			try:
				print "sending"
				socket.send(message.toJson())
				print "sent"
			except:
				print "could not send message"
		else:
			print "could not find user "+str(contact)

	def connect(self, contact, ip):
		print "connecting to contact "+str(contact)+" ip "+str(ip)
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		#try:
		client.connect((str(ip), self.TCP_PORT))
		self.userSockets[str(contact)] = client
		#except:
		#	print "could not connect to contact"


	def run(self):
		self.running = True
		while self.running:
			print "running server"
			try:
				readable_sockets,writeable_sockets,error_sockets = select.select(self.connections,[],[])
			except:
				print "hmmm...."
				break
			for s in readable_sockets:
				if s == self.serversocket:
					connection, address = self.serversocket.accept()
					self.connections.append(connection)
					print "connection added"

				else:
					try:
						print "message received"
						data = s.recv(self.BUFFER_SIZE)
						user = getUser(data)
						self.emit(QtCore.SIGNAL('update(QString)'), data)
						self.userSockets[user] = s
						#s.send(msg.toJson())
					except:
						print "error data..."
						break
					
					
			
	def end(self):
		self.running = False
		for conn in self.connections:
			conn.close()
		self.serversocket.close()