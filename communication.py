from message import Message
from chat import Chat
import socket

class Communication():

	def __init__(self, chat):
		self.chat = chat
		None

	def sendMessage(self):
		None


	def receiveMessage(self, message):
		self.chat.receiveMessage(message)

