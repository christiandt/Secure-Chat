from userpref import userPref
from PyQt4 import QtCore, QtGui
import sys


app = QtGui.QApplication(sys.argv)
usernameWindow = userPref()
usernameWindow.show()

sys.exit(app.exec_())