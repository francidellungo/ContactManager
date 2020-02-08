# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/formDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 354)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.nameLayout = QtWidgets.QHBoxLayout()
        self.nameLayout.setObjectName("nameLayout")
        self.name_label = QtWidgets.QLabel(Dialog)
        self.name_label.setObjectName("name_label")
        self.nameLayout.addWidget(self.name_label)
        self.name_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.name_lineEdit.setStatusTip("")
        self.name_lineEdit.setInputMask("")
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.nameLayout.addWidget(self.name_lineEdit)
        self.verticalLayout_2.addLayout(self.nameLayout)
        self.surnameLayout = QtWidgets.QHBoxLayout()
        self.surnameLayout.setObjectName("surnameLayout")
        self.suename_label = QtWidgets.QLabel(Dialog)
        self.suename_label.setObjectName("suename_label")
        self.surnameLayout.addWidget(self.suename_label)
        self.surname_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.surname_lineEdit.setObjectName("surname_lineEdit")
        self.surnameLayout.addWidget(self.surname_lineEdit)
        self.verticalLayout_2.addLayout(self.surnameLayout)
        self.phoneLayout = QtWidgets.QHBoxLayout()
        self.phoneLayout.setObjectName("phoneLayout")
        self.phone_label = QtWidgets.QLabel(Dialog)
        self.phone_label.setObjectName("phone_label")
        self.phoneLayout.addWidget(self.phone_label)
        self.phone_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.phone_lineEdit.setObjectName("phone_lineEdit")
        self.phoneLayout.addWidget(self.phone_lineEdit)
        self.verticalLayout_2.addLayout(self.phoneLayout)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.name_label.setText(_translate("Dialog", "Name"))
        self.suename_label.setText(_translate("Dialog", "Surname"))
        self.phone_label.setText(_translate("Dialog", "Phone"))
        self.label.setText(_translate("Dialog", "TextLabel"))

