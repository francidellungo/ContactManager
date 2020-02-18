import os

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QMessageBox, QLabel
from ui.contactDetails_ui import Ui_Dialog



class ContactDetails(QDialog):
    def __init__(self, model):
        super(ContactDetails, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.contact_id = None

        self.model = model

        # when window is closed clear lines
        self.ui.back_pb.clicked.connect(self.clearLines)
        self.ui.edit_pb.clicked.connect(self.clearLines)

        # delete contact behavior
        self.ui.delete_pb.clicked.connect(self.deleteContact)


    def deleteContact(self):
        buttonReply = QMessageBox.question(self, 'Remove contact', "Are you sure you want to delete " + self.ui.contact_label.text() + "?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            self.model.deleteContact(self.contact_id)
        # if buttonReply == QMessageBox.No:
        #     print('No clicked.')

    def showDetails(self, contact_id):
        contact_details = list(self.model.getContactInfofromId(contact_id))[1:]
        self.ui.contact_label.setText(contact_details[0] + ' ' + contact_details[1])
        for detail in contact_details:
            # TODO: fix too much distance between fields and insert icons
            if detail != '':
                self.ui.contact_info_layout.addWidget(QtWidgets.QLabel((str(detail) if detail is not None else ' ')))

            # if detail != '':
                # layout = QtWidgets.QHBoxLayout()
                # field_icon = QtWidgets.QLabel()
                # pixmap = QPixmap('img/phoneIcon2.png')
                # field_icon.setPixmap(pixmap.scaledToWidth(30))
                # # self.resize(pixmap.width(), pixmap.height())
                # layout.addWidget(field_icon)
                # layout.addWidget(QtWidgets.QLabel((str(detail) if detail is not None else ' ')))
                # self.ui.contact_info_layout.addWidget(QtWidgets.QLabel((str(detail) if detail is not None else ' ')))
                # self.ui.contact_info_layout.addWidget(layout.widget())

                # self.horiz = QtWidgets.QHBoxLayout(self)
                # self.img_label = QLabel()
                # self.img_label.setScaledContents(True)
                # pixmap = QPixmap(os.path.join('img', 'phoneIcon2.png'))
                # self.img_label.setPixmap(pixmap)
                # self.img_label.setFixedSize(150, 150)
                # self.horiz.addWidget(self.img_label)
                # self.horiz.addWidget(QtWidgets.QLabel(str(detail)))
                # self.ui.contact_info_layout.addWidget(self.horiz.widget())


    def clearLines(self):
        self.ui.contact_label.clear()
        for i in reversed(range(self.ui.contact_info_layout.count())):
            item = self.ui.contact_info_layout.itemAt(i).widget()
            item.deleteLater()

    def setContact(self, contact_id):
        self.contact_id = contact_id

        # self.ui.surname_lineEdit.clear()
        # self.ui.phone_lineEdit.clear()
        # self.ui.email_lineEdit.clear()

        # self.ui.contact_info_layout.addWidget(QtWidgets.QLabel(contact_details[2]))
        # self.ui.contact_info_layout.addWidget(QtWidgets.QLabel(str(contact.surname)))