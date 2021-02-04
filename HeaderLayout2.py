# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HeaderLayout.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(440, 545)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.formLayout = QtWidgets.QFormLayout(self.frame_3)
        self.formLayout.setObjectName("formLayout")
        self.labelName = QtWidgets.QLabel(self.frame_3)
        self.labelName.setObjectName("labelName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelName)
        self.lineEditName = QtWidgets.QLineEdit(self.frame_3)
        self.lineEditName.setObjectName("lineEditName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditName)
        self.labelDescription = QtWidgets.QLabel(self.frame_3)
        self.labelDescription.setObjectName("labelDescription")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelDescription)
        self.textEditDescription = QtWidgets.QTextEdit(self.frame_3)
        self.textEditDescription.setObjectName("textEditDescription")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textEditDescription)
        self.labelOwner = QtWidgets.QLabel(self.frame_3)
        self.labelOwner.setObjectName("labelOwner")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelOwner)
        self.lineEditOwner = QtWidgets.QLineEdit(self.frame_3)
        self.lineEditOwner.setObjectName("lineEditOwner")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditOwner)
        self.labelAims = QtWidgets.QLabel(self.frame_3)
        self.labelAims.setObjectName("labelAims")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelAims)
        self.lineEditAims = QtWidgets.QLineEdit(self.frame_3)
        self.lineEditAims.setObjectName("lineEditAims")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEditAims)
        self.labelContext = QtWidgets.QLabel(self.frame_3)
        self.labelContext.setObjectName("labelContext")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.labelContext)
        self.lineEditContext = QtWidgets.QLineEdit(self.frame_3)
        self.lineEditContext.setObjectName("lineEditContext")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEditContext)
        self.verticalLayout.addWidget(self.frame_3)
        self.metadataFrame = QtWidgets.QFrame(self.frame)
        self.metadataFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.metadataFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.metadataFrame.setObjectName("metadataFrame")
        self.formLayout_2 = QtWidgets.QFormLayout(self.metadataFrame)
        self.formLayout_2.setObjectName("formLayout_2")
        self.lineMetadata = QtWidgets.QFrame(self.metadataFrame)
        self.lineMetadata.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineMetadata.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineMetadata.setObjectName("lineMetadata")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.lineMetadata)
        self.labelFilePath = QtWidgets.QLabel(self.metadataFrame)
        self.labelFilePath.setObjectName("labelFilePath")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelFilePath)
        self.lineEditFilePath = QtWidgets.QLineEdit(self.metadataFrame)
        self.lineEditFilePath.setEnabled(True)
        self.lineEditFilePath.setReadOnly(True)
        self.lineEditFilePath.setObjectName("lineEditFilePath")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditFilePath)
        self.labelFileName = QtWidgets.QLabel(self.metadataFrame)
        self.labelFileName.setObjectName("labelFileName")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelFileName)
        self.lineEditFileName = QtWidgets.QLineEdit(self.metadataFrame)
        self.lineEditFileName.setEnabled(True)
        self.lineEditFileName.setReadOnly(True)
        self.lineEditFileName.setObjectName("lineEditFileName")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEditFileName)
        self.labelCreationDate = QtWidgets.QLabel(self.metadataFrame)
        self.labelCreationDate.setObjectName("labelCreationDate")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.labelCreationDate)
        self.dateTimeEditCreationDate = QtWidgets.QDateTimeEdit(self.metadataFrame)
        self.dateTimeEditCreationDate.setEnabled(True)
        self.dateTimeEditCreationDate.setReadOnly(True)
        self.dateTimeEditCreationDate.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateTimeEditCreationDate.setObjectName("dateTimeEditCreationDate")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.dateTimeEditCreationDate)
        self.labelModificationDate = QtWidgets.QLabel(self.metadataFrame)
        self.labelModificationDate.setObjectName("labelModificationDate")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.labelModificationDate)
        self.dateTimeEditModificationDate = QtWidgets.QDateTimeEdit(self.metadataFrame)
        self.dateTimeEditModificationDate.setEnabled(True)
        self.dateTimeEditModificationDate.setReadOnly(True)
        self.dateTimeEditModificationDate.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateTimeEditModificationDate.setObjectName("dateTimeEditModificationDate")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.dateTimeEditModificationDate)
        self.labelMetadata = QtWidgets.QLabel(self.metadataFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelMetadata.sizePolicy().hasHeightForWidth())
        self.labelMetadata.setSizePolicy(sizePolicy)
        self.labelMetadata.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.labelMetadata.setObjectName("labelMetadata")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.labelMetadata)
        self.verticalLayout.addWidget(self.metadataFrame)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.labelName.setBuddy(self.lineEditName)
        self.labelDescription.setBuddy(self.textEditDescription)
        self.labelOwner.setBuddy(self.lineEditOwner)
        self.labelAims.setBuddy(self.lineEditAims)
        self.labelContext.setBuddy(self.lineEditContext)
        self.labelFilePath.setBuddy(self.lineEditFilePath)
        self.labelFileName.setBuddy(self.lineEditFileName)
        self.labelCreationDate.setBuddy(self.dateTimeEditCreationDate)
        self.labelModificationDate.setBuddy(self.dateTimeEditModificationDate)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.labelName.setText(_translate("Form", "Name"))
        self.labelDescription.setText(_translate("Form", "Description"))
        self.labelOwner.setText(_translate("Form", "Owner"))
        self.labelAims.setText(_translate("Form", "Goals"))
        self.labelContext.setText(_translate("Form", "Context"))
        self.labelFilePath.setText(_translate("Form", "File path"))
        self.labelFileName.setText(_translate("Form", "File name"))
        self.labelCreationDate.setText(_translate("Form", "Creation date"))
        self.labelModificationDate.setText(_translate("Form", "Modification date"))
        self.labelMetadata.setText(_translate("Form", "Metadata"))
        self.label.setText(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Project Header</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
