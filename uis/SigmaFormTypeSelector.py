#!/usr/bin/env python3
from PyQt5.QtWidgets import QComboBox
from PyQt5 import QtCore
import sys

class SigmaFormTypeSelector(QComboBox):
	def __init__(self, parent=None):
		super(SigmaFormTypeSelector, self).__init__(parent)
		self.keyPressEvent

	#TODO
	def keyPressEvent(self,event):
		if event.key() == QtCore.Qt.Key_Comma:
			print("QComboBox Extension TODO")

if __name__ == '__main__':
	SigmaFormTypeSelector
	print("module")