# -*- coding: utf-8 -*-
#
#  ProjectUserInterface.py
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

# Compile resources.py com:
# pyrcc5 resource/resource.qrc -o resources.py

import resources                                     
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog
from HeaderForm import HeaderForm
from FlightForm import FlightForm
from TerrainForm import TerrainForm
from SensorForm import SensorForm
import sys, os


project = ""
class ProjectUserInterface(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(ProjectUserInterface, self).__init__(parent)
        self.interface = uic.loadUi('uis/FormProject.ui', self)
        #self.execute()                              # Simulando o básico de interação
        self.interface.menuProject.triggered.connect(self.createProject)
        self.show()                                  

    def execute(self):
        # Hide Debug
        self.debuggerDockWidget.hide()
        self.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.debuggerDockWidget)
        # Create shortcut to Debugger
        shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+Shift+D"), self)
        shortcut.activated.connect(self.toggleDebug)
        # Sample of ETreeWidget execution without a real project
        self.projectDockWidget.setWidget(ETree(self))                   # A interface cria a árvore e colocar em sua estrutura
        oldWidget = self.interface.centralWidget()
        self.interface.setCentralWidget(HeaderForm(self))
        oldWidget.deleteLater()
    def toggleDebug(self):
        # Change debugger visibility
        self.debuggerDockWidget.setVisible(not self.debuggerDockWidget.isVisible())

    def createProject(self):
        global project
        url = QFileDialog.getSaveFileName(self, "Criar Projeto", "", "*.epp")
        project = url[0]
        if project:
            self.execute()



class ETree(QtWidgets.QTreeWidget):
    def __init__(self, parent=None):
        super(ETree, self).__init__(parent)
        self.interface = parent                                         # A árvore preserva o link de acesso da interface
        self.treeUI()
        self.itemClicked.connect(self.Eclicked)

    def treeUI(self):
        #http://3plus.hatenablog.com/entry/2014/09/12/222738
        tree = [("Project Header",0,None)
            , ("Terrain",1,None)
            ,("Sensor",2,None)
            ,("Flight",3,None)
            ,("Images",4,None)
            ,("Points",5,None)]

        self.addTopLevelItems(self.returnTree(tree))
        self.itemDelegate()
        self.header().hide()
        self.setIndentation(20)
        self.setStyleSheet(
'''
QTreeView::branch:has-siblings:!adjoins-item {
    border-image: url(./icons/branch/vline.png) 0;
}

QTreeView::branch:has-siblings:adjoins-item {
    border-image: url(./icons/branch/branch-more.png) 0;
}

QTreeView::branch:!has-children:!has-siblings:adjoins-item {
    border-image: url(./icons/branch/branch-end.png) 0;
}
QTreeView::item:selected:active{
background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6ea1f1, stop: 1 #567dbc);
}

''')

    def returnTree(self, lst=[]):
        items = []
        while len(lst):
            k, v, n = lst.pop(0)
            item = QtWidgets.QTreeWidgetItem([k])
            item.setData(0, QtCore.Qt.UserRole, v)
            items.append(item)
            if n is not None:
                items[-1].addChildren(self.returnTree(n))

        return items

    def Eclicked(self, it, col):
        if it.text(col) == "Project Header":
            oldWidget = self.interface.centralWidget()     # Trocas de formulários implicam em:
            self.interface.setCentralWidget(HeaderForm(self))  # Criar e posicionar novos formulários
            oldWidget.deleteLater()                        # e agendar a destruição dos anteriores
        elif it.text(col) == "Terrain":
            oldWidget = self.interface.centralWidget()
            self.interface.setCentralWidget(TerrainForm(self))
            oldWidget.deleteLater()
        elif it.text(col) == "Sensor":
            oldWidget = self.interface.centralWidget()
            self.interface.setCentralWidget(SensorForm(self))
            oldWidget.deleteLater()
        elif it.text(col) == "Flight":
            oldWidget = self.interface.centralWidget()
            self.interface.setCentralWidget(FlightForm(self))
            oldWidget.deleteLater()
        elif it.text(col) == "Images":
            print("4")
        elif it.text(col) == "Points":
            print("5")
        else:
            pass



def main():
    App = QtWidgets.QApplication(sys.argv)
    window = ProjectUserInterface()
    sys.exit(App.exec_())

if __name__ == "__main__":
    main()
