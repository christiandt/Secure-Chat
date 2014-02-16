
from PyQt4 import QtCore, QtGui
import sys



class Ui_UserWindow(QtGui.QDialog):
    def __init__(self):
        super(Ui_UserWindow, self).__init__()
        title = "Users"
        self.setWindowTitle(str(title))
        self.resize(300,400)

        self.layout = QtGui.QGridLayout(self)

        #listView
        self.list = QtGui.QListView()
        self.layout.addWidget(self.list, 0, 5)

        #selectbutton
        self.selectbutton = QtGui.QPushButton(self)
        self.selectbutton.setText("Select")
        self.selectbutton.setGeometry(QtCore.QRect(10, 330, 114, 51))
        self.layout.addWidget(self.list, 1, 0)

        #cancelbutton


        self.setLayout(self.layout)


    def setupUi(self, UserWindow):
        UserWindow.setObjectName(_fromUtf8("UserWindow"))
        UserWindow.resize(371, 384)
        self.centralWidget = QtGui.QWidget(UserWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.listView = QtGui.QListView(self.centralWidget)
        self.listView.setGeometry(QtCore.QRect(10, 10, 351, 311))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 330, 114, 51))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 330, 114, 51))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        UserWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(UserWindow)
        QtCore.QMetaObject.connectSlotsByName(UserWindow)

    def retranslateUi(self, UserWindow):
        UserWindow.setWindowTitle(_translate("UserWindow", "UserWindow", None))
        self.pushButton.setText(_translate("UserWindow", "Select", None))
        self.pushButton_2.setText(_translate("UserWindow", "Cancel", None))


app = QtGui.QApplication(sys.argv)
ui = Ui_UserWindow()
ui.show()

sys.exit(app.exec_())

