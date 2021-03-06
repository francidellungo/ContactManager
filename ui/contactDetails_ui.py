# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/contactDetails.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(350, 538)
        Dialog.setMaximumSize(QtCore.QSize(500, 16777215))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)
        self.delete_pb = QtWidgets.QPushButton(Dialog)
        self.delete_pb.setObjectName("delete_pb")
        self.gridLayout.addWidget(self.delete_pb, 6, 0, 1, 1, QtCore.Qt.AlignRight)
        self.contact_info_layout = QtWidgets.QVBoxLayout()
        self.contact_info_layout.setObjectName("contact_info_layout")
        self.gridLayout.addLayout(self.contact_info_layout, 2, 0, 1, 1)
        self.edit_pb = QtWidgets.QPushButton(Dialog)
        self.edit_pb.setObjectName("edit_pb")
        self.gridLayout.addWidget(self.edit_pb, 5, 0, 1, 1, QtCore.Qt.AlignRight)
        self.horizontalWidget = QtWidgets.QWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy)
        self.horizontalWidget.setMaximumSize(QtCore.QSize(16777215, 45))
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.horizontalWidget)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.back_pb = QtWidgets.QToolButton(self.horizontalWidget)
        icon = QtGui.QIcon.fromTheme("back")
        self.back_pb.setIcon(icon)
        self.back_pb.setAutoRaise(False)
        self.back_pb.setObjectName("back_pb")
        self.gridLayout_2.addWidget(self.back_pb, 0, 0, 1, 1)
        self.contact_label = QtWidgets.QLabel(self.horizontalWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.contact_label.setFont(font)
        self.contact_label.setAutoFillBackground(False)
        self.contact_label.setAlignment(QtCore.Qt.AlignCenter)
        self.contact_label.setObjectName("contact_label")
        self.gridLayout_2.addWidget(self.contact_label, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.horizontalWidget, 0, 0, 1, 1)
        self.tag_h_layout = QtWidgets.QHBoxLayout()
        self.tag_h_layout.setObjectName("tag_h_layout")
        self.tags_scrollArea = QtWidgets.QScrollArea(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tags_scrollArea.sizePolicy().hasHeightForWidth())
        self.tags_scrollArea.setSizePolicy(sizePolicy)
        self.tags_scrollArea.setMinimumSize(QtCore.QSize(0, 150))
        self.tags_scrollArea.setMaximumSize(QtCore.QSize(16777215, 200))
        self.tags_scrollArea.setWidgetResizable(True)
        self.tags_scrollArea.setObjectName("tags_scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 328, 189))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.tags_layout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.tags_layout.setObjectName("tags_layout")
        self.tags_scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tag_h_layout.addWidget(self.tags_scrollArea)
        self.gridLayout.addLayout(self.tag_h_layout, 3, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.delete_pb.setText(_translate("Dialog", "Delete"))
        self.edit_pb.setText(_translate("Dialog", "Edit"))
        self.back_pb.setText(_translate("Dialog", "..."))
        self.contact_label.setText(_translate("Dialog", "name surname"))

