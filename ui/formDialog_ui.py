# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/formDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_new_contact_form(object):
    def setupUi(self, new_contact_form):
        new_contact_form.setObjectName("new_contact_form")
        new_contact_form.resize(400, 354)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(new_contact_form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(-1, -1, -1, 0)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.surname_label = QtWidgets.QLabel(new_contact_form)
        self.surname_label.setObjectName("surname_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.surname_label)
        self.name_lineEdit = QtWidgets.QLineEdit(new_contact_form)
        self.name_lineEdit.setAccessibleDescription("")
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name_lineEdit)
        self.name_label = QtWidgets.QLabel(new_contact_form)
        self.name_label.setObjectName("name_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.name_label)
        self.surname_lineEdit = QtWidgets.QLineEdit(new_contact_form)
        self.surname_lineEdit.setObjectName("surname_lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.surname_lineEdit)
        self.phone_label = QtWidgets.QLabel(new_contact_form)
        self.phone_label.setObjectName("phone_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.phone_label)
        self.phone_lineEdit = QtWidgets.QLineEdit(new_contact_form)
        self.phone_lineEdit.setObjectName("phone_lineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.phone_lineEdit)
        self.email_label = QtWidgets.QLabel(new_contact_form)
        self.email_label.setObjectName("email_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.email_label)
        self.email_lineEdit = QtWidgets.QLineEdit(new_contact_form)
        self.email_lineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.email_lineEdit.setObjectName("email_lineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.email_lineEdit)
        self.notes_label = QtWidgets.QLabel(new_contact_form)
        self.notes_label.setObjectName("notes_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.notes_label)
        self.notes_textEdit = QtWidgets.QTextEdit(new_contact_form)
        self.notes_textEdit.setObjectName("notes_textEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.notes_textEdit)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.add_field_pb = QtWidgets.QPushButton(new_contact_form)
        self.add_field_pb.setObjectName("add_field_pb")
        self.verticalLayout_2.addWidget(self.add_field_pb, 0, QtCore.Qt.AlignLeft)
        self.buttonBox = QtWidgets.QDialogButtonBox(new_contact_form)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(new_contact_form)
        self.buttonBox.accepted.connect(new_contact_form.accept)
        self.buttonBox.rejected.connect(new_contact_form.reject)
        QtCore.QMetaObject.connectSlotsByName(new_contact_form)

    def retranslateUi(self, new_contact_form):
        _translate = QtCore.QCoreApplication.translate
        new_contact_form.setWindowTitle(_translate("new_contact_form", "New Contact"))
        self.surname_label.setText(_translate("new_contact_form", "Surname"))
        self.name_lineEdit.setPlaceholderText(_translate("new_contact_form", "John"))
        self.name_label.setText(_translate("new_contact_form", "Name"))
        self.surname_lineEdit.setPlaceholderText(_translate("new_contact_form", "Smith"))
        self.phone_label.setText(_translate("new_contact_form", "Phone"))
        self.phone_lineEdit.setPlaceholderText(_translate("new_contact_form", "+39 333 111 222"))
        self.email_label.setText(_translate("new_contact_form", "Email"))
        self.email_lineEdit.setPlaceholderText(_translate("new_contact_form", "johnsmith@unifi.com"))
        self.notes_label.setText(_translate("new_contact_form", "Notes"))
        self.notes_textEdit.setPlaceholderText(_translate("new_contact_form", "some notes..."))
        self.add_field_pb.setText(_translate("new_contact_form", "Add field"))

