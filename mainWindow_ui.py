# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(956, 762)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.contacts_scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.contacts_scrollArea.setWidgetResizable(True)
        self.contacts_scrollArea.setObjectName("contacts_scrollArea")
        self.contacts_scrollAreaW = QtWidgets.QWidget()
        self.contacts_scrollAreaW.setGeometry(QtCore.QRect(0, 0, 936, 664))
        self.contacts_scrollAreaW.setObjectName("contacts_scrollAreaW")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.contacts_scrollAreaW)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.contact0_label = QtWidgets.QLabel(self.contacts_scrollAreaW)
        self.contact0_label.setObjectName("contact0_label")
        self.verticalLayout_2.addWidget(self.contact0_label)
        self.line = QtWidgets.QFrame(self.contacts_scrollAreaW)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.contact1_label = QtWidgets.QLabel(self.contacts_scrollAreaW)
        self.contact1_label.setObjectName("contact1_label")
        self.verticalLayout_2.addWidget(self.contact1_label)
        self.line_2 = QtWidgets.QFrame(self.contacts_scrollAreaW)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.label_3 = QtWidgets.QLabel(self.contacts_scrollAreaW)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.line_3 = QtWidgets.QFrame(self.contacts_scrollAreaW)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        self.label_4 = QtWidgets.QLabel(self.contacts_scrollAreaW)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.contacts_scrollArea.setWidget(self.contacts_scrollAreaW)
        self.gridLayout.addWidget(self.contacts_scrollArea, 0, 0, 1, 1)
        self.newContact_pb = QtWidgets.QPushButton(self.centralwidget)
        self.newContact_pb.setObjectName("newContact_pb")
        self.gridLayout.addWidget(self.newContact_pb, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 956, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Contact Manager"))
        self.contact0_label.setText(_translate("MainWindow", "TextLabel"))
        self.contact1_label.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.newContact_pb.setText(_translate("MainWindow", "New contact"))

