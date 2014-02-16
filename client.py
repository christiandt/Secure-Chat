import socket, json, sys

server = None
SERVER_TCP_IP = '10.0.0.9'
SERVER_TCP_PORT = 5005
BUFFER_SIZE = 1024


def connect():
	global server
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		server.connect((SERVER_TCP_IP, SERVER_TCP_PORT))
		server.settimeout(3)
		return True
	except:
		return False
	
def sendUsername(username):
	try:
		server.send(username)
	except:
		print "Could not send message, disconnecting"

def receiveUserList():
	userList = dict()
	try:
		data = server.recv(BUFFER_SIZE)
		server.close()
		try:
			userList = dict(json.loads(data))
		except:
			#bad data
			None
	except socket.timeout:
		#timed out
		None
	return userList


if(connect()):
	sendUsername("christian")
	usernames = receiveUserList()
	print usernames
else:
	print "could not reach server"