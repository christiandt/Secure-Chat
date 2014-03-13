from PyQt4 import QtCore, QtGui
from userselect import UserSelect
from error import Error

class UserPref(QtGui.QDialog):

    def __init__(self):
        super(UserPref, self).__init__()
        title = "Preferences"
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
        QtCore.QObject.connect(self.okbutton, QtCore.SIGNAL("clicked()"), self.logOn)

        #Crypto group
        self.cryptoBoxes = []
        ciphers = ["CAMELLIA256-SHA", "AES256-SHA", "AES128-SHA", "DES-CBC3-SHA", "RC4-SHA"]

        self.cryptoGroup = QtGui.QGroupBox("Ciphers", self)
        self.cryptoGroup.setStyleSheet("font: 13pt")
        self.cryptoGroupLayout = QtGui.QGridLayout()
        allBox = QtGui.QCheckBox("ALL")
        allBox.setChecked(True)
        self.cryptoBoxes.append(allBox)
        self.cryptoGroupLayout.addWidget(allBox, 0, 0)
        highBox = QtGui.QCheckBox("HIGH")
        self.cryptoBoxes.append(highBox)
        self.cryptoGroupLayout.addWidget(highBox, 1, 0)
        mediumBox = QtGui.QCheckBox("MEDIUM")
        self.cryptoBoxes.append(mediumBox)
        self.cryptoGroupLayout.addWidget(mediumBox, 2, 0)
        lowBox = QtGui.QCheckBox("LOW")
        self.cryptoBoxes.append(lowBox)
        self.cryptoGroupLayout.addWidget(lowBox, 3, 0)
        for cipher in ciphers:
            cipherBox = QtGui.QCheckBox(cipher)
            self.cryptoBoxes.append(cipherBox)
            self.cryptoGroupLayout.addWidget(cipherBox, ciphers.index(cipher), 1)

        self.cryptoGroup.setLayout(self.cryptoGroupLayout)
        self.layout.addWidget(self.cryptoGroup, 2, 0, 1, 2)

        self.setLayout(self.layout)

    def logOn(self):
        username = str(self.nameInput.text())
        ciphersList = ""
        for checkBox in self.cryptoBoxes:
            if checkBox.isChecked():
                name = str(checkBox.text())
                ciphersList+=(name+":")
                #if name == "ALL" or name == "HIGH" or name == "MEDIUM" or name == "LOW":
                #    break
        ciphersList = ciphersList.strip(':')
        if username != "" and ciphersList:
            self.userswindow = UserSelect(username, ciphersList)
            self.accept()
        else:
            self.error = Error("Username and cipher must be set.")