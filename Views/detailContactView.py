from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
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
        # self.model.deleteContact()
        pass
        #TODO finish call model function to removw contact from db

    def showDetails(self, contact_id):
        contact_details = list(self.model.getContactInfofromId(contact_id))[1:]
        self.ui.contact_label.setText(contact_details[0] + ' ' + contact_details[1])
        for detail in contact_details:
            self.ui.contact_info_layout.addWidget(QtWidgets.QLabel((str(detail) if detail is not None else ' ')))

    def clearLines(self):
        self.ui.contact_label.clear()
        for i in reversed(range(self.ui.contact_info_layout.count())):
            item = self.ui.contact_info_layout.itemAt(i).widget()
            item.deleteLater()

    def setContact(self, contact):
        self.contact = contact

        # self.ui.surname_lineEdit.clear()
        # self.ui.phone_lineEdit.clear()
        # self.ui.email_lineEdit.clear()

        # self.ui.contact_info_layout.addWidget(QtWidgets.QLabel(contact_details[2]))
        # self.ui.contact_info_layout.addWidget(QtWidgets.QLabel(str(contact.surname)))