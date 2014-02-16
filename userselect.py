
from PyQt4 import QtCore, QtGui
import sys
from nameclient import NameClient

class userSelect(QtGui.QDialog):

    def userChanged(item):
        print item

    def getUsers(self):
        global userList
        client = NameClient()
        if(client.connect()):
            client.sendUsername("kine")
            return client.receiveUserList()
        else:
            None

    def quitProgram(self):
        sys.exit(0)

    def __init__(self):
        super(userSelect, self).__init__()
        title = "Users"
        self.setWindowTitle(str(title))
        self.resize(300,400)

        self.layout = QtGui.QGridLayout(self)

        #listView
        
        self.list = QtGui.QListView()
        model = QtGui.QStandardItemModel(self.list)
        self.userList = self.getUsers()
        users = list(self.userList)
        for user in users:
            item = QtGui.QStandardItem(user)
            item.setEditable(False)
            model.appendRow(item)
        self.list.setModel(model)
        model.itemChanged.connect(self.userChanged)
        self.layout.addWidget(self.list, 0, 0, 1, 2)

        #selectbutton
        self.selectbutton = QtGui.QPushButton(self)
        self.selectbutton.setText("Select")
        self.selectbutton.setMinimumWidth(20)
        self.selectbutton.setMinimumHeight(50)
        self.layout.addWidget(self.selectbutton, 1, 0)

        #cancelbutton
        self.cancelbutton = QtGui.QPushButton(self)
        self.cancelbutton.setText("Cancel")
        self.cancelbutton.setMinimumWidth(5)
        self.cancelbutton.setMinimumHeight(50)
        self.layout.addWidget(self.cancelbutton, 1, 1)
        QtCore.QObject.connect(self.cancelbutton, QtCore.SIGNAL("clicked()"), self.quitProgram)

        self.setLayout(self.layout)