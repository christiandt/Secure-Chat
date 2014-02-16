from PyQt4 import QtCore, QtGui



class Chat(QtGui.QDialog):

    def __init__(self, user, ip):
        super(Chat, self).__init__()
        self.setWindowTitle("Chat with "+str(user))
        self.resize(500, 50)

        self.layout = QtGui.QGridLayout(self)

        userLabel = QtGui.QLabel("Username: "+user)
        self.layout.addWidget(userLabel, 0, 0)

        ipLabel = QtGui.QLabel("IP: "+ip)
        self.layout.addWidget(ipLabel, 1, 0)


        self.setLayout(self.layout)
        self.show()