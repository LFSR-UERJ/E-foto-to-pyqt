#!/usr/bin/env python3
from PyQt5.QtWidgets import QLineEdit
from PyQt5 import QtCore
import sys

class DmsEdit(QLineEdit):
	def __init__(self, parent=None):
		super(DmsEdit, self).__init__(parent)
		self.keyPressEvent

    #TODO
	def keyPressEvent(self,event):
		if event.key() == QtCore.Qt.Key_Comma:
			print("QLineEdit Extension TODO")

if __name__ == '__main__':
	DmsEdit
	print("module")