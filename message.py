from datetime import datetime
import json

class Message():

	def __init__(self, user, message):
		self.time = datetime.now()
		self.user = user
		self.message = message


	def getTime(self):
		return str(self.time.time())[:-7]

	def getDate(self):
		return str(self.time.date())

	def getUser(self):
		return self.user

	def getMessage(self):
		return self.message

	def toJson(self):
		messageJson = {'time':self.time, 'user':self.user, 'message':self.message}
		return json.dumps(messageJson)

	def fromJson(self, messageJson):
		try:
			messageDict = json.loads(messageJson)
			self.time = messageDict['time']
			self.user = messageDict['user']
			self.message = messageDict['message']
			return True
		except:
			False