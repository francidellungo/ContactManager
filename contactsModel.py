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
        # address, nickname

    def setContactId(self, id):
        self.id = id

    def getId(self):
        return self.id


class ContactsListModel(QObject):
    contact_added = pyqtSignal()
    contact_removed = pyqtSignal()
    contact_updated = pyqtSignal()

    def __init__(self):
        super(ContactsListModel, self).__init__()
        self.contacts_db = ContactsDb()

    def saveNewContact(self, name, surname, phone, email, notes):
        # generate id for new contact and add new contact to contacts_db, return new id generated
        contact = ContactModel()
        contact.setFields(None, name, surname, phone, email, notes)
        contact.setContactId(self.contacts_db.generateNewContactId())
        self.contacts_db.addContact(contact)
        # emit signal contact added to db
        self.contact_added.emit()
        return contact.getId()

    def updateContact(self, id, name, surname, phone, email, notes):
        self.contacts_db.updateContact(id, name, surname, phone, email, notes)

    def getContactInfofromId(self, c_id):
        # get id, name, surname,phone,email, notes of the given contact
        return self.contacts_db.getContactInfo(c_id)

    def submitContact(self, id, name, surname, phone, email, notes, tags_checked):
        # check if contact was already in db or not
        if id is None:
            id = self.saveNewContact(name, surname, phone, email, notes)
        else:
            self.updateContact(id, name, surname, phone, email, notes)
            self.contact_updated.emit()

        self.submitContactTags(id, tags_checked)

    def getAllContacts(self, field_to_sort='name', mode='ASC'):
        # get all contacts in the contact db
        return self.contacts_db.getAllContacts(field_to_sort, mode)

    def getContactInfo(self, contact_id):
        # get id, name, surname, phone, email and notes
        return self.contacts_db.getContactInfo(contact_id)

    def deleteContact(self, contact_id):
        self.contacts_db.removeContact(contact_id)
        self.contacts_db.removeContactTag(contact_id)
        self.contact_removed.emit()

    def searchTerm(self, term):
        # list of contacts where term is present
        return self.contacts_db.searchWord(term)

    # tags

    def setTag(self, tags: list):
        self.contacts_db.addTag()
        # tags is a list of tags for this contact

    def submitContactTags(self, contact_id, new_tags):
        contact_id = str(contact_id)
        old_tags = self.contacts_db.getContactTags(contact_id)
        tags_to_add = list(set(new_tags) - set(old_tags))
        print('tags_to_add:    ', tags_to_add)
        tags_to_remove = list(set(old_tags) - set(new_tags))
        print('tags_to_remove:    ', tags_to_remove)

        for tag in tags_to_add:
            self.contacts_db.setContactTag(contact_id, tag)
        for tag in tags_to_remove:
            self.contacts_db.removeContactTag(contact_id, tag)

    def getContactTags(self, contact_id) -> list:
        # get a list of all the tags associated with a contact
        return self.contacts_db.getContactTags(str(contact_id))

    def getAllTags(self):
        return self.contacts_db.getAllTags()

    def getContactsFromTag(self, tag: str) -> list:
        # return list of id of the contacts that have the specified tag
        return self.contacts_db.getContactsFromTag(tag)

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
