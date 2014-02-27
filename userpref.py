from PyQt4 import QtCore, QtGui
from userselect import UserSelect

class UserPref(QtGui.QDialog):

    def __init__(self):
        super(UserPref, self).__init__()
        title = "Username"
        self.setWindowTitle(str(title))
        self.resize(500, 50)

        self.layout = QtGui.QGridLayout(self)


        #name input
        self.nameInput = QtGui.QLineEdit('', self)
        self.nameInput.setStyleSheet("font: 20pt")
        self.nameInput.setFixedHeight(30)
        self.layout.addWidget(self.nameInput, 1, 0)
        userLabel = QtGui.QLabel('Username:')
        self.layout.addWidget(userLabel, 0, 0)

        #OK buton
        self.okbutton = QtGui.QPushButton(self)
        self.okbutton.setText("OK")
        self.okbutton.setMinimumWidth(50)
        self.okbutton.setMinimumHeight(45)
        self.layout.addWidget(self.okbutton, 1, 1)
        QtCore.QObject.connect(self.okbutton, QtCore.SIGNAL("clicked()"), self.setUsername)

        self.setLayout(self.layout)

    def setUsername(self):
        username = str(self.nameInput.text())
        if username != "":
            self.userswindow = UserSelect(username)
            self.accept()