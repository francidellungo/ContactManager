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

    # def setTag(self, tags: list):
    #     self.contacts_db.addTag()
    #     # tags is a list of tags for this contact

    def submitContactTags(self, contact_id, new_tags):
        contact_id = str(contact_id)
        old_tags = self.contacts_db.getContactTags(contact_id)
        tags_to_add = list(set(new_tags) - set(old_tags))
        # print('tags_to_add:    ', tags_to_add)
        tags_to_remove = list(set(old_tags) - set(new_tags))
        # print('tags_to_remove:    ', tags_to_remove)

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
