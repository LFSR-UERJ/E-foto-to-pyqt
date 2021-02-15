# -*- coding: utf-8 -*-
#
#  TerrainForm.py
#
#  Copyright 2021 Badolato <badolato@Medusa>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
#!/usr/bin/env python3

import resources
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys

from uis import EfotoDoubleSpinBox
from uis import SigmaFormTypeSelector
from uis import SigmaFormContent
from uis import ScienceSpinBox
#print(EfotoDoubleSpinBoxModule.__file__)
import traceback


class SensorForm(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(SensorForm, self).__init__(parent)
        sys.modules['SigmaFormTypeSelector'] = SigmaFormTypeSelector
        sys.modules['EfotoDoubleSpinBox'] = EfotoDoubleSpinBox
        sys.modules['SigmaFormContent'] = SigmaFormContent
        sys.modules['ScienceSpinBox'] = ScienceSpinBox
        self.interface = uic.loadUi('uis/SensorLayout.ui', self)
        self.show()
#TODO
#resize
def main():
    App = QtWidgets.QApplication(sys.argv)
    window = SensorForm()
    sys.exit(App.exec_())

if __name__ == "__main__":
    main()
