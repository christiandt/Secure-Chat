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
        aesBox = QtGui.QCheckBox("AES256")
        self.cryptoBoxes.append(aesBox)
        self.cryptoGroupLayout.addWidget(aesBox, 0, 1)
        shaBox = QtGui.QCheckBox("SHA1")
        self.cryptoBoxes.append(shaBox)
        self.cryptoGroupLayout.addWidget(shaBox, 1, 1)
        desBox = QtGui.QCheckBox("3DES")
        self.cryptoBoxes.append(desBox)
        self.cryptoGroupLayout.addWidget(desBox, 2, 1)
        rsaBox = QtGui.QCheckBox("RSA")
        self.cryptoBoxes.append(rsaBox)
        self.cryptoGroupLayout.addWidget(rsaBox, 3, 1)
        rc4Box = QtGui.QCheckBox("RC4")
        self.cryptoBoxes.append(rc4Box)
        self.cryptoGroupLayout.addWidget(rc4Box, 4, 1)

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
        print ciphersList
        if username != "" and ciphersList:
            self.userswindow = UserSelect(username, ciphersList)
            self.accept()
        else:
            self.error = Error("Username and cipher must be set.")