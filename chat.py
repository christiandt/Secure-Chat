from PyQt4 import QtCore, QtGui
from message import Message



class Chat(QtGui.QDialog):


    def sendMessage(self):
        html = ""
        message = self.messageText.text()
        self.chatLog.append(Message(self.username, message))
        self.messageText.clear()
        for post in self.chatLog:
            if post.getUser() == self.username:
                html += '<div align="right">'
                html += post.getMessage()
                html += " ("
                html += post.getTime()
                html += ")"
            else:
                html += "<div>"
                html += "("
                html += str(post.getTime().time())[:-7]
                html += ") "
                html += post.getMessage()
            html += "</div>"
        self.chatText.setHtml(html)

    def __init__(self, username, contact, ip):
        super(Chat, self).__init__()
        self.chatLog = []
        self.username = username
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