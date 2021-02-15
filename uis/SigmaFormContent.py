#!/usr/bin/env python3
from PyQt5.QtWidgets import QFrame
from PyQt5 import QtCore
import sys

class SigmaFormContent(QFrame):
	def __init__(self, parent=None):
		super(SigmaFormContent, self).__init__(parent)
		self.keyPressEvent


	#TODO
	def keyPressEvent(self,event):
		if event.key() == QtCore.Qt.Key_Comma:
			print("QFrame Extension TODO")

if __name__ == '__main__':
	SigmaFormContent
	print("module")