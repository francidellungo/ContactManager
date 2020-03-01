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
        new_contact_form.resize(400, 638)
        new_contact_form.setMaximumSize(QtCore.QSize(400, 16777215))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(new_contact_form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(-1, -1, -1, 0)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.name_label = QtWidgets.QLabel(new_contact_form)
        self.name_label.setObjectName("name_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.name_label)
        self.name_lineEdit = QtWidgets.QLineEdit(new_contact_form)
        self.name_lineEdit.setAccessibleDescription("")
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name_lineEdit)
        self.surname_label = QtWidgets.QLabel(new_contact_form)
        self.surname_label.setObjectName("surname_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.surname_label)
        self.surname_lineEdit = QtWidgets.QLineEdit(new_contact_form)
        self.surname_lineEdit.setObjectName("surname_lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.surname_lineEdit)
        self.phone_label = QtWidgets.QLabel(new_contact_form)
        self.phone_label.setObjectName("phone_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.phone_label)
        self.phone_lineEdit = QtWidgets.QLineEdit(new_contact_form)
        self.phone_lineEdit.setMaxLength(20)
        self.phone_lineEdit.setObjectName("phone_lineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.phone_lineEdit)
        self.email_label = QtWidgets.QLabel(new_contact_form)
        self.email_label.setObjectName("email_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.email_label)
        self.email_lineEdit = QtWidgets.QLineEdit(new_contact_form)
        self.email_lineEdit.setObjectName("email_lineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.email_lineEdit)
        self.notes_label = QtWidgets.QLabel(new_contact_form)
        self.notes_label.setObjectName("notes_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.notes_label)
        self.notes_textEdit = QtWidgets.QTextEdit(new_contact_form)
        self.notes_textEdit.setMaximumSize(QtCore.QSize(400, 100))
        self.notes_textEdit.setObjectName("notes_textEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.notes_textEdit)
        self.tags_label = QtWidgets.QLabel(new_contact_form)
        self.tags_label.setObjectName("tags_label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.tags_label)
        self.tags_scrollArea = QtWidgets.QScrollArea(new_contact_form)
        self.tags_scrollArea.setMinimumSize(QtCore.QSize(317, 150))
        self.tags_scrollArea.setMaximumSize(QtCore.QSize(16777215, 400))
        self.tags_scrollArea.setWidgetResizable(True)
        self.tags_scrollArea.setObjectName("tags_scrollArea")
        self.tags_layout_obj = QtWidgets.QWidget()
        self.tags_layout_obj.setGeometry(QtCore.QRect(0, 0, 315, 148))
        self.tags_layout_obj.setObjectName("tags_layout_obj")
        self.tags_layout = QtWidgets.QVBoxLayout(self.tags_layout_obj)
        self.tags_layout.setObjectName("tags_layout")
        self.tags_scrollArea.setWidget(self.tags_layout_obj)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.tags_scrollArea)
        self.image_pb = QtWidgets.QPushButton(new_contact_form)
        self.image_pb.setText("")
        icon = QtGui.QIcon.fromTheme("image-x-generic")
        self.image_pb.setIcon(icon)
        self.image_pb.setObjectName("image_pb")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.image_pb)
        self.img_label = QtWidgets.QLabel(new_contact_form)
        self.img_label.setObjectName("img_label")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.img_label)
        self.birthday_pb = QtWidgets.QPushButton(new_contact_form)
        self.birthday_pb.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./img/birthday.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.birthday_pb.setIcon(icon)
        self.birthday_pb.setObjectName("birthday_pb")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.birthday_pb)
        self.birthdayDateEdit = QtWidgets.QDateEdit(new_contact_form)
        self.birthdayDateEdit.setCalendarPopup(True)
        self.birthdayDateEdit.setObjectName("birthdayDateEdit")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.birthdayDateEdit)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.add_field_pb = QtWidgets.QPushButton(new_contact_form)
        self.add_field_pb.setObjectName("add_field_pb")
        self.verticalLayout_2.addWidget(self.add_field_pb, 0, QtCore.Qt.AlignLeft)
        self.add_tag_pb = QtWidgets.QPushButton(new_contact_form)
        self.add_tag_pb.setObjectName("add_tag_pb")
        self.verticalLayout_2.addWidget(self.add_tag_pb, 0, QtCore.Qt.AlignLeft)
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
        self.name_label.setText(_translate("new_contact_form", "Name"))
        self.name_lineEdit.setPlaceholderText(_translate("new_contact_form", "name"))
        self.surname_label.setText(_translate("new_contact_form", "Surname"))
        self.surname_lineEdit.setPlaceholderText(_translate("new_contact_form", "surname"))
        self.phone_label.setText(_translate("new_contact_form", "Phone"))
        self.phone_lineEdit.setPlaceholderText(_translate("new_contact_form", "phone"))
        self.email_label.setText(_translate("new_contact_form", "Email"))
        self.email_lineEdit.setPlaceholderText(_translate("new_contact_form", "email"))
        self.notes_label.setText(_translate("new_contact_form", "Notes"))
        self.notes_textEdit.setPlaceholderText(_translate("new_contact_form", "some notes..."))
        self.tags_label.setText(_translate("new_contact_form", "Tags"))
        self.img_label.setText(_translate("new_contact_form", "img"))
        self.birthdayDateEdit.setDisplayFormat(_translate("new_contact_form", "dd/MM/yyyy"))
        self.add_field_pb.setText(_translate("new_contact_form", "Add field"))
        self.add_tag_pb.setText(_translate("new_contact_form", "Add tag"))

