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
        self.createTagTable()

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

    def deleteContactTable(self, table_name):
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

    def createTagTable(self):
        # create a new tags table in db if it doesn't exist yet
        self.connection.execute("CREATE TABLE IF NOT EXISTS TAGS(TAG TEXT)")
        self.connection.commit()


# db = ContactsDb()
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
