import PyQt5
from PyQt5.QtCore import pyqtSignal, QObject
from database import Database


class ContactModel:
    def __init__(self, name, surname, phone=None, email=None, notes=None):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email
        self.notes = notes

    # def setFirstName(self, first):
    #     self.name = first


class ContactsModel(QObject):
    contact_added = pyqtSignal()

    def __init__(self):
        super(ContactsModel, self).__init__()
        # create DB and contacts table
        self.contacts_db = Database()
        self.contacts_db.createTable()

    def addContact(self, contact):
        # add a single contact to the contact db
        # NB: contact is a ContactModel obj
        self.contacts_db.addContact(contact)
        self.contact_added.emit()

    def getAllContacts(self, field_to_sort='name', mode='ASC'):
        # get all contacts in the contact db
        return self.contacts_db.getAllContacts(field_to_sort, mode)


