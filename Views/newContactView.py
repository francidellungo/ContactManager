from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QCheckBox, QMessageBox, QInputDialog
from ui.formDialog_ui import Ui_new_contact_form
from contactsModel import ContactModel, ContactsListModel


class NewContactView(QDialog):
    tag_added = pyqtSignal()

    def __init__(self, contacts_model, tags_model):  # , contacts_tags_model
        super(NewContactView, self).__init__()
        self.ui = Ui_new_contact_form()
        self.ui.setupUi(self)

        # all contacts model (obj ContactsListModel)
        self.contacts_list_model = contacts_model
        self.tags_model = tags_model
        # self.contacts_tags_model = contacts_tags_model

        # update contact_id when updating existent contact
        self.contact_id = None
        self.ui.buttonBox.button(QDialogButtonBox.Save).setEnabled(False)

        # get user inputs for the new contact
        self.ui.buttonBox.accepted.connect(self.onAccepted)
        self.ui.add_tag_pb.clicked.connect(self.addTag)
        # self.ui.buttonBox.accepted.connect(lambda: self.contacts_list_model.submitContact(self.contact_id,
        #                                                                                   self.ui.name_lineEdit.text(),
        #                                                                                   self.ui.surname_lineEdit.text(),
        #                                                                                   self.ui.phone_lineEdit.text(),
        #                                                                                   self.ui.email_lineEdit.text(),
        #                                                                                   self.ui.notes_textEdit.toPlainText()))
        # self.ui.buttonBox.accepted.connect(self.)

        # signal when contact is edited

        # clear text input lines
        self.ui.buttonBox.accepted.connect(self.clearLines)
        self.ui.buttonBox.rejected.connect(self.clearLines)

        # Enable save button when Name and Surname are given
        self.ui.name_lineEdit.textChanged.connect(self.onChangeLine)
        self.ui.surname_lineEdit.textChanged.connect(self.onChangeLine)

    def onAccepted(self):
        # submit new contact details and tags to model
        tags_checked = [self.ui.tags_layout.itemAt(i).widget().objectName() for i in range(self.ui.tags_layout.count())
                        if self.ui.tags_layout.itemAt(i).widget().isChecked() is True]
        self.contacts_list_model.submitContact(self.contact_id,
                                               self.ui.name_lineEdit.text(),
                                               self.ui.surname_lineEdit.text(),
                                               self.ui.phone_lineEdit.text(),
                                               self.ui.email_lineEdit.text(),
                                               self.ui.notes_textEdit.toPlainText(),
                                               tags_checked)

        # submit modifications to contact tags+
        # self.ui.tag1_checkBox.isChecked()
        # self.ui.tag1_checkBox.setChecked(True)

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

        # remove all tags (get ready for next time the view is open, there could be different tags!)
        for i in range(self.ui.tags_layout.count()):
            self.ui.tags_layout.itemAt(i).widget().deleteLater()
            # self.ui.tags_layout.itemAt(i).widget().setChecked(False)

    def setContact(self, contact_id):
        # set contact id
        self.contact_id = contact_id
        self.setContactDetails(self.contact_id)

    def setContactDetails(self, contact_id):
        # used to modify existing contact
        # self.clearLines()
        # TODO fix contact_id must be str, but here is int and is fixed here but it's not ok
        print(contact_id, 'contact_id')
        # contact info
        info = self.contacts_list_model.getContactInfo(contact_id)
        assert len(info) == 6
        self.ui.name_lineEdit.setText(info[1])
        self.ui.surname_lineEdit.setText(info[2])
        self.ui.phone_lineEdit.setText(str(info[3]))
        self.ui.email_lineEdit.setText(info[4])
        self.ui.notes_textEdit.setText(info[5])

        # set contact tags
        contact_tags = self.contacts_list_model.getContactTags(str(contact_id))
        self.setTags(contact_tags)

    def setTags(self, contact_tags=None):
        all_tags = self.contacts_list_model.getAllTags()
        for tag in all_tags:
            tag_w = QCheckBox()
            tag_w.setObjectName(tag)
            tag_w.setText(tag)
            if contact_tags is not None and tag in contact_tags:
                tag_w.setChecked(True)
            self.ui.tags_layout.addWidget(tag_w)

    def addTag(self):
        all_tags = self.contacts_list_model.getAllTags()

        text, ok = QInputDialog.getText(self, 'New tag', 'Enter new tag:')
        while ok and (text == '' or text in all_tags):
            if text == '':
                text, ok = QInputDialog.getText(self, 'New tag', text + ' Please enter a valid tag:')
            elif text in all_tags:
                text, ok = QInputDialog.getText(self, 'New tag', text + ' tag already exists,\n please enter new tag:')

        if ok and text not in all_tags:
            self.tags_model.newTag(text)
            # tag added signal emitted
            self.tag_added.emit()
            # TODO finish tag added signal

        # refresh list of tags
        for i in range(self.ui.tags_layout.count()):
            self.ui.tags_layout.itemAt(i).widget().deleteLater()
        self.setTags(self.contacts_list_model.getContactTags(self.contact_id))

    #TODO finish add new tag!
