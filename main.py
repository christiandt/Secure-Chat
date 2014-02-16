from userselect import userSelect
from PyQt4 import QtCore, QtGui
import sys

app = QtGui.QApplication(sys.argv)
ui = userSelect()
ui.show()

sys.exit(app.exec_())