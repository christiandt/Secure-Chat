from userpref import UserPref
from PyQt4 import QtCore, QtGui
import sys


app = QtGui.QApplication(sys.argv)
usernameWindow = UserPref()
usernameWindow.show()

sys.exit(app.exec_())