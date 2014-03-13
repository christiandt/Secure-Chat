import socket, ssl, sys, errno
from PyQt4 import QtCore, QtGui
from chatserver import ChatServer
from message import Message
from error import Error



class Chat(QtGui.QDialog):

    def receiveMessage(self, message):
        self.chatLog.append(message)
        self.refreshChatMessages()

    def sendMessage(self, text):
        message = Message(self.username, text)
        self.chatLog.append(message)
        self.refreshChatMessages()
        try:
            self.sslSocket.send(message.toJson())
        except ssl.SSLError as e:
            self.error = Error(str(e))
        except socket.error as e:
            errorcode = e[0]
            if errorcode == errno.EPIPE:
                self.error = Error("Could not send message, user has probably logged out")
                try:
                    self.sslSocket.close()
                except:
                    None

    def connect(self, ip):
        #Changed resturn
        self.port = 5005
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sslSocket = ssl.wrap_socket(client, 
                        ssl_version=ssl.PROTOCOL_TLSv1,
                        ciphers=self.ciphers)
        self.sslSocket.settimeout(3)
        try:
            self.sslSocket.connect((ip, self.port))
            return True
        except socket.error as e:
            errorcode = e[0]
            if errorcode==errno.ECONNREFUSED:
                self.error = Error("Could not connect to "+ self.contact)
            else:
                messageError = "Error code " + e[0]
                self.error = Error(messageError)
            return False

    def clickedButton(self):
        text = self.messageText.text()
        self.sendMessage(text)

    def refreshChatMessages(self):
        html = ""
        #print self.chatLog
        self.messageText.clear()
        for post in self.chatLog:
            #print post.getUser()
            #print self.username
            if post.getUser() == self.username:
                html += '<div align="right">'
                html += post.getMessage()
                html += " ("
                html += post.getTime()
                html += ")"
            else:
                html += "<div>"
                html += "("
                html += post.getTime()
                html += ") "
                html += post.getMessage()
            html += "</div>"
        self.chatText.setHtml(html)

    def __init__(self, username, contact, ip, ciphers):
        super(Chat, self).__init__()
        print "un: "+username
        print "con: "+contact
        self.chatLog = []
        self.username = username
        self.contact = contact
        self.ciphers = ciphers
        self.setWindowTitle("Chat with "+str(contact))
        self.resize(600, 400)
        self.layout = QtGui.QGridLayout(self)
        
        if self.connect(ip):
            #Text
            self.scrollArea = QtGui.QScrollArea(self)
            self.scrollArea.setWidgetResizable(True)
            self.scrollAreaWidgetContents = QtGui.QWidget()
            self.scrollArea.setWidget(self.scrollAreaWidgetContents)
            self.chatText = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
            self.layout.addWidget(self.scrollArea, 0, 0, 1, 2)
            self.layout.addWidget(self.chatText, 0, 0, 1, 2)

            #SendButton
            self.sendButton = QtGui.QPushButton(self)
            self.sendButton.setText("Send")
            self.sendButton.setMinimumWidth(50)
            self.sendButton.setMinimumHeight(45)
            QtCore.QObject.connect(self.sendButton, QtCore.SIGNAL("clicked()"), self.clickedButton)

            self.layout.addWidget(self.sendButton, 1, 1)

            #messageText
            self.messageText = QtGui.QLineEdit(self)
            self.layout.addWidget(self.messageText, 1, 0)

            self.setLayout(self.layout)
            self.show()

        else:
            self.accept()
