import socket
from message import Message

class ChatClient():

	def __init__(self):
		self.userSockets = dict()
		self.port = 5005

	def updateSockets(self, socket, data):
		print "socket updated"
		message = Message()
		message.fromJson(str(data))
		user = message.getUser()
		self.userSockets[user] = socket

	def sendMessage(self, contact, message):
		print "sending message to "+contact
		if contact in self.userSockets:
			socket = self.userSockets[contact]
			try:
				socket.send(message.toJson())
			except:
				print "could not send message"

	def connect(self, contact, ip):
		print "connecting to contact "+str(contact)+" ip "+str(ip)
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		try:
			client.connect((str(ip), self.port))
			self.userSockets[str(contact)] = client
		except:
			print "could not connect to contact"