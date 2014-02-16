
from PyQt4 import QtCore, QtGui
import sys
from nameclient import NameClient
from chat import Chat


class userSelect(QtGui.QDialog):

    def userChanged(self, item):
        self.user = item

    def chatStarted(self):
        user = self.list.currentItem().text()
        ip = self.userList[str(user)]
        if ip != None:
            self.chat = Chat(user, ip)
        #self.accept()

    def getUsers(self):
        client = NameClient()
        if(client.connect()):
            client.sendUsername(self.username)
            return client.receiveUserList()
        else:
            return {'Server error':None}

    def quitProgram(self):
        sys.exit(0)

    def __init__(self, username):
        super(userSelect, self).__init__()
        self.username = username
        title = "Users"
        self.setWindowTitle(str(title))
        self.resize(300,400)

        self.layout = QtGui.QGridLayout(self)

        #listWidget
        self.list = QtGui.QListWidget()
        self.userList = self.getUsers()
        users = list(self.userList)
        self.list.addItems(users)
        self.layout.addWidget(self.list, 0, 0, 1, 2)

        #selectbutton
        self.selectbutton = QtGui.QPushButton(self)
        self.selectbutton.setText("Select")
        self.selectbutton.setMinimumWidth(20)
        self.selectbutton.setMinimumHeight(50)
        self.layout.addWidget(self.selectbutton, 1, 0)
        QtCore.QObject.connect(self.selectbutton, QtCore.SIGNAL("clicked()"), self.chatStarted)


        #cancelbutton
        self.cancelbutton = QtGui.QPushButton(self)
        self.cancelbutton.setText("Cancel")
        self.cancelbutton.setMinimumWidth(5)
        self.cancelbutton.setMinimumHeight(50)
        self.layout.addWidget(self.cancelbutton, 1, 1)
        QtCore.QObject.connect(self.cancelbutton, QtCore.SIGNAL("clicked()"), self.quitProgram)

        self.setLayout(self.layout)
        self.show()
