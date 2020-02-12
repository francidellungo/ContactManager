from PyQt5 import QtWidgets
import PyQt5.QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from ui.mainWindow_ui import Ui_MainWindow
from ui.formDialog_ui import Ui_new_contact_form
from contactsModel import ContactsModel, ContactModel
import sys

# TODO remove this at the end of the project
"""
All functions and classes names are thisKindOfTypo, and variables are this_kind_of_typo
"""
"""
See https://www.tutorialspoint.com/pyqt/pyqt_qstackedwidget.htm for QStackedWidget to switch between windows
"""


class NewContactView(QDialog):
    def __init__(self, model):
        super(NewContactView, self).__init__()
        self.ui = Ui_new_contact_form()
        self.ui.setupUi(self)
        self.model = model

        self.ui.buttonBox.accepted.connect(lambda: self.model.addContact(ContactModel(
            self.ui.name_lineEdit.text(), self.ui.surname_lineEdit.text(),
            self.ui.phone_lineEdit.text(), self.ui.email_lineEdit.text(),
            self.ui.notes_textEdit.toPlainText())))
        #
        # self.ui.buttonBox.accepted.connect(
        #     lambda: self.save(self.ui.name_lineEdit.text(), self.ui.surname_lineEdit.text()))


class ContactManagerView(QMainWindow):
    def __init__(self, model):
        super(ContactManagerView, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # db of contacts
        self.model = model
        self.showContacts()

        # connect buttons to slots
        # self.ui.newContact_pb.clicked.connect(self.createNewContact)
        self.ui.sort_combobox.currentIndexChanged.connect(self.sortBy)

        self.model.contact_added.connect(self.refreshContacts)

    def showContacts(self, contacts_=None):
        contacts = (contacts_ if contacts_ is not None else self.model.getAllContacts())
        for id, contact in enumerate(contacts):
            new_contact = QtWidgets.QPushButton(self.ui.contacts_scrollAreaW)
            new_contact.setFlat(True)
            # new_label.setParent(self.ui.contacts_scrollAreaW)
            new_contact.setText(contact[1] + ' ' + contact[2])
            new_contact.setObjectName(contact[0])
            if id != 0:
                line = QtWidgets.QFrame(self.ui.contacts_scrollAreaW)
                line.setFrameShape(QtWidgets.QFrame.HLine)
                line.setFrameShadow(QtWidgets.QFrame.Sunken)
                line.setObjectName("line")
                self.ui.contacts_layout.addWidget(line)
            self.ui.contacts_layout.addWidget(new_contact)
            # new_contact.clicked.connect(self.clicked)

    def refreshContacts(self, contacts=None):
        for i in reversed(range(self.ui.contacts_layout.count())):
            item = self.ui.contacts_layout.itemAt(i).widget()
            item.deleteLater()
            # self.ui.contacts_layout.removeWidget(item)
        print('removed all contacts', self.ui.contacts_layout.count())
        self.showContacts(contacts)

    def addRow(self, name, surname):
        """
        Add new contact to contacts GUI
        :param name:
        :param surname:
        :return:
        """
        new_contact = QtWidgets.QPushButton(self.ui.contacts_scrollAreaW)
        new_contact.setFlat(True)
        new_contact.setText(name + ' ' + surname)

        line = QtWidgets.QFrame(self.ui.contacts_scrollAreaW)
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        line.setObjectName("line")
        self.ui.contacts_layout.addWidget(line)
        self.ui.contacts_layout.addWidget(new_contact)
        # new_contact.clicked.connect(self.clicked)

    def sortBy(self, field, mode='ASC'):
        # field to sort by
        # print('sort by', field)
        # TODO sort also by number or email ??
        field_to_sort = ('name' if field == 0 else 'surname')
        contacts = self.model.getAllContacts(field_to_sort)
        self.refreshContacts(contacts)
        pass

    def clicked(self):
        print('clicked')

    # def createNewContact(self):
    #     """
    #     Open form dialog to create new contact
    #     :return:
    #     """
    #     self.dialog = QtWidgets.QDialog()
    #     self.dialog.ui = Ui_new_contact_form()
    #     self.dialog.ui.setupUi(self.dialog)
    #     # self.ui.mainWindow.close()
    #     # in mainWindow.py file:         self.mainWindow = MainWindow
    #     self.dialog.show()
    #
    #     # name = self.dialog.ui.name_lineEdit.text()
    #     # surname = self.dialog.ui.surname_lineEdit.text()
    #     # phone = self.dialog.ui.phone_lineEdit.text()
    #     # email = self.dialog.ui.email_lineEdit.text()
    #     # notes = self.dialog.ui.notes_textEdit.toPlainText()
    #
    #     # new_contact = ContactModel(name, surname, phone, email, notes)
    #     # TODO: error if name not given
    #     self.dialog.ui.buttonBox.accepted.connect(lambda: self.model.addContact(ContactModel(
    #         self.dialog.ui.name_lineEdit.text(), self.dialog.ui.surname_lineEdit.text(),
    #         self.dialog.ui.phone_lineEdit.text(), self.dialog.ui.email_lineEdit.text(),
    #         self.dialog.ui.notes_textEdit.toPlainText())))
    #
    #     self.dialog.ui.buttonBox.accepted.connect(lambda: self.save(self.dialog.ui.name_lineEdit.text(), self.dialog.ui.surname_lineEdit.text()))

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
