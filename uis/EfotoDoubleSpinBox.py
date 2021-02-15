#!/usr/bin/env python3
from PyQt5.QtWidgets import QDoubleSpinBox
from PyQt5 import QtCore
import sys

class EfotoDoubleSpinBox(QDoubleSpinBox):
	def __init__(self, parent=None):
		super(EfotoDoubleSpinBox, self).__init__(parent)
		self.keyPressEvent

	#TODO
	def keyPressEvent(self,event):
		if event.key() == QtCore.Qt.Key_Comma:
			print("QDoubleSpinBox Extension TODO")

if __name__ == '__main__':
	EfotoDoubleSpinBox
	print("module")