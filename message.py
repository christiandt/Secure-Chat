from datetime import datetime

class Message():

	def __init__(self, user, message):
		self.time = datetime.now()
		self.user = user
		self.message = message


	def getTime(self):
		return self.time

	def getUser(self):
		return self.user

	def getMessage(self):
		return self.message