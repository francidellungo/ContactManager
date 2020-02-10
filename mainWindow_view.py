from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from mainWindow_ui import Ui_MainWindow
from formDialog_ui import Ui_new_contact_form
import sys

# TODO remove this at the end of the project
"""
All functions and classes names are thisKindOfTypo, and variables are this_kind_of_typo
"""


class ContactManagerView(QMainWindow):
    def __init__(self):
        super(ContactManagerView, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.newContact_pb.clicked.connect(self.createNewContact)

    def addRow(self, name, surname):
        """
        Add new contact to contacts GUI
        :param name:
        :param surname:
        :return:
        """
        label_2 = QtWidgets.QLabel(self.ui.contacts_scrollAreaW)
        label_2.setText(name + ' ' + surname)
        self.ui.contacts_layout.addWidget(label_2)

    def createNewContact(self):
        """
        Open form dialog to create new contact
        :return:
        """
        self.dialog = QtWidgets.QDialog()
        self.dialog.ui = Ui_new_contact_form()
        self.dialog.ui.setupUi(self.dialog)
        self.dialog.show()

        # name = self.dialog.ui.name_lineEdit.text()
        # surname = self.dialog.ui.surname_lineEdit.text()
        self.dialog.ui.buttonBox.accepted.connect(lambda: self.save(self.dialog.ui.name_lineEdit.text(), self.dialog.ui.surname_lineEdit.text()))

    def save(self, name, surname):
        """
        Save new contact in DB
        :param name:
        :param surname:
        :return:
        """
        print('accept')
        # TODO validate input before save
        self.addRow(name, surname)
        # save in DB and show contacts in DB


if __name__== "__main__":
    app = QApplication(sys.argv)
    window = ContactManagerView()
    window.show()
    sys.exit(app.exec_())
