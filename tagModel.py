from PyQt5.QtCore import pyqtSignal, QObject
from contactsdb import ContactsDb


class TagsModel(QObject):

    def __init__(self):
        super(TagsModel, self).__init__()
        self.contacts_db = ContactsDb()

    def getAllTags(self):
        return self.contacts_db.getAllTags()

    def newTag(self, tag_name):
        # create and add new tag
        self.contacts_db.addTag(tag_name)

