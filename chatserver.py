import socket, select, sys
from PyQt4 import QtCore
from message import Message

class ChatServer(QtCore.QThread):

	def __init__(self):
		QtCore.QThread.__init__(self)
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
						self.emit(QtCore.SIGNAL('update(QString)'), data)
						#s.send(msg.toJson())
					except:
						print "error data..."
						break
					
					
			
	def end(self):
		self.running = False
		for conn in self.connections:
			conn.close()
		self.serversocket.close()