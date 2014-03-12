from PyQt4 import QtCore, QtGui

class Error(QtGui.QDialog):

	def __init__(self, message):
		super(Error, self).__init__()
		self.setWindowTitle("Error")
		self.resize(500, 100)
		self.layout = QtGui.QGridLayout(self)
		errorLabel = QtGui.QLabel(message)
		self.layout.addWidget(errorLabel, 0, 0)
		self.setLayout(self.layout)
		self.show()