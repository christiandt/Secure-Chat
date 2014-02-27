from datetime import datetime
import json

class Message():

	def __init__(self, user="", message=""):
		self.time = str(datetime.now().time())[:-7]
		self.date = str(datetime.now().date())
		self.user = str(user)
		self.message = str(message)


	def getTime(self):
		return self.time

	def getDate(self):
		return self.date

	def getUser(self):
		return self.user

	def getMessage(self):
		return self.message

	def toJson(self):
		messageJson = {'time':self.time, 'date':self.date, 'user':self.user, 'message':self.message}
		return json.dumps(messageJson)

	def fromJson(self, messageJson):
		try:
			messageDict = json.loads(messageJson)
			self.time = messageDict['time']
			self.date = messageDict['date']
			self.user = messageDict['user']
			self.message = messageDict['message']
			return True
		except:
			False