import socket
from message import Message

class ChatClient():

	def __init__(self):
		self.userSockets = dict()
		self.port = 5005

	def updateSockets(self, socket, data):
		message = Message()
		message.fromJson(str(data))
		user = message.getUser()
		if user not in self.userSockets:
			self.userSockets[user] = socket

	def sendMessage(self, message):
		user = message.getUser()
		if user in self.userSockets:
			socket = self.userSockets[user]
			try:
				socket.send(message.toJson())
			except:
				print "could not send message"

	def connect(self, user, ip):
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		try:
			client.connect((str(ip), self.port))
			self.userSockets[str(user)] = client
		except:
			print "could not connect to user"