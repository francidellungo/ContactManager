from typing import Dict

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow
from ui.mainWindow_ui import Ui_MainWindow


class AllContactsView(QMainWindow):
    contact_clicked = pyqtSignal(int)

    def __init__(self, model, t_model):
        super(AllContactsView, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.sort_fields = {'name': 0,
                            'surname': 1}

        # db of contacts
        self.model = model
        self.tags_model = t_model
        self.showContacts()

        # set tags
        self.ui.tags_combo_box.addItems(self.tags_model.getAllTags())

        # connect buttons to slots
        self.ui.sort_combobox.currentIndexChanged.connect(self.showContacts)
        self.ui.search_pb.clicked.connect(self.showContacts)

        # enter button clicked on search line -> search term on line edit
        self.ui.search_line_edit.editingFinished.connect(self.showContacts)

        # changed tag entry
        self.ui.tags_combo_box.currentIndexChanged.connect(self.showContacts)

        # refresh contacts list if a contact is added or removed
        # TODO:
        self.model.contact_added.connect(self.showContacts)
        self.model.contact_removed.connect(self.showContacts)
        self.model.contact_updated.connect(self.showContacts)

    def showContacts(self, contacts_=None):
        # clear contacts
        self.refreshContacts()
        # TODO check tag field, ordinamento and search
        # contacts = (contacts_ if contacts_ is not None else self.model.getAllContacts())

        # check order by (name/surname)
        sort_id = self.ui.sort_combobox.currentIndex()

        sorted_contacts = self.sortBy(list(self.sort_fields.keys())[sort_id])  # list of (id, name, surname) of sorted contacts
        contacts = [c for c in sorted_contacts]

        # check search bar
        if self.ui.search_line_edit.text() != '':
            term = self.ui.search_line_edit.text()
            contacts_ids_s = self.model.searchTerm(term)  # list of id of the contacts
            contacts = [c for c in contacts if c[0] in contacts_ids_s]

        # TODO: check tag ...
        if self.ui.tags_combo_box.currentText() != '':
            contacts_ids_t = self.model.getContactsFromTag(self.ui.tags_combo_box.currentText())
            contacts = [c for c in contacts if c[0] in contacts_ids_t]

        # contacts = self.model.getAllContacts()
        for id, contact in enumerate(contacts):
            new_contact = QtWidgets.QPushButton(self.ui.contacts_scrollAreaW)
            new_contact.setFlat(True)
            # new_label.setParent(self.ui.contacts_scrollAreaW)
            new_contact.setText(contact[1] + ' ' + contact[2])
            new_contact.setObjectName(str(contact[0]))
            if id != 0:
                line = QtWidgets.QFrame(self.ui.contacts_scrollAreaW)
                line.setFrameShape(QtWidgets.QFrame.HLine)
                line.setFrameShadow(QtWidgets.QFrame.Sunken)
                line.setObjectName("line")
                self.ui.contacts_layout.addWidget(line)
            self.ui.contacts_layout.addWidget(new_contact)
            new_contact.clicked.connect(self.clicked)

    def refreshContacts(self, contacts=None):
        for i in reversed(range(self.ui.contacts_layout.count())):
            item = self.ui.contacts_layout.itemAt(i).widget()
            item.deleteLater()
            # self.ui.contacts_layout.removeWidget(item)
        # print('removed all contacts', self.ui.contacts_layout.count())
        # self.showContacts(contacts)

    def sortBy(self, field, mode='ASC'):
        # field name to sort by
        # field_to_sort = ('name' if field == 0 else 'surname')
        contacts = self.model.getAllContacts(field)
        # self.refreshContacts(contacts)
        return contacts

    def clicked(self):
        sender_id = int(self.sender().objectName())
        print('contact clicked, sender_id: ', sender_id)
        # send id of the contact
        self.contact_clicked.emit(sender_id)

    def searchTerm(self):
        # TODO: search more than one word
        term = self.ui.search_line_edit.text()
        contacts_ids = self.model.searchTerm(term)
        # self.showContacts(contacts_ids)
        print(contacts_ids)

