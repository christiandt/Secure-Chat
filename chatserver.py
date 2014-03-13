import socket, select, sys, ssl, os.path
from PyQt4 import QtCore
from message import Message
from OpenSSL import crypto

class ChatServer(QtCore.QThread):

	def __init__(self, ciphers):
		QtCore.QThread.__init__(self)
		self.ciphers = ciphers
		self.IP = socket.gethostbyname(socket.gethostname())
		self.TCP_PORT = 5005
		self.BUFFER_SIZE = 1024
		self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.running=False
		self.serversocket.bind((self.IP, self.TCP_PORT))
		self.serversocket.listen(5)

		self.generate_certificate()

		self.connections = []
		self.connections.append(self.serversocket)


	def generate_certificate(self):
		certificate_file_name = "cert.pem"
		key_file_name = "key.key"
		
		if os.path.isfile(certificate_file_name) and os.path.isfile(key_file_name):
			return
		else:
			key = crypto.PKey()
			key.generate_key(crypto.TYPE_RSA, 1024)

			certificate = crypto.X509()

			certificate.get_subject().C = "US"
			certificate.get_subject().ST = "CA"
			certificate.get_subject().L = "IV"
			certificate.get_subject().O = "UCSB"
			certificate.get_subject().OU = "UCSB"
			certificate.get_subject().CN = self.IP

			certificate.gmtime_adj_notBefore(0)
			certificate.gmtime_adj_notAfter(365*24*60*60)

			certificate.set_issuer(certificate.get_subject())
			certificate.set_pubkey(key)
			certificate.sign(key, 'sha1')

			certificate_file = open(certificate_file_name, "wt")
			certificate_file.write(crypto.dump_certificate(crypto.FILETYPE_PEM, certificate))
			certificate_file.close()

			key_file = open(key_file_name, "wt")
			key_file.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, key))
			key_file.close()


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
					sslconnection = ssl.wrap_socket(connection,
								server_side=True,
								certfile="cert.pem",
								keyfile="key.key",
								ssl_version=ssl.PROTOCOL_TLSv1,
								ciphers=self.ciphers)
					self.connections.append(sslconnection)
					print sslconnection.cipher()
					print "connection added"

				else:
					try:
						print "message received"
						data = s.recv(self.BUFFER_SIZE)
						if data == "":
							s.close()
							connections.remove(s)
						self.emit(QtCore.SIGNAL('update(QString)'), data)
					except:
						print "error data..."
						break
					
					
			
	def end(self):
		self.running = False
		print "Shutting down"
		for conn in self.connections:
			conn.close()
		self.serversocket.close()
		sys.exit(0)