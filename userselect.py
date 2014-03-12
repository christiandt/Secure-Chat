import sys
from PyQt4 import QtCore, QtGui
from nameclient import NameClient
from chat import Chat
from chatserver import ChatServer
from message import Message


class UserSelect(QtGui.QDialog):

    def chatStarted(self):
        clickedItem = self.list.currentItem()
        if clickedItem != None:
            user = str(self.list.currentItem().text())
            ip = self.userList[user]
            if ip != None:
                chat = Chat(self.username, user, ip)
                self.chats[user] = chat
        #self.accept()

    def receivedMessage(self, data):
        message = Message()
        message.fromJson(str(data))
        user = message.getUser()
        if user in self.chats:
            chat = self.chats[user]
            chat.receiveMessage(message)
        else:
            self.refreshUsers()
            ip = self.userList[user]
            chat = Chat(self.username, user, ip)
            self.chats[user] = chat
            chat.receiveMessage(message)

    def getUsers(self):
        client = NameClient()
        if(client.connect()):
            client.sendUsername(self.username)
            return client.receiveUserList()
        else:
            return {'Server error':None}

    def refreshUsers(self):
        self.userList = self.getUsers()
        users = list(self.userList)
        self.list.clear()
        self.list.addItems(users)

    def quitProgram(self):
        self.chatserver.end()
        sys.exit(0)


    def __init__(self, username, ciphers):
        super(UserSelect, self).__init__()
        self.username = username

        self.chatserver = ChatServer(ciphers)
        self.connect( self.chatserver, QtCore.SIGNAL("update(QString)"), self.receivedMessage )
        #self.chatserver.daemon = True
        self.chatserver.start()

        
        self.chats = dict()
        title = "Users"
        self.setWindowTitle(str(title))
        self.resize(300,400)

        self.layout = QtGui.QGridLayout(self)

        #listWidget
        self.list = QtGui.QListWidget()
        self.userList = self.getUsers()
        users = list(self.userList)
        self.list.addItems(users)
        self.layout.addWidget(self.list, 0, 0, 1, 3)

        #selectbutton
        self.selectbutton = QtGui.QPushButton(self)
        self.selectbutton.setText("Select")
        self.selectbutton.setMinimumWidth(20)
        self.selectbutton.setMinimumHeight(50)
        self.layout.addWidget(self.selectbutton, 1, 0)
        QtCore.QObject.connect(self.selectbutton, QtCore.SIGNAL("clicked()"), self.chatStarted)

        #refreshbutton
        self.refreshbutton = QtGui.QPushButton(self)
        self.refreshbutton.setText("Refresh")
        self.refreshbutton.setMinimumWidth(20)
        self.refreshbutton.setMinimumHeight(50)
        self.layout.addWidget(self.refreshbutton, 1, 1)
        QtCore.QObject.connect(self.refreshbutton, QtCore.SIGNAL("clicked()"), self.refreshUsers)

        #cancelbutton
        self.cancelbutton = QtGui.QPushButton(self)
        self.cancelbutton.setText("Log out")
        self.cancelbutton.setMinimumWidth(5)
        self.cancelbutton.setMinimumHeight(50)
        self.layout.addWidget(self.cancelbutton, 1, 2)
        QtCore.QObject.connect(self.cancelbutton, QtCore.SIGNAL("clicked()"), self.quitProgram)

        self.setLayout(self.layout)
        self.show()
