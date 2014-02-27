from PyQt4 import QtCore, QtGui
from chatserver import ChatServer
from message import Message



class Chat(QtGui.QDialog):

    def receiveMessage(self, message):
        self.chatLog.append(message)
        self.refreshChatMessages()

    def sendMessage(self):
        text = self.messageText.text()
        message = Message(self.username, text)
        self.chatLog.append(message)
        self.refreshChatMessages()
        self.chatserver.sendMessage(self.contact, message)

        #self.chatsocket.send(message.toJson())
        #data = self.chatsocket.recv(1024)
        #msg = Message()
        #msg.fromJson(data)
        #self.receiveMessage(msg)
        #self.communication.sendMessage(message)

    def refreshChatMessages(self):
        html = ""
        print self.chatLog
        self.messageText.clear()
        for post in self.chatLog:
            print post.getUser()
            print self.username
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

    def __init__(self, username, contact, server):
        super(Chat, self).__init__()
        #self.communication = Communication(self, ip)
        print "un: "+username
        print "con: "+contact
        self.chatLog = []
        self.username = username
        self.contact = contact
        self.chatserver = server
        self.setWindowTitle("Chat with "+str(contact))
        self.resize(600, 400)

        self.layout = QtGui.QGridLayout(self)

        #userLabel = QtGui.QLabel("Username: "+user)
        #self.layout.addWidget(userLabel, 0, 0)

        #ipLabel = QtGui.QLabel("IP: "+ip)
        #self.layout.addWidget(ipLabel, 1, 0)



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
        QtCore.QObject.connect(self.sendButton, QtCore.SIGNAL("clicked()"), self.sendMessage)

        self.layout.addWidget(self.sendButton, 1, 1)

        #messageText
        self.messageText = QtGui.QLineEdit(self)
        self.layout.addWidget(self.messageText, 1, 0)


        self.setLayout(self.layout)
        self.show()