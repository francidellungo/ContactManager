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


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("contacts.db")
        # self.createTable()
        # cur = self.connection.cursor()
        # cur.execute('pragma compile_options;')
        # available_pragmas = cur.fetchall()
        # if ('ENABLE_FTS5',) in available_pragmas:
        #     print('ENABLE_FTS5 YES')
        # else:
        #     print('ENABLE_FTS5 NO')

    def createTable(self):
        # create a new table in db if it doesn't exist yet
        self.connection.execute("""CREATE TABLE IF NOT EXISTS contacts(
            id text,
            name text,
            surname text,
            phone integer,
            email text,
            notes text
            )""")
        self.connection.commit()

    def deleteContactTable(self, table_name):
        # TODO fix -> non funziona!
        self.connection.execute("DROP TABLE IF EXISTS :table_", {'table_': table_name})
        self.connection.commit()

    def addContact(self, contact):
        new_id = self.connection.execute("SELECT max(id) FROM contacts") + 1
        self.connection.execute("INSERT INTO contacts VALUES (:id, :name ,:surname, :phone, :email, :notes)",
                                {
                                    'id': new_id,
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

    def getAllContacts(self):
        # return a list of contacts with all fields
        all_contacts = self.connection.execute("SELECT * FROM contacts")
        return all_contacts

    def searchWord(self, word):
        # TODO fix
        self.connection.execute("CREATE VIRTUAL TABLE IF NOT EXISTS complete USING fts5(id,name,surname,phone,email,notes)")
        # match = self.connection.execute("SELECT * FROM complete WHERE complete = :word", {'word': word})
        match = self.connection.execute("SELECT count(*), * FROM complete")
        print([el for el in match])


# DB = Database()
# DB.createTable()
# DB.searchWord('1')
# print([el for el in DB.getAllContacts()])
# contact1 = ContactModel('franci1', 'dellu', 43564, 'dsad@dss', 'dwdwds')
# DB.addContact(contact1)
# DB.deleteContact(0)
