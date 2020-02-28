import sqlite3
from contactsModel import *
import uuid
# conn = sqlite3.connect('contacts.db')
# c = conn.cursor()
#
# contact1 = ContactModel('franci', 'delluu', phone=3232)
# # c.execute("""CREATE TABLE contacts(
# #     name text,
# #     surname text,
# #     phone integer
# #     )""")
#
# # c.execute("INSERT INTO contacts VALUES ('Fra', 'Delld', 34343)")
# # version 2
# # c.execute("INSERT INTO contacts VALUES (:name , :surname, :phone)", {'name': str(contact1.name), 'surname': contact1.surname, 'phone': contact1.phone})
# # conn.commit()
# c.execute("SELECT * FROM contacts WHERE name='franci'")
#
#
#
# print(c.fetchall())
# conn.commit()
# conn.close()


class ContactsDb:
    def __init__(self):
        self.connection = sqlite3.connect("contacts.db")
        self.createContactsTable()
        tags = ['sport', 'university', 'work', 'cinema']
        self.createTagTable(tags)
        self.createContactsTagTable()

    """
    TRIGGER EVENT
    """

    def createTrigger(self):
        pass


    """
    CONTACTS TABLE
    """

    def createContactsTable(self):
        # create a new contacts table in db if it doesn't exist yet
        self.connection.execute("""CREATE TABLE IF NOT EXISTS contacts(
            id integer,
            name text,
            surname text,
            phone integer,
            email text,
            notes text
            )""")
        self.connection.commit()

    def deleteTable(self, table_name):
        query = "DROP TABLE IF EXISTS " + table_name
        self.connection.execute(query)
        self.connection.commit()

    def generateNewContactId(self):
        # generate new contact id as (max + 1) of id in db
        if self.connection.execute("SELECT count(*) FROM contacts").fetchone()[0] != 0:
            new_id = int((self.connection.execute("SELECT max(id) FROM contacts").fetchone()[0])) + 1
        else:
            new_id = 0
        return new_id

    def addContact(self, contact):
        # generate new id for the contact
        self.connection.execute("INSERT INTO contacts VALUES (:id, :name ,:surname, :phone, :email, :notes)",
                                {
                                    'id': contact.id,
                                    'name': contact.name,
                                    'surname': contact.surname,
                                    'phone': contact.phone,
                                    'email': contact.email,
                                    'notes': contact.notes
                                })
        self.connection.commit()

    def deleteContact(self, contact_id):
        self.connection.execute("DELETE FROM contacts WHERE id=:id", {'id': contact_id})
        self.connection.commit()

    def getAllContacts(self, field_to_sort='name', mode='ASC'):
        # return a list of contacts with all fields (ordered by name mode ASC or DESC)
        field_2 = ('surname' if field_to_sort == 'name' else 'name')
        query = "SELECT * FROM contacts ORDER BY " + field_to_sort + " COLLATE NOCASE " + mode + " , " + field_2
        all_contacts = [c for c in self.connection.execute(query).fetchall()]
        return all_contacts

    def getContactInfo(self, contact_id):
        query = 'SELECT id, name, surname,phone,email, notes FROM contacts WHERE id =' + str(contact_id)
        contact_details = self.connection.execute(query).fetchone()
        # print('contact_details:  ', contact_details)
        return contact_details

    def updateContact(self, contact_id, name, surname, phone, email, notes):
        # update info for the contact specified in the contact_id
        # contact is ContactModel obj
        # print('updateContact: ', name, ' ', surname)
        query = "UPDATE contacts SET name=" + str("'") + name + str("'") + ", surname=" + str("'") + surname + str("'") + \
                ', phone =' + str("'") + str(phone) + str("'") + ', email=' + str("'") + email + str("'") + ', notes=' + str("'") + notes + str("'") + ' WHERE id = ' + str(contact_id)
        self.connection.execute(query)
        self.connection.commit()

    def isContactInDb(self, contact_id):
        # return True if contact relative to contact_id is in contacts table else False
        if contact_id is None:
            return False
        query = 'SELECT name from contacts Where id =' + str(contact_id)
        # print('is contact in db: ', contact_id, ' ', query)
        contact = self.connection.execute(query).fetchone()
        return contact is not None

    def removeContact(self, contact_id):
        # remove contact from contacts db
        query = "DELETE FROM contacts WHERE id=" + str(contact_id)
        self.connection.execute(query)
        self.connection.commit()

    def searchWord(self, word):
        # # TODO fix
        # self.connection.execute("CREATE VIRTUAL TABLE IF NOT EXISTS complete USING fts5(id,name,surname,phone,email,notes)")
        # query = "SELECT * FROM complete WHERE complete = " + word
        # match = self.connection.execute(query)
        # # match = self.connection.execute("SELECT count(*), * FROM complete")
        # # print([el for el in match])
        query = "SELECT id FROM contacts WHERE name LIKE " + str("'%") + word + str("%' or surname LIKE ") + str("'%") + word + str("%' or phone LIKE ") + str("'%") + word + str("%' or email LIKE ") + str("'%") + word + str("%' or notes LIKE ") + str("'%") + word + str("%'")

        # list of ids of contacts in which the term is present
        ww = [el[0] for el in self.connection.execute(query).fetchall()]
        return ww

    """
    TAGS TABLE
    """

    def createTagTable(self, tag_list):
        # create a new tags table in db if it doesn't exist yet (tag_list starting list of tags)
        self.connection.execute("CREATE TABLE IF NOT EXISTS tags(tag text)")
        self.connection.commit()
        for tag in tag_list:
            self.addTag(tag)

    def addTag(self, tag_name: str) -> bool:
        # add tag to tags table if not already present
        tags = self.getAllTags()
        if tag_name not in tags:
            query = "INSERT INTO tags VALUES (" + str("'") + tag_name + str("'") + ")"
            self.connection.execute(query)
            self.connection.commit()
            return True
        return False

    def getAllTags(self):
        # get list of tags in tags table
        return [tag[0] for tag in self.connection.execute("SELECT * FROM tags ORDER BY tag COLLATE NOCASE").fetchall()]

    def deleteTag(self, tag):
        # delete tag
        # TODO: warning!! se cancello un tag poi devo andare a verificare se il tag è presente nei contatti e casomai levarlo
        query = "DELETE FROM tags WHERE Tag='" + tag + "'"
        self.connection.execute(query)
        self.connection.commit()

    """
    CONTACTS - TAGS TABLE
    """

    def createContactsTagTable(self):
        self.connection.execute("CREATE TABLE IF NOT EXISTS contacts_tags(contact_id text, tag text )")
        self.connection.commit()

    def setContactTags(self, contact_id, tags):
        # tags is a list of tags
        for tag in tags:
            self.setContactTag(contact_id, tag)

    def setContactTag(self, contact_id, tag):
        # set tag for a contact
        query = "INSERT INTO contacts_tags VALUES (" + contact_id + ", " + str("'") + tag + str("')")  # (12, 'school')"
        self.connection.execute(query)
        self.connection.commit()

    def getContactTags(self, contact_id):
        assert type(contact_id) == str
        return [tag[0] for tag in self.connection.execute("SELECT tag FROM contacts_tags WHERE contact_id = '" + contact_id + "' ").fetchall()]

    def removeContactTag(self, contact_id, tag=None):
        if tag is not None:
            # delete specific entry in contacts_tags table
            self.connection.execute("DELETE FROM contacts_tags WHERE contact_id='" + str(contact_id) + "' and tag='" + tag + "'")
            self.connection.commit()
        else:
            # delete all entries in contacst_tags  table where id == contact_id
            self.connection.execute("DELETE FROM contacts_tags WHERE contact_id='" + str(contact_id) + "'")
            self.connection.commit()

    def getAllContactsTags(self):
        # list of (contact_id, tag) ...
        return [tag for tag in self.connection.execute("SELECT * FROM contacts_tags ORDER BY tag COLLATE NOCASE").fetchall()]

    def getContactsFromTag(self, tag):
        # get list of contacts_id for the given tag
        return [int(c_id[0]) for c_id in self.connection.execute("SELECT contact_id FROM contacts_tags WHERE tag='" + tag + "'")]



# db = ContactsDb()
# db.deleteTag(' ')
# print(db.getAllContactsTags())
# db.setContactTag('12', 'sport')
# db.setContactTag('12', 'uni')
# print(db.getContactTags('12'))
# # db.deleteTable('tags')
# print(db.addTag('Work'))
# print(db.getAllTags())

# print(db.searchWord('Gi'))

# # DB.connection.execute("ATTACH contacts.db AS my_db")
# # tab = DB.connection.execute("SELECT name FROM contacts.db.sqlite_master WHERE type='table'")
# # print(tab)
# DB.createTable()
# print(DB.isContactInDb(17))
# DB.deleteContactTable('contacts')
# DB.searchWord('1')
# print([el for el in DB.getAllContacts()])
# contact1 = ContactModel('franci1', 'dellu', 43564, 'dsad@dss', 'dwdwds')
# DB.addContact(contact1)
# DB.deleteContact(0)
