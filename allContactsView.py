# from PyQt5 import QtWidgets
# from PyQt5.QtCore import pyqtSignal
# from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QDialogButtonBox
# from ui.mainWindow_ui import Ui_MainWindow
# from ui.formDialog_ui import Ui_new_contact_form
# from ui.contactDetails_ui import Ui_Dialog
# from contactsModel import ContactsModel, ContactModel
# import sys
#
# # TODO remove this at the end of the project
# """
# All functions and classes names are thisKindOfTypo, and variables are this_kind_of_typo
# """
# """
# See https://www.tutorialspoint.com/pyqt/pyqt_qstackedwidget.htm for QStackedWidget to switch between windows
# """
#
#
# class NewContactView(QDialog):
#     def __init__(self, model):
#         super(NewContactView, self).__init__()
#         self.ui = Ui_new_contact_form()
#         self.ui.setupUi(self)
#         self.model = model
#         self.contact_id = None
#         self.ui.buttonBox.button(QDialogButtonBox.Save).setEnabled(False)
#
#         # get user inputs for the new contact
#         # self.ui.buttonBox.accepted.connect(lambda: self.model.addContact(ContactModel(
#         #     self.ui.name_lineEdit.text(), self.ui.surname_lineEdit.text(),
#         #     self.ui.phone_lineEdit.text(), self.ui.email_lineEdit.text(),
#         #     self.ui.notes_textEdit.toPlainText())))
#
#         # maybe todo: fix this below should emit a signal and send contact -> model should think about creating a new contact
#         self.ui.buttonBox.accepted.connect(lambda: self.model.submitContact(self.contact_id, ContactModel(
#             self.ui.name_lineEdit.text(), self.ui.surname_lineEdit.text(),
#             self.ui.phone_lineEdit.text(), self.ui.email_lineEdit.text(),
#             self.ui.notes_textEdit.toPlainText())))
#
#         # clear text input lines
#         self.ui.buttonBox.accepted.connect(self.clearLines)
#         self.ui.buttonBox.rejected.connect(self.clearLines)
#
#         # Enable save button when Name and Surname are given
#         self.ui.name_lineEdit.textChanged.connect(self.onChangeLine)
#         self.ui.surname_lineEdit.textChanged.connect(self.onChangeLine)
#
#     def onChangeLine(self):
#         # Check if name and surname lines are empty or not, if they are given -> enable save button
#         if self.ui.name_lineEdit.text() is not None and self.ui.name_lineEdit.text() != '' and self.ui.surname_lineEdit.text() is not None and self.ui.surname_lineEdit.text() != '':
#             self.ui.buttonBox.button(QDialogButtonBox.Save).setEnabled(True)
#         else:
#             self.ui.buttonBox.button(QDialogButtonBox.Save).setEnabled(False)
#
#     def clearLines(self):
#         # clear form lines when window is closed
#         self.ui.name_lineEdit.clear()
#         self.ui.surname_lineEdit.clear()
#         self.ui.phone_lineEdit.clear()
#         self.ui.email_lineEdit.clear()
#         self.ui.notes_textEdit.clear()
#
#     def setContact(self, contact_id):
#         self.contact_id = contact_id
#         self.setContactDetails(self.contact_id)
#
#     def setContactDetails(self, contact_id):
#         # used to modify existing contact
#         print(contact_id, 'contact_id')
#         info = self.model.getContactInfo(contact_id)
#         assert len(info) == 5
#         self.ui.name_lineEdit.setText(info[0])
#         self.ui.surname_lineEdit.setText(info[1])
#         self.ui.phone_lineEdit.setText(str(info[2]))
#         self.ui.email_lineEdit.setText(info[3])
#         self.ui.notes_textEdit.setText(info[4])
#
#
# class ContactDetails(QDialog):
#     def __init__(self, model):
#         super(ContactDetails, self).__init__()
#         self.ui = Ui_Dialog()
#         self.ui.setupUi(self)
#         self.contact = None
#
#         self.model = model
#
#         # when window is closed clear lines
#         self.ui.back_pb.clicked.connect(self.clearLines)
#         self.ui.edit_pb.clicked.connect(self.clearLines)
#
#         # delete contact behavior
#         self.ui.delete_pb.clicked.connect(self.deleteContact)
#
#     def deleteContact(self):
#         pass
#         #TODO finish call model function to removw contact from db
#
#     def showDetails(self, contact_id):
#         contact_details = list(self.model.getContactInfofromId(contact_id))[1:]
#         self.ui.contact_label.setText(contact_details[0] + ' ' + contact_details[1])
#         for detail in contact_details:
#             self.ui.contact_info_layout.addWidget(QtWidgets.QLabel((str(detail) if detail is not None else ' ')))
#
#     def clearLines(self):
#         self.ui.contact_label.clear()
#         for i in reversed(range(self.ui.contact_info_layout.count())):
#             item = self.ui.contact_info_layout.itemAt(i).widget()
#             item.deleteLater()
#
#     def setContact(self, contact):
#         self.contact = contact
#
#         # self.ui.surname_lineEdit.clear()
#         # self.ui.phone_lineEdit.clear()
#         # self.ui.email_lineEdit.clear()
#
#         # self.ui.contact_info_layout.addWidget(QtWidgets.QLabel(contact_details[2]))
#         # self.ui.contact_info_layout.addWidget(QtWidgets.QLabel(str(contact.surname)))
#
#
# class ContactManagerView(QMainWindow):
#     contact_clicked = pyqtSignal(int)
#
#     def __init__(self, model):
#         super(ContactManagerView, self).__init__()
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#
#         # db of contacts
#         self.model = model
#         self.showContacts()
#
#         # connect buttons to slots
#         # self.ui.newContact_pb.clicked.connect(self.createNewContact)
#         self.ui.sort_combobox.currentIndexChanged.connect(self.sortBy)
#
#         self.model.contact_added.connect(self.refreshContacts)
#
#     def showContacts(self, contacts_=None):
#         contacts = (contacts_ if contacts_ is not None else self.model.getAllContacts())
#         for id, contact in enumerate(contacts):
#             new_contact = QtWidgets.QPushButton(self.ui.contacts_scrollAreaW)
#             new_contact.setFlat(True)
#             # new_label.setParent(self.ui.contacts_scrollAreaW)
#             new_contact.setText(contact[1] + ' ' + contact[2])
#             new_contact.setObjectName(str(contact[0]))
#             if id != 0:
#                 line = QtWidgets.QFrame(self.ui.contacts_scrollAreaW)
#                 line.setFrameShape(QtWidgets.QFrame.HLine)
#                 line.setFrameShadow(QtWidgets.QFrame.Sunken)
#                 line.setObjectName("line")
#                 self.ui.contacts_layout.addWidget(line)
#             self.ui.contacts_layout.addWidget(new_contact)
#             new_contact.clicked.connect(lambda: self.clicked(new_contact))
#
#     def refreshContacts(self, contacts=None):
#         for i in reversed(range(self.ui.contacts_layout.count())):
#             item = self.ui.contacts_layout.itemAt(i).widget()
#             item.deleteLater()
#             # self.ui.contacts_layout.removeWidget(item)
#         print('removed all contacts', self.ui.contacts_layout.count())
#         self.showContacts(contacts)
#
#     def sortBy(self, field, mode='ASC'):
#         # field to sort by
#         # print('sort by', field)
#         # TODO sort also by number or email ??
#         field_to_sort = ('name' if field == 0 else 'surname')
#         contacts = self.model.getAllContacts(field_to_sort)
#         self.refreshContacts(contacts)
#         pass
#
#     def clicked(self, contact):
#         # contact_id = int(contact.objectName())
#         sender_id = int(self.sender().objectName())
#         print('contact clicked, sender_id: ', sender_id)
#         # print('sender_id', contact_id, ' ', sender_id, ' ', type(sender_id))
#         # contact_info = self.model.getContactInfo(sender_id)
#         # send id of the contact
#         self.contact_clicked.emit(sender_id)
#
#     # def addRow(self, name, surname):
#     #     """
#     #     Add new contact to contacts GUI
#     #     :param name:
#     #     :param surname:
#     #     :return:
#     #     """
#     #     new_contact = QtWidgets.QPushButton(self.ui.contacts_scrollAreaW)
#     #     new_contact.setFlat(True)
#     #     new_contact.setText(name + ' ' + surname)
#     #     new_contact.clicked.connect(self.button_clicked.emit)
#     #
#     #     line = QtWidgets.QFrame(self.ui.contacts_scrollAreaW)
#     #     line.setFrameShape(QtWidgets.QFrame.HLine)
#     #     line.setFrameShadow(QtWidgets.QFrame.Sunken)
#     #     line.setObjectName("line")
#     #     self.ui.contacts_layout.addWidget(line)
#     #     self.ui.contacts_layout.addWidget(new_contact)
#     #     # new_contact.clicked.connect(self.clicked)
#
#
#
#     # def createNewContact(self):
#     #     """
#     #     Open form dialog to create new contact
#     #     :return:
#     #     """
#     #     self.dialog = QtWidgets.QDialog()
#     #     self.dialog.ui = Ui_new_contact_form()
#     #     self.dialog.ui.setupUi(self.dialog)
#     #     # self.ui.mainWindow.close()
#     #     # in mainWindow.py file:         self.mainWindow = MainWindow
#     #     self.dialog.show()
#     #
#     #     # name = self.dialog.ui.name_lineEdit.text()
#     #     # surname = self.dialog.ui.surname_lineEdit.text()
#     #     # phone = self.dialog.ui.phone_lineEdit.text()
#     #     # email = self.dialog.ui.email_lineEdit.text()
#     #     # notes = self.dialog.ui.notes_textEdit.toPlainText()
#     #
#     #     # new_contact = ContactModel(name, surname, phone, email, notes)
#     #
#     #     self.dialog.ui.buttonBox.accepted.connect(lambda: self.model.addContact(ContactModel(
#     #         self.dialog.ui.name_lineEdit.text(), self.dialog.ui.surname_lineEdit.text(),
#     #         self.dialog.ui.phone_lineEdit.text(), self.dialog.ui.email_lineEdit.text(),
#     #         self.dialog.ui.notes_textEdit.toPlainText())))
#     #
#     #     self.dialog.ui.buttonBox.accepted.connect(lambda: self.save(self.dialog.ui.name_lineEdit.text(), self.dialog.ui.surname_lineEdit.text()))
#
#
#     # def save(self, name, surname):
#     #     """
#     #     Save new contact in DB
#     #     :param name:
#     #     :param surname:
#     #     :return:
#     #     """
#     #     print('accept')
#     #     # TODO validate input before save
#     #     self.addRow(name, surname)
#     #     # save in DB and show contacts in DB
#
#
# # if __name__== "__main__":
# #     app = QApplication(sys.argv)
# #     window = ContactManagerView()
# #     window.show()
# #     sys.exit(app.exec_())
