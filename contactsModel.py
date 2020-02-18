from PyQt5.QtCore import pyqtSignal, QObject
from contactsdb import ContactsDb


class ContactModel:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.surname = ""
        self.phone = ""
        self.email = ""
        self.notes = ""

    def setFields(self, id, name, surname, phone=None, email=None, notes=None):
        self.id = id
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email
        self.notes = notes

    def setContactId(self, id):
        self.id = id

    def getId(self):
        return self.id


class ContactsListModel(QObject):
    contact_added = pyqtSignal()
    contact_removed = pyqtSignal()

    def __init__(self):
        super(ContactsListModel, self).__init__()
        self.contacts_db = ContactsDb()

    def saveNewContact(self, name, surname, phone, email, notes):
        # generate id for new contact and add new contact to contacts_db
        contact = ContactModel()
        contact.setFields(None, name, surname, phone, email, notes)
        contact.setContactId(self.contacts_db.generateNewContactId())
        self.contacts_db.addContact(contact)
        # emit signal contact added to db
        self.contact_added.emit()

    def updateContact(self, id, name, surname, phone, email, notes):
        self.contacts_db.updateContact(id, name, surname, phone, email, notes)

    def getContactInfofromId(self, c_id):
        # get id, name, surname,phone,email, notes of the given contact
        return self.contacts_db.getContactInfo(c_id)

    def submitContact(self, id, name, surname, phone, email, notes):
        # check if contact was already in db or not
        if id is None:
            self.saveNewContact(name, surname, phone, email, notes)
        else:
            self.updateContact(id, name, surname, phone, email, notes)

    def getAllContacts(self, field_to_sort='name', mode='ASC'):
        # get all contacts in the contact db
        return self.contacts_db.getAllContacts(field_to_sort, mode)

    def getContactInfo(self, contact_id):
        # get id, name, surname, phone, email and notes
        return self.contacts_db.getContactInfo(contact_id)

    def deleteContact(self, contact_id):
        self.contacts_db.removeContact(contact_id)
        self.contact_removed.emit()

    def searchTerm(self, term):
        # list of contacts where term is present
        return self.contacts_db.searchWord(term)

# class ContactsModel(QObject):
#     contact_added = pyqtSignal()
#
#     def __init__(self):
#         super(ContactsModel, self).__init__()
#         # create DB and contacts table
#         self.contacts_db = Database()
#         self.contacts_db.createTable()
#
#     def addContact(self, contact):
#         # add a single contact to the contact db
#         # NB: contact is a ContactModel obj
#         new_id = self.contacts_db.generateNewContactId()
#         contact.setContactId(new_id)
#         print('contact.id', contact.id)
#         self.contacts_db.addContact(contact)
#         self.contact_added.emit()
#
#     def getAllContacts(self, field_to_sort='name', mode='ASC'):
#         # get all contacts in the contact db
#         return self.contacts_db.getAllContacts(field_to_sort, mode)
#
#     def getContactInfo(self, contact_id):
#         # get name, surname, phone, email and notes
#         return self.contacts_db.getContactInfo(contact_id)
#
#     def isContactInDb(self, contact_id):
#         # return True if contact id is in db else False
#         return self.contacts_db.isContactInDb(contact_id)
#
#     def submitContact(self, contact_id, contact):
#         # todo fix: maybe contact id not needed?
#         # add or update contact in contacts db
#         if not self.contacts_db.isContactInDb(contact_id):
#             self.addContact(contact)
#         else:
#             self.updateContact(contact)
#
#     def updateContact(self, contact):
#         # update contact info
#         self.contacts_db.updateContact(contact)
