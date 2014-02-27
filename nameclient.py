import socket, json, sys


class NameClient():

	def __init__(self):
		self.server = None
		self.CLIENT_TCP_IP = socket.gethostbyname(socket.gethostname())
		self.SERVER_TCP_IP = '10.0.0.9'
		self.SERVER_TCP_PORT = 5000
		self.BUFFER_SIZE = 1024


	def connect(self):
		global server
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			self.server.connect((self.SERVER_TCP_IP, self.SERVER_TCP_PORT))
			self.server.settimeout(3)
			return True
		except:
			return False
		
	def sendUsername(self, username):
		try:
			self.server.send(username)
		except:
			print "Could not send message, disconnecting"

	def receiveUserList(self):
		userList = dict()
		try:
			data = self.server.recv(self.BUFFER_SIZE)
			self.server.close()
			try:
				userList = dict(json.loads(data))
			except:
				#bad data
				None
		except socket.timeout:
			#timed out
			None
		print userList
		return userList
