from PyQt5.QtCore import pyqtSignal
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


class ContactsModel:
    contact_added = pyqtSignal(int)

    def __init__(self):
        # create DB and contacts table
        self.contacts_db = Database()
        self.contacts_db.createTable()

    def addContact(self, contact):
        # add a single contact to the contact db
        # NB: contact is a ContactModel obj
        self.contacts_db.addContact(contact)

    def getAllContacts(self):
        # get all contacts in the contact db
        return self.contacts_db.getAllContacts()


