from PyQt5.QtWidgets import QDialog, QDialogButtonBox
from ui.formDialog_ui import Ui_new_contact_form
from contactsModel import ContactModel, ContactsListModel


class NewContactView(QDialog):
    def __init__(self, contacts_model):
        super(NewContactView, self).__init__()
        self.ui = Ui_new_contact_form()
        self.ui.setupUi(self)

        # all contacts model (obj ContactsListModel)
        self.contacts_list_model = contacts_model

        # update contact_id when updating
        self.contact_id = None
        self.ui.buttonBox.button(QDialogButtonBox.Save).setEnabled(False)
        # get user inputs for the new contact
        # self.ui.buttonBox.accepted.connect(lambda: self.model.addContact(ContactModel(
        #     self.ui.name_lineEdit.text(), self.ui.surname_lineEdit.text(),
        #     self.ui.phone_lineEdit.text(), self.ui.email_lineEdit.text(),
        #     self.ui.notes_textEdit.toPlainText())))

        self.ui.buttonBox.accepted.connect(lambda: self.contacts_list_model.submitContact(self.contact_id,
                                                                                          self.ui.name_lineEdit.text(),
                                                                                          self.ui.surname_lineEdit.text(),
                                                                                          self.ui.phone_lineEdit.text(),
                                                                                          self.ui.email_lineEdit.text(),
                                                                                          self.ui.notes_textEdit.toPlainText()))

        # clear text input lines
        self.ui.buttonBox.accepted.connect(self.clearLines)
        self.ui.buttonBox.rejected.connect(self.clearLines)

        # Enable save button when Name and Surname are given
        self.ui.name_lineEdit.textChanged.connect(self.onChangeLine)
        self.ui.surname_lineEdit.textChanged.connect(self.onChangeLine)

    def onAccepted(self, name, surname, phone, email, notes):
        pass

    def onChangeLine(self):
        # Check if name and surname lines are empty or not, if they are given -> enable save button
        if self.ui.name_lineEdit.text() is not None and self.ui.name_lineEdit.text() != '' and self.ui.surname_lineEdit.text() is not None and self.ui.surname_lineEdit.text() != '':
            self.ui.buttonBox.button(QDialogButtonBox.Save).setEnabled(True)
        else:
            self.ui.buttonBox.button(QDialogButtonBox.Save).setEnabled(False)

    def clearLines(self):
        # clear form lines when window is closed
        self.ui.name_lineEdit.clear()
        self.ui.surname_lineEdit.clear()
        self.ui.phone_lineEdit.clear()
        self.ui.email_lineEdit.clear()
        self.ui.notes_textEdit.clear()

    def setContact(self, contact_id):
        self.contact_id = contact_id
        self.setContactDetails(self.contact_id)

    def setContactDetails(self, contact_id):
        # used to modify existing contact
        print(contact_id, 'contact_id')
        info = self.contacts_list_model.getContactInfo(contact_id)
        assert len(info) == 6
        self.ui.name_lineEdit.setText(info[1])
        self.ui.surname_lineEdit.setText(info[2])
        self.ui.phone_lineEdit.setText(str(info[3]))
        self.ui.email_lineEdit.setText(info[4])
        self.ui.notes_textEdit.setText(info[5])


class NewContactView_(QDialog):
    def __init__(self, model):
        super(NewContactView_, self).__init__()
        self.ui = Ui_new_contact_form()
        self.ui.setupUi(self)
        self.model = model

        self.ui.buttonBox.button(QDialogButtonBox.Save).setEnabled(False)

        # Enable save button when Name and Surname are given
        self.ui.name_lineEdit.textChanged.connect(self.onChangeLine)
        self.ui.surname_lineEdit.textChanged.connect(self.onChangeLine)

    def onChangeLine(self):
        # Check if name and surname lines are empty or not, if they are given -> enable save button
        if self.ui.name_lineEdit.text() is not None and self.ui.name_lineEdit.text() != '' and self.ui.surname_lineEdit.text() is not None and self.ui.surname_lineEdit.text() != '':
            self.ui.buttonBox.button(QDialogButtonBox.Save).setEnabled(True)
        else:
            self.ui.buttonBox.button(QDialogButtonBox.Save).setEnabled(False)
